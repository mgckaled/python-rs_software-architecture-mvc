from flask import Blueprint, jsonify

pet_route_db = Blueprint(name="pet_routes", import_name=__name__)


@pet_route_db.route(rule="/pets", methods=["GET"])
def list_pets() -> dict:
    return jsonify({"dada": "pets"}), 200
