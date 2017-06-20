from apistar import schema

from pharmap.schemas import common as common_schema


class EntityIn(schema.Object):
    properties = {
        "name": schema.String,
        "description": schema.String,
        "lon": common_schema.Longitude,
        "lat": common_schema.Latitude,
    }


class EntityOut(schema.Object):
    properties = {
        "name": schema.String,
        "description": schema.String,
        "is_active": schema.Boolean,
        "longitude": common_schema.Longitude,
        "latitude": common_schema.Latitude,
        "created_datetime": common_schema.DateTime,
        "updated_datetime": common_schema.DateTime
    }


__all__ = [
    "EntityIn",
    "EntityOut"
]
