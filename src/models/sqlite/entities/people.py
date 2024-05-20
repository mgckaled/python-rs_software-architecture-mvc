from sqlalchemy import BIGINT, Column, ForeignKey, String

from src.models.sqlite.settings.base import Base


class PeopleTable(Base):
    __tablename__ = "people"
    id = Column(name_pos=BIGINT, primary_key=True)
    fisrt_name = Column(name_pos=String, nullable=False)
    last_name = Column(name_pos=String, nullable=False)
    age = Column(name_pos=BIGINT, nullable=False)
    pet_id = Column(name_pos=BIGINT, type_pos=ForeignKey(
        "pets.id"), nullable=False)

    def __repr__(self) -> str:
        return f"People(id={self.id}, fisrt_name={self.fisrt_name!r}, last_name={self.last_name!r}, age={self.age}, pet_id={self.pet_id})"
