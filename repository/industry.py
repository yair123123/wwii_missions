from config.base import session_factory
from model import Industry
def get_id_by_name(name:str) -> int:
    with (session_factory() as session):
        industry = session.query(Industry).filter(Industry.industry_name == name).first()
        return industry.industry_id if industry else None

def insert_industry(industry:Industry) -> int:
    ind_id = get_id_by_name(industry.industry_name)
    if ind_id is None and industry.industry_name is not None:
        with session_factory() as session:
            session.add(industry)
            session.commit()
            session.refresh(industry)
            return industry.industry_id
    return ind_id