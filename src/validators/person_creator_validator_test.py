from .person_creator_validator import person_creator_validator


class MockRequest():
    def __init__(self, body) -> None:
        self.body = body


def test_person_creator_validator() -> None:
    request = MockRequest(body={"first_name": "fulano",
                                "last_name": "deTal",
                                "age": 6,
                                "pet_id": 7})

    person_creator_validator(http_request=request)
