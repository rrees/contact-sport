from .api.api_routes import routes as api_routes
from .forms.form_routes import routes as form_routes
from .pages import routes as page_routes

routes = api_routes + form_routes + page_routes
