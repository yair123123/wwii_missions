from returns.maybe import Maybe

from config.base import session_factory
from model import Target

def get_id(target:Target) -> int:
    with session_factory() as session:
        target_from_table = session.query(Target).filter(
            Target.target_type == target.target_type,
            Target.location == target.location,
            Target.points_location == target.points_location,
            Target.priority == target.priority
        ).first()
        return target_from_table.target_id if target_from_table else None
def get_target_by_id(id:int):
    with session_factory() as session:
        return Maybe.from_optional(session.get(Target,id))
def get_all_targets():
    with session_factory() as session:
        return Maybe.from_optional(session.query(Target).all())
def insert_target(target:Target) -> int:
    if get_id(target) is None:
        with session_factory() as session:
            session.add(target)
            session.commit()
            session.refresh(target)
            return target.target_id
