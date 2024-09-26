from config.base import session_factory
from model import Country


def get_id_by_name(name:str) -> int:
    with session_factory() as session:
        country =  session.query(Country).filter(Country.country_name == name).first()
        return country.id_country if country else None
def insert_country(country:Country) -> int:
    country_id = get_id_by_name(country.country_name)
    if country_id is None:
        with session_factory() as session:

            session.add(country)
            session.commit()
            session.refresh(country)
            return country.id_country
    return country_id