from config.base import session_factory
from model import City

def get_id_by_name(name:str) -> int:
    with session_factory() as session:
        city =  session.query(City).filter(City.city_name == name).first()
        return city.id_city if city else None
def insert_city(city:City) -> int:
    city_id = get_id_by_name(city.city_name)
    if city_id is None:
        with session_factory() as session:
            session.add(city)
            session.commit()
            session.refresh(city)
            return city.id_city
    return city_id