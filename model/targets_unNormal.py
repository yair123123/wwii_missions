from sqlalchemy import Column, String, Integer, Float, NUMERIC
from config.base import Base

class TargetUnNormal:
    def __init__(self, target_country, target_city, target_type,
                 target_industry, target_priority,
                 target_longitude=None, target_latitude=None):
        self.target_country = target_country
        self.target_city = target_city
        self.target_type = target_type
        self.target_industry = target_industry
        self.target_priority = target_priority
        self.target_longitude = target_longitude
        self.target_latitude = target_latitude

    def __repr__(self):
        return (f"TargetUnNormal(target_country={self.target_country}, "
                f"target_city={self.target_city}, target_type={self.target_type}, "
                f"target_industry={self.target_industry}, target_priority={self.target_priority}, "
                f"target_longitude={self.target_longitude}, target_latitude={self.target_latitude})")

