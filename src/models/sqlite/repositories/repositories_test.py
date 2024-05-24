import pytest

from src.models.sqlite.repositories.people_repository import PeopleRepository
from src.models.sqlite.repositories.pets_repository import PetsRepository
from src.models.sqlite.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="interation with database")
def test_list_pets() -> None:
    repo = PetsRepository(db_connection=db_connection_handler)
    response = repo.list_pets()
    print(response)


@pytest.mark.skip(reason="interation with database")
def test_delete_pets() -> None:
    name = "belinha"
    repo = PetsRepository(db_connection=db_connection_handler)
    repo.delete_pets(name=name)


@pytest.mark.skip(reason="interation with database")
def test_insert_person() -> None:
    first_name = "test first name"
    last_name = "test last name"
    age = 77
    pet_id = 2

    repo = PeopleRepository(db_connection=db_connection_handler)
    repo.insert_person(first_name=first_name,
                       last_name=last_name, age=age, pet_id=pet_id)


@pytest.mark.skip(reason="interation with database")
def test_get_person() -> None:
    person_id = 1

    repo = PeopleRepository(db_connection=db_connection_handler)
    response = repo.get_person(person_id=person_id)
    print(f'\n{response}\n{response.pet_name}')
