from .forms import form_handlers
from .pages import routes as page_routes

routes = [
    ("/forms/address/add", "address_add_form", form_handlers.address, ["POST"]),
    ("/forms/contact/add", "contact_add_form", form_handlers.contact, ["POST"]),
    ("/forms/email/add", "email_add_form", form_handlers.email, ["POST"]),
] + page_routes
