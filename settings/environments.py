from apistar import environment, schema


class Env(environment.Environment):
    properties = {
        "PHARMAP_DEBUG": schema.Boolean(default=False),
        "PHARMAP_DATABASE_URL": schema.String(default="postgresql://:@localhost/pharmap")
    }

env = Env()
