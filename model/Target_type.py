
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.base import Base


class TargetType(Base):
    __tablename__ = "target_type"
    type_id = Column(Integer,primary_key=True)
    type_name = Column(String(1000),nullable=False)
    industry = Column(Integer,ForeignKey("industries.industry_id"))

    industries_relationship = relationship("Industry",back_populates="target_type",lazy="joined")

    targets = relationship("Target",back_populates="target_type_relationship")