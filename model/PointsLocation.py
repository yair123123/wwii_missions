from sqlalchemy import Column, Integer,NUMERIC
from sqlalchemy.orm import relationship
from config.base import Base


class PointsLocation(Base):
    __tablename__ = "points_location"
    id_points = Column(Integer,primary_key=True,autoincrement=True)
    lat = Column(NUMERIC)
    lon = Column(NUMERIC)

    targets = relationship("Target",back_populates="points_location_relationship")