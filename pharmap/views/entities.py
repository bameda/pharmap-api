from typing import List

from apistar import exceptions as exc
from apistar.backends import SQLAlchemy

from pharmap.storage import repository
from pharmap.schemas import EntityIn, EntityOut


def list_entities(db: SQLAlchemy) -> List[EntityOut]:
    """List all entitiess."""
    db_session = db.session_class()
    return [EntityOut(entity) for entity in repository.list_entities(db_session)]


def get_entity(db: SQLAlchemy, id: str) -> EntityOut:
    """Get and entity by id."""
    db_session = db.session_class()

    entry = repository.get_entity(db_session, id)
    if not entry:
        raise exc.NotFound()
    return EntityOut(entry)


def create_entity(db: SQLAlchemy, entity_data: EntityIn) -> EntityOut:
    """Create a new entity."""
    db_session = db.session_class()
    entity = repository.create_entity(db_session,
                                      name=entity_data.name,
                                      description=entity_data.description,
                                      longitud=entity_data.longitude,
                                      latitude=entity_data.latitude)
    return EntityOut(entity)


def update_entity(db: SQLAlchemy, id: str, entity_data: EntityIn) -> EntityOut:
    """Update the information of an existing entity."""
    db_session = db.session_class()
    entity = repository.update_entity(db_session, id,
                                      name=entity_data.name,
                                      description=entity_data.description,
                                      longitude=entity_data.longitude,
                                      latitude=entity_data.latitude)
    return EntityOut(entity)


def delete_entity(db: SQLAlchemy, id: str):
    """Delete an entity according its id."""
    db_session = db.session_class()
    return repository.delete_entity(db_session, id)
