import pytest

HOST = "https://jsonplaceholder.typicode.com/"


@pytest.fixture(scope="session")
def endpoint():
    endpoint_dict = {
        "host": HOST,
        # фигурные скобки используется чтобы заменить их
        # на конкретный параметр в тесте методом format
        "posts": HOST + "posts/{}",
        "users": HOST + "users/{}",
        "albums": HOST + "albums/{}",
        "comments": HOST + "comments/{}",
        "photos": HOST + "photos/{}",
        "todos": HOST + "todos/{}"
    }
    return endpoint_dict


@pytest.fixture(params={
    HOST + "posts/1": {"userId": {"type": "integer"},
                       "id": {"type": "integer"},
                       "title": {"type": "string"},
                       "body": {"type": "string"}
                       },
    HOST + "comments/1": {"postId": {"type": "integer"},
                          "id": {"type": "integer"},
                          "name": {"type": "string"},
                          "email": {"type": "string", "regex": ".+@.+\..+"},
                          "body": {"type": "string"}
                          },

}.items(), scope="session")
def schema(request):
    return request.param
