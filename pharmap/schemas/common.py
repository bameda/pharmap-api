from arrow import Arrow
from apistar import schema
from apistar.exceptions import SchemaError
import dateparser
from datetime import datetime


class DateTime(datetime):
    native_type = datetime
    errors = {
        'type': 'Must be a valid datetime.'
    }

    def __new__(cls, *args, **kwargs):
        if kwargs:
            assert not args
            return type(cls.__name__, (cls,), kwargs)

        assert len(args) == 1
        value = args[0]

        if isinstance(value, datetime):
            return value
        elif isinstance(value, str):
            try:
                return dateparser.parse(value, settings={'TIMEZONE': 'UTC'})
            except KeyError:
                raise SchemaError(schema.error_message(cls, 'type'))
        elif isinstance(value, Arrow):
            return value.datetime

        raise SchemaError(schema.error_message(cls, 'type'))

    # The following is currently required in order to keep mypy happy
    # with our atypical usage of `__new__`...
    # See: https://github.com/python/mypy/issues/3307

    def __init__(self, *args, **kwargs):
        super().__init__()


class Latitude(schema.Number):
    minimum = -90
    maximum = 90


class Longitude(schema.Number):
    minimum = -180
    maximum = 180


__all__ = [
    "DateTime",
    "Latitude",
    "Longitude"
]
