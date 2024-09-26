from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from config.base import Base


class Country(Base):
    __tablename__ = "countries"
    id_country = Column(Integer,primary_key=True,autoincrement=True)
    country_name = Column(String(1000))

    locations = relationship("Location",back_populates="countries_location")