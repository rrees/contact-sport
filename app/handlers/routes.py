from .forms import form_handlers

routes = [
    ("/forms/address", "address_form", form_handlers.address, ["POST"]),
]
