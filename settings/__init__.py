import sys

try:
    from .local import settings # noqa
    print ("Using 'local' settings...")
except ImportError:
    from .common import settings # noqa
    print ("Using 'common' settings...")

