from apistar.backends import SQLAlchemy
from pharmap.storage import repository
from pharmap import schemas


def list_entities(db: SQLAlchemy):
    db_session = db.session_class()
    return [schemas.EntityOut(e) for e in repository.list_entities(db_session)]


def get_entity(db: SQLAlchemy, id: str):
    db_session = db.session_class()
    return "TODO"


def create_entity(db: SQLAlchemy, entity: schemas.EntityIn):
    db_session = db.session_class()
    return "TODO"


def update_entity(db: SQLAlchemy, id: str):
    db_session = db.session_class()
    return "TODO"


def delete_entity(db: SQLAlchemy, id: str):
    db_session = db.session_class()
    return "TODO"
