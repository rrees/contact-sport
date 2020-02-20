import flask

passwordless_blueprint =  flask.Blueprint('passwordless', __name__, template_folder="templates")

@passwordless_blueprint.route('/login')
def login():
	return flask.render_template('login.html')