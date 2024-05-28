from src.controllers.interfaces.pet_lister_controller_interface import \
    PetListerControllerInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface


class PetListerView(ViewInterface):
    def __init__(self, controller: PetListerControllerInterface) -> None:
        self.__controller = controller

    def handle_request(self, http_request: HttpRequest) -> HttpResponse:
        body_response = self.__controller.list_pets()

        return HttpResponse(status_code=200, body=body_response)
