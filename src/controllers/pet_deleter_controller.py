from src.controllers.interfaces.pet_deleter_controller_interface import \
    PetDeleterControllerInterface
from src.models.sqlite.interfaces.pets_repository_interface import \
    PetsRepositoryInterface


class PetDeleterController(PetDeleterControllerInterface):
    def __init__(self, pets_repository: PetsRepositoryInterface) -> None:
        self.__pets_repository = pets_repository

    def delete_pet(self, name: str) -> None:
        self.__pets_repository.delete_pets(name=name)
