from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from config.base import Base


class Location(Base):
    __tablename__ = "locations"
    location_id = Column(Integer,primary_key=True,autoincrement=True)
    city = Column(Integer,ForeignKey("cities.id_city"))
    country = Column(Integer,ForeignKey("countries.id_country"))


    cities_location = relationship("City",back_populates="locations",lazy="joined")
    countries_location = relationship("Country",back_populates="locations",lazy="joined")


    targets = relationship("Target",back_populates="location_relationship")