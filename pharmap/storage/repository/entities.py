from typing import List

from geoalchemy2.elements import WKTElement
from sqlalchemy.orm.session import Session

from pharmap.storage.models import Entity


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


def list_entities(db_session: Session) -> List[Entity]:
    return db_session.query(Entity).all()


__all__ = [
    "create_entity",
    "list_entities"
]
