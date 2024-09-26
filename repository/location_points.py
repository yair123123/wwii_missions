from sqlalchemy import Numeric

from config.base import session_factory
from model import PointsLocation
def get_id(lat: Numeric, lon: Numeric) -> int:
    with session_factory() as session:
        pointsLocation = session.query(PointsLocation).filter(
            PointsLocation.lat == lat,
            PointsLocation.lon == lon
        ).first()
        return pointsLocation.id_points if pointsLocation else None

def insert_points_location(points_location:PointsLocation) -> int:
    l_id = get_id(points_location.lat,points_location.lon)
    if l_id is None:
        with session_factory() as session:
            session.add(points_location)
            session.commit()
            session.refresh(points_location)
            return points_location.id_points
    return l_id