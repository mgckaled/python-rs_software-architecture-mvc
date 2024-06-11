from flask import Blueprint, jsonify, request

from src.errors.error_handler import handle_errors
from src.main.composer.person_creator_composer import person_creator_composer
from src.main.composer.person_finder_composer import person_finder_composer
from src.views.http_types.http_request import HttpRequest

person_route_db = Blueprint(name="person_routes", import_name=__name__)


@person_route_db.route(rule="/people", methods=["POST"])
def create_person() -> dict:
    try:
        http_request = HttpRequest(body=request.json)
        view = person_creator_composer()
        http_response = view.handle_request(http_request=http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(error=exception)

        return jsonify(http_response.body), http_response.status_code


@person_route_db.route(rule="/people/<person_id>", methods=["GET"])
def find_person_by_id(person_id: int) -> dict:
    try:
        http_request = HttpRequest(param={"person_id": person_id})
        view = person_finder_composer()
        http_response = view.handle_request(http_request=http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(error=exception)

        return jsonify(http_response.body), http_response.status_code
