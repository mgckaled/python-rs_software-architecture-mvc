
from typing import Self
from unittest import mock

from mock_alchemy.mocking import UnifiedAlchemyMagicMock

from src.models.sqlite.entities.pets import PetsTable

from .pets_repository import PetsRepository


class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PetsTable)],

                    [
                        PetsTable(name="dog", type="dog"),
                        PetsTable(name="cat", type="cat")
                    ]

                )
            ]
        )

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        pass


def test_list_pets() -> None:
    mock_connection = MockConnection()
    repo = PetsRepository(db_connection=mock_connection)
    response = repo.list_pets()

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    assert response[0].name == "dog"


def test_delete_pet() -> None:
    mock_connection = MockConnection()
    repo = PetsRepository(db_connection=mock_connection)
    repo.delete_pets(name="petName")

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.filter.assert_called_once_with(
        PetsTable.name == "petName")
    mock_connection.session.delete.assert_called_once()
