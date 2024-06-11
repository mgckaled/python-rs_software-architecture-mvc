from src.controllers.pet_deleter_controller import PetDeleterController
from src.models.sqlite.repositories.pets_repository import PetsRepository
from src.models.sqlite.settings.connection import db_connection_handler
from src.views.pet_deleter_view import PetDeleterView


def pet_deleter_composer() -> PetDeleterView:
    model = PetsRepository(db_connection=db_connection_handler)
    controller = PetDeleterController(pets_repository=model)
    view = PetDeleterView(controller=controller)

    return view
