from sqlalchemy import create_engine


class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "sqlite:///storage.db"
        self.__engine = None

    def connect_to_db(self):
        self.__engine = create_engine(url=self.__connection_string)

    def get_engine(self):
        if self.__engine is None:
            self.connect_to_db()
        return self.__engine


db_connection_handler = DBConnectionHandler()
