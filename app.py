from apistar import App
from apistar.commands import create_tables

from pharmap.routes import routes
from settings import settings

from pharmap.storage.models import *     # noop


app = App(routes=routes, settings=settings, commands=[create_tables])
