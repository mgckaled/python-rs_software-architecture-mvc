from abc import ABC, abstractmethod

from src.models.sqlite.entities.pets import PetsTable


class PetsRepositoryInterface(ABC):

    @abstractmethod
    def list_pets(self) -> list[PetsTable]:
        raise NotImplementedError

    @abstractmethod
    def delete_pets(self, name: str) -> None:
        raise NotImplementedError
