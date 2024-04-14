from uuid import uuid4

import flask


def create_session(session_key):
    flask.session[session_key] = uuid4()
