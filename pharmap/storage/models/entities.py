import arrow
import uuid

from sqlalchemy import Boolean, Column, DateTime, Float, Text
from sqlalchemy.dialects.postgresql import UUID

from pharmap.storage import database


now = lambda: arrow.utcnow().datetime   # noqa


class Entity(database.Base):
    __tablename__ = "Entities"

    id = Column(UUID(as_uuid=True), nullable=False, primary_key=True, default=uuid.uuid4)

    name = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)

    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)

    created_datetime = Column(DateTime(timezone=True), nullable=False,
                              default=now)
    updated_datetime = Column(DateTime(timezone=True), nullable=False,
                              default=now, onupdate=now)


__all__ = [
    "Entity"
]
