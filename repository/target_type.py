from config.base import session_factory
from model import TargetType

def get_id(type_name: str, industry: int) -> int:
    with session_factory() as session:
        targetType = session.query(TargetType).filter(
            TargetType.type_name == type_name,
            TargetType.industry == industry
        ).first()
        return targetType.type_id if targetType else None


def insert_target_type(target_type:TargetType) -> int:
    target_type_id = get_id(target_type.type_name,target_type.industry)
    if target_type_id is None and target_type.type_name is not None:
        with session_factory() as session:
            session.add(target_type)
            session.commit()
            session.refresh(target_type)
            return target_type.type_id
    return target_type_id