from apistar import App
from apistar.commands import create_tables

from pharmap.storage.models import *     # noqa
from pharmap.routes import routes
from pharmap.settings import settings



app = App(routes=routes, settings=settings, commands=[create_tables])
