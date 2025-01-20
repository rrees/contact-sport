import wtforms

from wtforms import validators


class AddressForm(wtforms.form.Form):
    contact_id = wtforms.StringField("contact_id", [validators.InputRequired()])
    label = wtforms.StringField("label", [validators.InputRequired()])
    address = wtforms.TextAreaField("address", [validators.InputRequired()])


class ContactForm(wtforms.form.Form):
    name = wtforms.StringField("name", [validators.InputRequired()])


class EmailForm(wtforms.form.Form):
    contact_id = wtforms.StringField("contact_id", [validators.InputRequired()])
    label = wtforms.StringField("label", [validators.InputRequired()])
    email = wtforms.TextAreaField("email", [validators.InputRequired()])


class DirectoryForm(wtforms.form.Form):
    name = wtforms.StringField(
        "name", [validators.InputRequired(), validators.Length(max=200)]
    )
