class HttpRequest():

    def __init__(self, body: dict = None, param: dict = None, header: dict = None) -> None:
        """
        Initializes a new instance of the HttpRequest class.

        Parameters:
            body (dict, optional): The body of the request. Defaults to None.
            param (dict, optional): The parameters of the request. Defaults to None.
            header (dict, optional): The headers of the request. Defaults to None.
        """
        self.body = body
        self.param = param
        self.header = header
