import flask

from app.repositories import addresses as address_repository
from app.repositories import contacts as contact_repository
from app.repositories import directories as directory_repository
from app.repositories import emails as email_repository

from .form_models import AddressForm, ContactForm, DirectoryForm, EmailForm


def address():
    form = AddressForm(flask.request.form)

    if form.validate():
        contact_id = form.contact_id.data

        [id, external_id] = address_repository.create(
            contact_id, form.label.data, form.address.data
        )

        return flask.redirect(flask.url_for("contact", contact_id=contact_id))

    return flask.abort(400)


def email():
    form = EmailForm(flask.request.form)

    if form.validate():
        contact_id = form.contact_id.data

        [id, external_id] = email_repository.create(
            contact_id, form.label.data, form.email.data
        )

        return flask.redirect(flask.url_for("contact", contact_id=contact_id))

    return flask.abort(400)


def contact():
    form = ContactForm(flask.request.form)

    if form.validate():
        [id, external_id] = contact_repository.create(form.name.data)

        return flask.redirect(flask.url_for("contact", contact_id=external_id))

    return flask.abort(400)


def directory():
    form = DirectoryForm(flask.request.form)

    if form.validate():
        [id, external_id] = directory_repository.create(form.name.data)

        return flask.redirect(flask.url_for("directory", directory_id=external_id))

    return flask.abort(400, "Form is invalid")


def add_contact_to_directory(directory_id, contact_id):
    return flask.redirect(flask.url_for("directory", directory_id=directory_id))
