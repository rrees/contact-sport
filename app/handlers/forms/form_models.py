import wtforms

from wtforms import validators


class AddressForm(wtforms.form.Form):
    contact_id = wtforms.StringField("contact_id", [validators.InputRequired()])
    label = wtforms.StringField("label", [validators.InputRequired()])
    address = wtforms.TextAreaField("address", [validators.InputRequired()])
