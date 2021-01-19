import requests


def test_get_response_status_code(url, expected_status_code):
    response_status_code = str(requests.get(url).status_code)
    assert expected_status_code == response_status_code
