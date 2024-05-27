class HttpResponse():

    def __init__(self, status_code: int, body: dict = None) -> None:
        """
        Initializes a new instance of the HttpResponse class.

        Args:
            status_code (int): The HTTP status code of the response.
            body (dict, optional): The body of the response. Defaults to None.
        """
        self.status_code = status_code
        self.body = body
