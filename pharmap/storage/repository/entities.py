from apistar.backends import SQLAlchemy

from pharmap.storage import Entity


def create_entity(db: SQLAlchemy, name: str, description: str,
                  lon: float, lat: float, is_active: bool=True):
    entity = Entity(
        name=name,
        description=description,
        is_active=is_active,
        point="POINT({} {})".format(lon, lat)
    )
    db.add(entity)
    return entity
