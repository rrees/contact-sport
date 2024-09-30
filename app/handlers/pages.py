import flask

from app.models import Contact
from app.repositories import contacts as contacts_repository


def front_page():
    return flask.render_template("index.html")


def home_page():
    return flask.render_template("home.html")


def contacts():
    return flask.render_template("contacts.html", contacts=contacts_repository.all())


def contact(contact_id):
    a_contact = contacts_repository.full(contact_id)
    print(a_contact)
    contact_details = Contact.from_dict(a_contact)

    return flask.render_template("contact.html", contact=contact_details)
