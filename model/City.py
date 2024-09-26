from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.base import Base


class City(Base):
    __tablename__ = "cities"
    id_city = Column(Integer,primary_key=True,autoincrement=True)
    city_name = Column(String(1000),nullable=True)

    locations = relationship("Location",back_populates="cities_location")