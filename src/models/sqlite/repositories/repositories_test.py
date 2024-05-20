import pytest

from src.models.sqlite.repositories.pets_repository import PetsRepository
from src.models.sqlite.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="interation with database")
def test_list_pets() -> None:
    repo = PetsRepository(db_connection=db_connection_handler)
    response = repo.list_pets()
    print(response)
