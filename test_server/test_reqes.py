import json
import urllib3
import requests
from jsonschema import validate
from test_server.schemas.schemas import post_users


urllib3.disable_warnings()
test_url = 'http://127.0.0.1:8002/api/'


def test_schema_validate_from_file():
    response = requests.post(test_url + "user", data={"name": "morpheus", "job": "master"})
    body = response.json()

    assert response.status_code == 201
    with open("test_server/schemas/post_users.json") as file:
        validate(body, schema=json.loads(file.read()))


def test_schema_validate_from_variable():
    response = requests.post(test_url + "user", data={"name": "morpheus", "job": "master"})
    body = response.json()

    assert response.status_code == 201
    validate(body, schema=post_users)


def test_job_name_from_request_returns_in_response():
    job = "master"
    name = "morpheus"

    response = requests.post(test_url + "users", json={"name": name, "job": job})
    body = response.json()

    assert body["name"] == name
    assert body["job"] == job


def test_get_users_returns_unique_users():
    response = requests.get(
        url=test_url + "users",
        params={"page": 2, "per_page": 4},
        verify=False
    )
    ids = [element["id"] for element in response.json()["data"]]

    assert len(ids) == len(set(ids))
