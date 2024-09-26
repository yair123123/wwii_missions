from config.base import engine, Base

def create_tables():
    Base.metadata.create_all(engine)
def drop_table():
    Base.metadata.drop_all(engine)