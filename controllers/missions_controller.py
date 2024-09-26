from flask import blueprints, jsonify

from repository.target import get_target_by_id, get_all_targets
from service.target_service import convert_to_json, convert_list

missions_blueprint = blueprints.Blueprint("mission",__name__)

@missions_blueprint.route("/<int:id>",methods=["GET"])
def get_target(id:int):
    return (
        get_target_by_id(id)
        .map(convert_to_json)
        .map(lambda u: (jsonify(u), 200))
        .value_or((jsonify({}), 404))
    )

@missions_blueprint.route("/",methods=["GET"])
def get_targets():
    return (
        get_all_targets()
        .map(convert_list)
        .map(lambda u: (jsonify(u), 200))
        .value_or((jsonify({}), 404))
    )


