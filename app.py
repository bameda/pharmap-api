from apistar import App
from apistar.commands import create_tables

from pharmap.commands import sample_data
from pharmap.storage.models import * # noqa
from pharmap.routes import routes
from pharmap.settings import settings


commands = [
    create_tables,
    sample_data,
]


app = App(routes=routes, settings=settings, commands=commands)
