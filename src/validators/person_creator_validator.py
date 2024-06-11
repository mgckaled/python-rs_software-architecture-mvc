from pydantic import BaseModel, ValidationError, constr

from src.errors.errors_types.http_unprocessable_entity import \
    HTTPUnprocessableEntityError
from src.views.http_types.http_request import HttpRequest


def person_creator_validator(http_request: HttpRequest) -> None | str:
    class BodyData(BaseModel):
        first_name: constr(min_length=1, max_length=100)  # type: ignore
        last_name: constr(min_length=1, max_length=100)  # type: ignore
        age: int
        pet_id: int

    try:
        BodyData(**http_request.body)

    except ValidationError as e:
        raise HTTPUnprocessableEntityError(message=e.errors()) from e
