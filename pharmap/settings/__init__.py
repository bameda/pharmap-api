try:
    from pharmap.settings.local import settings # noqa
    print(" * Using 'local' settings...")
except ImportError:
    from pharmap.settings.common import settings # noqa
    print(" * Using 'common' settings...")
