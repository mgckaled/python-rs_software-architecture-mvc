import re

from src.controllers.interfaces.person_creator_controller_interface import \
    PersonCreatorControllerInterface
from src.models.sqlite.interfaces.people_repository_interface import \
    PeopleRepositoryInterface


class PersonCreatorController(PersonCreatorControllerInterface):
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository

    def create_person(self, person_info: dict) -> dict:
        first_name = person_info["first_name"]
        last_name = person_info["last_name"]
        age = person_info["age"]
        pet_id = person_info["pet_id"]

        self.__validade_first_and_last_name(
            first_name=first_name, last_name=last_name)
        self.__insert_person_into_db(
            first_name=first_name, last_name=last_name, age=age, pet_id=pet_id)
        formated_resposnse = self.__format_response(person_info=person_info)

        return formated_resposnse

    def __validade_first_and_last_name(self, first_name: str, last_name: str) -> None:
        non_valid_characters = re.compile(pattern=r'[^a-zA-Z]')

        if non_valid_characters.search(string=first_name) or non_valid_characters.search(string=last_name):
            raise Exception(
                "Nome da pessoa inválido. O nome deve conter apenas letras.")

    def __insert_person_into_db(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        self.__people_repository.insert_person(
            first_name=first_name, last_name=last_name, age=age, pet_id=pet_id)

    def __format_response(self, person_info: dict) -> dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": person_info
            }
        }
