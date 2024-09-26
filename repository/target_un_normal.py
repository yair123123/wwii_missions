from typing import List

from sqlalchemy import text

from config.base import session_factory
from model.targets_unNormal import TargetUnNormal


def get_targets() -> List[TargetUnNormal]:
    with session_factory() as session:
        results = session.execute(text("SELECT target_country,target_city,target_type,target_industry,target_priority,target_longitude,target_latitude FROM mission")).fetchall()
        return  [TargetUnNormal(*result) for result in results]
