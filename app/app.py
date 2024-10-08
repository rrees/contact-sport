import os
import logging

import flask


from . import handlers
from . import redis_utils

from app.auth_passwordless.blueprint import passwordless_blueprint

ENV = os.environ.get("ENV", "PROD")

redis_url = os.environ.get("REDIS_URL", None)

redis = redis_utils.setup_redis(redis_url) if redis_url else None

app = flask.Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", os.urandom(24))

app.logger.setLevel(logging.INFO)

routes = [
    # ("/", "index", handlers.pages.front_page, ["GET"]),
    ("/", "index", handlers.pages.home_page, ["GET"]),
    ("/home", "home", handlers.pages.home_page, ["GET"]),
    ("/contacts", "contacts", handlers.pages.contacts, ["GET"]),
    ("/contact/<contact_id>", "contact", handlers.pages.contact, ["GET"]),
] + handlers.routes

for path, endpoint, handler, methods in routes:
    app.add_url_rule(path, endpoint, handler, methods=methods)

app.register_blueprint(passwordless_blueprint)


@app.before_request
def before_request():
    def check_credentials(username, password):
        valid_users = os.environ.get("VALID_USERS").split(",")
        return username in valid_users and password == os.environ.get("ADMIN_PASSWORD")

    auth = flask.request.authorization
    if (
        not auth
        or not auth.username
        or not auth.password
        or not check_credentials(auth.username, auth.password)
    ):
        return flask.Response(
            "Please login", 401, {"WWW-Authenticate": 'Basic realm="contact-sport"'}
        )


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception("An error occurred during a request.")
    return "An internal error occurred.", 500
