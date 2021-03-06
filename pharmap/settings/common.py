from pharmap.settings.environments import env
from pharmap.storage import database

settings = {
    "DEBUG": env.get("PHARMAP_DEBUG", False),

    "DATABASE": {
        "URL": env.get("PHARMAP_DATABASE_URL", "postgresql://:@localhost/pharmap"),
        "POOL_SIZE": env.get("PHARMAP_DATABASE_POOL_SIZE", 10),
        "METADATA": database.Base.metadata
    },
}
