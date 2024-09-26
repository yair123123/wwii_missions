from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from config.base import Base


class Target(Base):
    __tablename__ = "target"
    target_id = Column(Integer,primary_key=True,autoincrement=True)
    target_type = Column(Integer,ForeignKey("target_type.type_id"),nullable=True)
    location = Column(Integer,ForeignKey("locations.location_id"),nullable=True)
    points_location = Column(Integer,ForeignKey("points_location.id_points"),nullable=True)
    priority = Column(String(1000),nullable=True)

    target_type_relationship = relationship("TargetType", back_populates="targets" ,lazy="joined")
    location_relationship = relationship("Location", back_populates="targets",lazy="joined")
    points_location_relationship = relationship("PointsLocation", back_populates="targets",lazy="joined")