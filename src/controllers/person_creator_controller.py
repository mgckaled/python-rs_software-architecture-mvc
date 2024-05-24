from src.models.sqlite.interfaces.people_repository_interface import \
    PeopleRepositoryInterface


class PersonCreatorController():
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository

    def create_person(self, first_name, last_name, age, pet_id) -> None:
        self.__people_repository.insert_person(
            first_name=first_name, last_name=last_name, age=age, pet_id=pet_id
        )
