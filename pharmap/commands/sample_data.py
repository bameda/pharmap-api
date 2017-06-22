import click
from faker import Faker

from pharmap.storage import repository

TOTAL_ENTRIES = 40

fake = Faker()


def _create_entity(db_session):
    repository.create_entity(
        db_session=db_session,
        name="{} {}".format(fake.company(), fake.company_suffix()),
        description=fake.sentence(),
        longitude=fake.longitude(),
        latitude=fake.latitude()
    )


def sample_data():
    """Populate the database with some sample data."""
    from apistar.main import get_current_app
    from apistar.backends import SQLAlchemy

    app = get_current_app()
    db_session = SQLAlchemy.build(settings=app.settings).session_class()

    for n in range(TOTAL_ENTRIES):
        _create_entity(db_session)

    db_session.commit()
    click.echo("Generated sample data.")


__all__ = [
    "sample_data",
]
