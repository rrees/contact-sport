from wtforms import Form, validators
from wtforms import fields


class Login(Form):
    username = fields.StringField("Username", [validators.required()])
    password = fields.PasswordField("Password", [validators.required()])
