import flask


def find_contacts_by_name(name, exclude_directory=None):
    return flask.render_template("api/contact-search-results.html", name=name)
