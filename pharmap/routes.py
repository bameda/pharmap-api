from apistar import Include, Route
from apistar.docs import docs_routes
from apistar.statics import static_routes

from pharmap import views
from pharmap.views import entities


routes = [
    Route('/', 'GET', views.welcome),

    Route('/entities', 'GET', entities.list_entities),
    Route('/entities', 'POST', entities.create_entity),
    Route('/entities/{id}', 'GET', entities.get_entity),
    Route('/entities/{id}', 'PUT', entities.update_entity),
    Route('/entities/{id}', 'DELETE', entities.delete_entity),

    Include('/docs', docs_routes),
    Include('/static', static_routes)
]
