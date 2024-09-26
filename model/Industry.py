from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.base import Base


class Industry(Base):
    __tablename__ = "industries"
    industry_id = Column(Integer,primary_key=True,autoincrement=True)
    industry_name = Column(String(1000),nullable=False)

    target_type = relationship("TargetType",back_populates="industries_relationship")