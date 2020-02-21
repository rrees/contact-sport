import flask

from . import forms

passwordless_blueprint =  flask.Blueprint('passwordless', __name__, template_folder="templates")

@passwordless_blueprint.route('/login')
def login():
	return flask.render_template('login.html')

@passwordless_blueprint.route('/login/form', methods=['POST'])
def login_form():
	login_form = forms.Login(flask.request.form)

	if login_form.validate():
		return flask.redirect(flask.url_for('passwordless.login_sent'))

	return flask.redirect(flask.url_for('passwordless.login'))

@passwordless_blueprint.route('/login/sent')
def login_sent():
	return flask.render_template(('login-sent.html'))