import flask

from app.repositories import addresses as address_repository

from .form_models import AddressForm


def address():
    form = AddressForm(flask.request.form)

    if form.validate():
        [id, external_id] = address_repository.create(
            form.contact_id.data, form.label.data, form.address.data
        )
        return flask.redirect(flask.url_for("home"))

    return flask.abort(400)
