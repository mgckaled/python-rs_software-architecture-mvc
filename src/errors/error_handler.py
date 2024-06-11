from src.errors.errors_types.http_bad_request import HTTPBadRequestError
from src.errors.errors_types.http_not_found import HTTPNotFoundError
from src.errors.errors_types.http_unprocessable_entity import \
    HTTPUnprocessableEntityError
from src.views.http_types.http_response import HttpResponse


def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HTTPBadRequestError, HTTPNotFoundError, HTTPUnprocessableEntityError)):
        return HttpResponse(
            status_code=error.status_code,
            body={"errors": [{"title": error.name, "detail": error.message}]},
        )

    return HttpResponse(status_code=500, body={"errors": [{"title": "InternalServerError", "detail": str(object=error)}]})
