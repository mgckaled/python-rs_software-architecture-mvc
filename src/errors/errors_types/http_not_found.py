class HTTPNotFoundError(Exception):

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.status_code = 404
        self.name = "HTTPNotFound"
        self.message = message
