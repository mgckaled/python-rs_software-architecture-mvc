from flask import Blueprint, jsonify, request

from src.main.composer.person_creator_composer import person_creater_composer
from src.views.http_types.http_request import HttpRequest

person_route_db = Blueprint(name="person_routes", import_name=__name__)


@person_route_db.route(rule="/people", methods=["POST"])
def create_person() -> dict:
    http_request = HttpRequest(body=request.json)
    view = person_creater_composer()
    http_response = view.handle_request(http_request=http_request)

    return jsonify(http_response.body), http_response.status_code
