
from typing import NoReturn, Self
from unittest import mock

import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound

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


class MockConnectionNoResult:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs) -> NoReturn:
        raise NoResultFound("No Result Found")

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


def test_list_pets_no_result() -> None:
    mock_connection = MockConnectionNoResult()
    repo = PetsRepository(db_connection=mock_connection)
    response = repo.list_pets()

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.all.assert_not_called()
    mock_connection.session.filter.assert_not_called()

    assert response == []


def test_delete_pet_error() -> None:
    mock_connection = MockConnectionNoResult()
    repo = PetsRepository(db_connection=mock_connection)

    with pytest.raises(expected_exception=Exception):
        repo.delete_pets(name="petName")

    mock_connection.session.rollback.assert_called_once()
