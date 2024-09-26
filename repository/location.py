from config.base import session_factory
from model import Industry, Location

def get_id(city: str, country: str) -> int:
    with session_factory() as session:
        location = session.query(Location).filter(
            Location.city == city,
            Location.country == country
        ).first()
        return location.location_id if location else None

def insert_location(location:Location) -> int:
    loc_id = get_id(location.city,location.country)
    if loc_id is None:
        with session_factory() as session:
            session.add(location)
            session.commit()
            session.refresh(location)
            return location.location_id
    return loc_id