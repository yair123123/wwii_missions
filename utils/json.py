from datetime import datetime
from typing import List, Dict

import toolz as t

@t.curry
def has_all_keys(keys: List[str], d: Dict[str, str]) -> bool:
    return all(k in d for k in keys)
def get_datetime(datetime_str:str) -> datetime:
    year, month, day, hour, minute, second = map(int, datetime_str.split(','))
    return datetime(year, month, day, hour, minute, second)