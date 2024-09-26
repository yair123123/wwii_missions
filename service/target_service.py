from typing import Dict

from sqlalchemy import inspect
from typing_extensions import List

from model import Target


def create_target(customer_dict: Dict[str, str]) -> Target:
    try:
        return Target(
            target_id=customer_dict["target_id"],
            target_type=customer_dict["target_type"],
            location=customer_dict["location"],
            points_location=customer_dict["points_location"],
            priority=customer_dict["priority"],
        )
    except KeyError as e:
        print(f"Missing key: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise


def convert_to_target(customer_json: Dict[str, str]) -> Target:
    return create_target(customer_json)
def convert_to_json(target: Target) -> Dict[str, str]:
    if not target:
        return {"error": "Target not found"}

    location = target.location_relationship
    target_type = target.target_type_relationship
    points_location = target.points_location_relationship

    return {
        "target_id": target.target_id,
        "target_type": {
            "target_type": target_type.type_name if target_type else None,
            "industry_name": target_type.industries_relationship.industry_name if target_type and target_type.industries_relationship else None
        },
        "location": {
            "city": location.cities_location.city_name if location and location.cities_location else None,
            "country": location.countries_location.country_name if location and location.countries_location else None
        } if location else None,
        "points_location": {
            "lat": points_location.lat if points_location else None,
            "lon": points_location.lon if points_location else None
        } if points_location else None,
        "priority": target.priority
    }
def convert_list(list_target:List[Target]) -> List[Dict[str,str]]:
    return list(map(lambda x:convert_to_json(x),list_target))