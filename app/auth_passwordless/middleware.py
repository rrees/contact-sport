import flask


def check_session(url_prefix, session_key):
    def check_session_middleware():
        flask.current_app.logger.debug("Check session middleware starting")

        current_request = flask.request

        if current_request.path.startswith(url_prefix):
            return

        flask.current_app.logger.debug(f"Rule name: {flask.request.url_rule.endpoint}")

        if current_request.url_rule.endpoint == "index":
            return

        if session_key in flask.session:
            return

        flask.current_app.logger.info("Attempt to access page requiring authentication")
        return flask.redirect(flask.url_for("index"))

    return check_session_middleware
