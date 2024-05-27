from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.pets_repository_interface import \
    PetsRepositoryInterface


class PetListerController:
    def __init__(self, pets_repository: PetsRepositoryInterface) -> None:
        self.__pets_repository = pets_repository

    def list_pets(self) -> dict:
        pets = self.__get_pets_in_db()
        response = self.__format_response(pets=pets)
        return response

    def __get_pets_in_db(self) -> list[PetsTable]:
        pets = self.__pets_repository.list_pets()
        return pets

    def __format_response(self, pets: list[PetsTable]) -> dict:
        formatted_pets = []

        for pet in pets:
            formatted_pets.append(
                {"name": pet.name, "type": pet.type, "id": pet.id})

        return {"data": {"type": "Pets", "count": len(formatted_pets), "attributes": formatted_pets}}
