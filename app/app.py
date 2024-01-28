import os
import logging
from logging.config import dictConfig

import flask


from . import handlers
from . import redis_utils
from app.auth_passwordless.blueprint import passwordless_blueprint

ENV = os.environ.get("ENV", "PROD")

redis_url = os.environ.get("REDIS_URL", None)

redis = redis_utils.setup_redis(redis_url) if redis_url else None

dictConfig(
    {
        "version": 1,
        "root": {
            "level": "INFO",
        },
    }
)

app = flask.Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", os.urandom(24))

routes = [
    ("/", "index", handlers.pages.front_page, ["GET"]),
    ("/home", "home", handlers.pages.home_page, ["GET"]),
]

for path, endpoint, handler, methods in routes:
    app.add_url_rule(path, endpoint, handler, methods=methods)

app.register_blueprint(passwordless_blueprint)


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception("An error occurred during a request.")
    return "An internal error occurred.", 500
