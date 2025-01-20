import flask

from app.models import Contact
from app.repositories import (
    contacts as contacts_repository,
    directories as directories_repository,
)


def front_page():
    return flask.render_template("index.html")


def home_page():
    return flask.render_template("home.html")


def contacts():
    return flask.render_template("contacts.html", contacts=contacts_repository.all())


def contact(contact_id):
    a_contact = contacts_repository.full(contact_id)
    contact_details = Contact.from_dict(a_contact)

    return flask.render_template("contact.html", contact=contact_details)


def directories():
    return flask.render_template(
        "directories/directories.html", directories=directories_repository.all()
    )


def directory(directory_id):
    return flask.render_template(
        "directories/directory.html",
        directory=directories_repository.directory(directory_id),
        contacts=contacts_repository.directory_contacts(directory_id),
    )


def create_directory():
    return flask.render_template("directories/create.html")


routes = [
    ("/directories", "directories", directories, ["GET"]),
    ("/directories/new", "create_directory", create_directory, ["GET"]),
    ("/directory/<directory_id>", "directory", directory, ["GET"]),
]
