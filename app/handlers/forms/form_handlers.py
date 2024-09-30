import flask

from app.repositories import addresses as address_repository

from .form_models import AddressForm


def address():
    form = AddressForm(flask.request.form)

    if form.validate():
        contact_id = form.contact_id.data

        [id, external_id] = address_repository.create(
            contact_id, form.label.data, form.address.data
        )

        return flask.redirect(flask.url_for("contact", contact_id=contact_id))

    return flask.abort(400)
