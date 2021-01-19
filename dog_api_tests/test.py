import random
import cerberus
import requests
from http import HTTPStatus


class TestApi:

    def test_list_all_breeds(self, endpoint):
        response = requests.get(endpoint["list_all_breeds"])
        assert response.status_code == HTTPStatus.OK
        print(response.json())

    def test_random_image_dont_repeat(self, endpoint):
        response = requests.get(endpoint["random_image"])
        assert response.status_code == HTTPStatus.OK
        print(response.json())

    def test_images_by_breed(self, endpoint):
        response = requests.get(endpoint["images_by_breed"].format())
        assert response.status_code == HTTPStatus.OK
        print(response.json())

    def test_subreed_by_breed(self, endpoint):
        response = requests.get(endpoint["subreed_by_breed"].format())
        assert response.status_code == HTTPStatus.OK
        print(response.json())
