import pytest

from .person_creator_controller import PersonCreatorController


class MockPeopleRepository:

    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        pass


def test_create_person() -> None:

    person_info = {
        "first_name": "firstname",
        "last_name": "lastname",
        "age": 30,
        "pet_id": 123
    }

    controller = PersonCreatorController(
        people_repository=MockPeopleRepository())
    response = controller.create_person(person_info=person_info)

    assert response == {"data": {"type": "Person",
                                 "count": 1, "attributes": person_info}}


def test_create_person_error() -> None:

    person_info = {
        "first_name": "firstname123",
        "last_name": "lastname",
        "age": 30,
        "pet_id": 123
    }

    controller = PersonCreatorController(
        people_repository=MockPeopleRepository())
    with pytest.raises(expected_exception=Exception):
        controller.create_person(person_info=person_info)
