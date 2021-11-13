import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

env = os.environ

engine = create_engine(
    f"postgresql://{env['DATABASE_USER']}:{env['DATABASE_PASS']}@{env['DATABASE_HOST']}:5432/{env['DATABASE_NAME']}"
)

connection = engine.connect()
session = Session(bind=connection)


def init_session():

    from model import Base

    Base.metadata.create_all(bind=engine)
