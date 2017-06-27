from typing import List

from sqlalchemy.orm.session import Session

from pharmap.storage.models import Entity


def list_entities(db_session: Session) -> List[Entity]:
    return db_session.query(Entity).all()


def get_entity(db_session: Session, id: str) -> Entity:
    return db_session.query(Entity).filter_by(id=id).one_or_none()


def create_entity(db_session: Session, name: str, description: str,
                  longitude: float, latitude: float, is_active: bool=True) -> Entity:

    entity = Entity(
        name=name,
        description=description,
        is_active=is_active,
        longitude=longitude,
        latitude=latitude
    )
    db_session.add(entity)
    return entity


def update_entity(db_session: Session, id: str, name: str, description: str,
                  longitude: float, latitude: float, is_active: bool=True) -> Entity:
    pass


def delete_entity(db_session: Session, id: str) -> bool:
    entry = get_entity(db_session, id)
    if not entry:
        return False


__all__ = [
    "list_entities",
    "get_entity",
    "create_entity",
    "update_entity",
    "delete_entity"
]
