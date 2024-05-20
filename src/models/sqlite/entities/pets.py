from sqlalchemy import BIGINT, Column, String

from src.models.sqlite.settings.base import Base


class PetsTable(Base):
    __tablename__ = "pets"
    id = Column(BIGINT, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f"Pets(id={self.id}, name={self.name!r}, type={self.type!r})"
