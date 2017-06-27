from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


_db = None


@property
def db():
    global _db
    if not _db:
        from apistar.main import get_current_app
        from apistar.backends import SQLAlchemy
        app = get_current_app()
        _db = SQLAlchemy.build(settings=app.settings)
    return _db


__all__ = [
    "Base",
    "db"
]
