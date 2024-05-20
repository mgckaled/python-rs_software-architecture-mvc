from typing import Self

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "sqlite:///storage.db"
        self.__engine = None
        self.session = None

    def connect_to_db(self) -> None:
        self.__engine = create_engine(url=self.__connection_string)

    def get_engine(self) -> None | Engine:
        if self.__engine is None:
            self.connect_to_db()
        return self.__engine

    def __enter__(self) -> Self:
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.session.close()


db_connection_handler = DBConnectionHandler()
