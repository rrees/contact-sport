from .forms import form_handlers

routes = [
    ("/forms/address/add", "address_add_form", form_handlers.address, ["POST"]),
    ("/forms/contact/add", "contact_add_form", form_handlers.contact, ["POST"]),
    ("/forms/email/add", "email_add_form", form_handlers.email, ["POST"]),
]
