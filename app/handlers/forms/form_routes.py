from . import form_handlers

routes = [
    ("/forms/address/add", "address_add_form", form_handlers.address, ["POST"]),
    ("/forms/contact/add", "contact_add_form", form_handlers.contact, ["POST"]),
    ("/forms/email/add", "email_add_form", form_handlers.email, ["POST"]),
    ("/forms/directory/add", "directory_add_form", form_handlers.directory, ["POST"]),
    (
        "/forms/directory/<directory_id>/contact/add/<contact_id>",
        "directory_add_contact_form",
        form_handlers.add_contact_to_directory,
        ["POST"],
    ),
]
