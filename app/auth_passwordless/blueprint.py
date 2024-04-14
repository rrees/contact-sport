import flask
from uuid import uuid4

from . import forms
from . import middleware

from .services import email
from .services import tokens
from .services import user_session

URL_PREFIX = "/auth"
AUTH_SESSION_KEY = "authenticated"

passwordless_blueprint = flask.Blueprint(
    "passwordless", __name__, template_folder="templates", url_prefix=URL_PREFIX
)


@passwordless_blueprint.route("/login")
def login():
    return flask.render_template("login.html")


@passwordless_blueprint.route("/login/form", methods=["POST"])
def login_form():
    login_form = forms.Login(flask.request.form)

    if login_form.validate():
        flask.current_app.logger.info(login_form.email.data)
        token = tokens.create_token()
        email.send_email()
        return flask.redirect(flask.url_for("passwordless.login_sent"))

    return flask.redirect(flask.url_for("passwordless.login"))


@passwordless_blueprint.route("/login/sent")
def login_sent():
    return flask.render_template(("login-sent.html"))


@passwordless_blueprint.route("/login/redeem/<token>")
def login_with_token(token):
    user_session.create_session(sesssion_key=AUTH_SESSION_KEY)
    return flask.redirect(flask.url_for("home"))


@passwordless_blueprint.route("/logout")
def logout():
    flask.session.pop(AUTH_SESSION_KEY, None)
    return flask.redirect(flask.url_for("index"))


passwordless_blueprint.before_app_request(
    middleware.check_session(URL_PREFIX, AUTH_SESSION_KEY)
)
