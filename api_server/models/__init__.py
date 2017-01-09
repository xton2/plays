from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import configure_mappers

from HenryIV import HenryIV
from Plays import Plays

def session_factory(settings):
    engine = engine_from_config(settings, 'db.')
    factory = sessionmaker()
    factory.configure(bind=engine)

    dbsession = factory()
    return dbsession

def includeme(config):
    config.add_request_method(
        lambda req: session_factory(config.get_settings()),
        'dbsession',
        reify=True
    )
