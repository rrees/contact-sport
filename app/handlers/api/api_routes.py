from . import api_handlers

routes = [
    (
        "/api/contacts/find-by-name/<name>",
        "api-contacts-find",
        api_handlers.find_contacts_by_name,
        ["GET"],
    )
]
