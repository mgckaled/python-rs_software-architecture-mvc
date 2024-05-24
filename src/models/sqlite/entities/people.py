from sqlalchemy import BIGINT, Column, ForeignKey, String

from src.models.sqlite.settings.base import Base


class PeopleTable(Base):
    __tablename__ = "people"
    id = Column(BIGINT, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(BIGINT, nullable=False)
    pet_id = Column(BIGINT, ForeignKey(
        "pets.id"), nullable=False)

    def __repr__(self) -> str:
        return f"People(id={self.id}, first_name={self.fisrt_name!r}, last_name={self.last_name!r}, age={self.age}, pet_id={self.pet_id})"
