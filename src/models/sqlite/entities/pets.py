from sqlalchemy import BIGINT, Column, String

from src.models.sqlite.settings.base import Base


class PetsTable(Base):
    __tablename__ = "pets"
    id = Column(__name_pos=BIGINT, primary_key=True)
    name = Column(__name_pos=String, nullable=False)
    type = Column(__name_pos=String, nullable=False)

    def __repr__(self) -> str:
        return f"Pets(id={self.id}, name={self.name!r}, type={self.type!r})"
