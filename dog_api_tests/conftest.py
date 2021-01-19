import pytest


@pytest.fixture(scope="session")
def endpoint():
    host = "https://dog.ceo/"
    endpoint_dict = {
        "list_all_breeds": host + "api/breeds/list/all",
        "random_image": host + "api/breeds/image/random",
        # фигурные скобки используется чтобы заменить их
        # на конкретную породу в тесте методом format
        "images_by_breed": host + "api/breed/{}/images",
        "subreed_by_breed": host + "api/breed/{}/list"
    }
    return endpoint_dict


@pytest.fixture(scope="session")
def schema():
    schema = {
        "name": {"type": "string", "required": True},
        "surname": {"type": "string", "required": True},
        "grade": {"type": "number", "required": True}
    }
    return schema

