from typing import List

from model import City, Country, Industry, TargetType, PointsLocation, Target, Location
from model.targets_unNormal import TargetUnNormal
from repository.city import insert_city
from repository.country import insert_country
from repository.industry import insert_industry
from repository.location import insert_location
from repository.location_points import insert_points_location
from repository.target import insert_target
from repository.target_type import insert_target_type


def load_target_and_push_normal(target_un_normal:TargetUnNormal) -> int:
    city_id = insert_city(City(city_name = target_un_normal.target_city))
    country_id = insert_country(Country(country_name = target_un_normal.target_country))
    location_id =  insert_location(Location(city=city_id,country = country_id))
    industry_id = insert_industry(Industry(industry_name=target_un_normal.target_industry))
    target_type_id = insert_target_type(TargetType(type_name=target_un_normal.target_type,industry=industry_id))
    location_points_id = insert_points_location(PointsLocation(lat=target_un_normal.target_latitude ,lon= target_un_normal.target_longitude))
    target_id = insert_target(Target(target_type= target_type_id,
                                     location = location_id,
                                     points_location = location_points_id,
                                     priority = target_un_normal.target_priority
                                     ))
    return target_id


def load_targets(targets_unnormal: List[TargetUnNormal]):
    for target in targets_unnormal:
        load_target_and_push_normal(target)
