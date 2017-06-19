import arrow
import uuid

from geoalchemy2 import Geometry
from sqlalchemy import Boolean, Column, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID

from pharmap.storage import database


class Entity(database.Base):
    __tablename__ = "Entities"

    id = Column(UUID(as_uuid=True), nullable=False, primary_key=True, default=uuid.uuid4)

    name = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)

    point = Column(Geometry("POINT"), nullable=False)

    created_datetime = Column(DateTime(timezone=True), nullable=False,
                              default=arrow.utcnow)
    updated_datetime = Column(DateTime(timezone=True), nullable=False,
                              default=arrow.utcnow, onupdate=arrow.utcnow)


__all__ = [
    "Entity"
]
