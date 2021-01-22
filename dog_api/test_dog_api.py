import pytest
import data
import cerberus
import requests
from http import HTTPStatus


class TestApi:

    def test_list_all_breeds(self, endpoint):
        response = requests.get(endpoint["list_all_breeds"])
        assert response.status_code == HTTPStatus.OK
        all_breed = response.json()["message"]
        assert data.all_breed == all_breed

    def test_random_image_dont_repeat(self, endpoint):
        response = requests.get(endpoint["random_image"])
        first_image = response.json()["message"]

        response = requests.get(endpoint["random_image"])
        second_image = response.json()["message"]

        assert first_image != second_image

    @pytest.mark.parametrize("breed,sub_breed_list", data.all_breed.items())
    def test_sub_breed_by_breed(self, endpoint, breed, sub_breed_list):
        response = requests.get(endpoint["sub_breed_by_breed"].format(breed))
        assert response.json()["message"] == sub_breed_list

    def test_endpoint_schemas(self, schema):
        url, schema = schema[0], schema[1]
        response = requests.get(url).json()
        v = cerberus.Validator(schema)
        assert v.validate(response)

    def test_non_existent_endpoint(self, endpoint):
        response = requests.get(endpoint["host"] + "/some_weird_url")
        assert response.status_code == HTTPStatus.NOT_FOUND
