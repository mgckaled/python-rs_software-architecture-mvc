
from abc import ABC, abstractmethod


@abstractmethod
class PersonCreatorControllerInterface(ABC):
    def create_person(self, person_info: dict) -> dict:
        pass
