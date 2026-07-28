import requests
import pytest


BASE_URL = "http://127.0.0.1:8000/api"
BASE_URL = "http://localhost:8000/api"
global employee_id
employee_id = 2


def test_get_health():
    URL_HEALTH = "http://localhost:8000/health"
    try:
        response = requests.get(URL_HEALTH)

        print()
        print(response)
        print(response.json())
        print(response.status_code)

    except requests.exceptions.RequestException as e:
        print("Wystąpił błąd podczas wysyłania żądania:", e)

@pytest.mark.create_employee
def test_post_create_employee():
    # AAA
    # ARRANGE
    URL_POST_EMPLOYEES = f"{BASE_URL}/employees"

    headers = {
        'Accept': '*/*',
    }

    payload = payload_data

    # ACT
    response = requests.post(URL_POST_EMPLOYEES, headers=headers, json=payload)
    response_body = response.json()
    employee_id = response_body["id"]

    # ASSERT
    assert response.status_code == 200
    assert response_body["name"] == payload_data["name"]
    assert response_body["salary"] == payload_data["salary"]
    assert response_body["age"] == payload_data["age"]
    assert response_body["position"] == payload_data["position"]
    assert response_body["on_leave"] == payload_data["on_leave"]


def test_put_update_employee():
    # AAA
    # ARRANGE
    URL_PUT_EMPLOYEES = f"{BASE_URL}/employees/{employee_id}"

    headers = {
        'Accept': '*/*',
    }

    payload = {
        "name": "XD",
        "salary": 3000,
        "age": 30,
        "position": "Junior QA",
        "on_leave": True
    }

    # ACT
    response = requests.put(URL_PUT_EMPLOYEES, headers=headers, json=payload)

    # ASSERT
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["name"] == "XD"
    assert response_body["salary"] == 3000
    assert response_body["age"] == 30
    assert response_body["position"] == "Junior QA"
    assert response_body["on_leave"] == True


def test_delete_employee():
    # ARRANGE
    URL_DELETE_EMPLOYEES = f"{BASE_URL}/employees/{employee_id}"

    # ACT
    response = requests.delete(URL_DELETE_EMPLOYEES)

    # ASSERT
    response_body = response.json()
    assert response.status_code == 200
    print(response_body)

