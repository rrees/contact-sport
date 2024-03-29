import logging
import os

import flask

from . import forms

_log = logging.getLogger(__name__)

ADMIN_EMAILS = os.environ["ADMIN_USERNAMES"].split(",")
ADMIN_PASSWORD = os.environ["PASSWORD"]


def login_form():
    login_form = forms.Login(flask.request.form)
    if (
        login_form.validate()
        and login_form.password.data == ADMIN_PASSWORD
        and login_form.username.data in ADMIN_USERNAMES
    ):
        flask.session["username"] = login_form.username.data
        flask.session.permanent = True
        return flask.redirect(flask.url_for("home"))

    return flask.redirect(flask.url_for("index"))
