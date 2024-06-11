from flask import Blueprint, jsonify

from src.errors.error_handler import handle_errors
from src.main.composer.pet_deleter_composer import pet_deleter_composer
from src.main.composer.pet_lister_composer import pet_lister_composer
from src.views.http_types.http_request import HttpRequest

pet_route_db = Blueprint(name="pet_routes", import_name=__name__)


@pet_route_db.route(rule="/pets", methods=["GET"])
def list_pets() -> dict:
    try:
        http_request = HttpRequest()
        view = pet_lister_composer()
        http_response = view.handle_request(http_request=http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(error=exception)

        return jsonify(http_response.body), http_response.status_code


@pet_route_db.route(rule="/pets/<name>", methods=["DELETE"])
def delete_pet(name: str) -> dict:
    try:
        http_request = HttpRequest(param={"name": name})
        view = pet_deleter_composer()
        http_response = view.handle_request(http_request=http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(error=exception)

        return jsonify(http_response.body), http_response.status_code
