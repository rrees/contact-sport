import flask

from app.repositories import contacts as contacts_repository


def find_contacts_by_name(name, exclude_directory=None):
    matching_contacts = contacts_repository.by_name(name)

    return flask.render_template(
        "api/contact-search-results.html", name=name, contacts=matching_contacts
    )
