import flask

from . import forms

URL_PREFIX = "/auth"

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
        return flask.redirect(flask.url_for("passwordless.login_sent"))

    return flask.redirect(flask.url_for("passwordless.login"))


@passwordless_blueprint.route("/login/sent")
def login_sent():
    return flask.render_template(("login-sent.html"))


def check_session():
    flask.current_app.logger.debug("Check session middleware starting")

    flask.current_app.logger.debug(f"Rule name: {flask.request.url_rule.endpoint}")

    current_request = flask.request

    if current_request.url_rule.endpoint == "index":
        return

    if current_request.path.startswith(URL_PREFIX):
        return

    if "authenticated" in flask.session:
        return

    flask.current_app.logger.info("Attempt to access page requiring authentication")
    return flask.redirect(flask.url_for("index"))


passwordless_blueprint.before_app_request(check_session)
