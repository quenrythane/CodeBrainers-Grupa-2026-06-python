import requests


BASE_URL = "http://127.0.0.1:8000/api"
BASE_URL = "http://localhost:8000/api"


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

def test_post_create_employee():
    # AAA
    # ARRANGE
    URL_POST_EMPLOYEES = f"{BASE_URL}/employees"

    headers = {
        'Accept': '*/*',
    }

    payload = {
        "name": "Cezary",
        "salary": 3000,
        "age": 30,
        "position": "Junior QA",
        "on_leave": False
    }

    # ACT
    response = requests.post(URL_POST_EMPLOYEES, headers=headers, json=payload)

    # ASSERT
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["name"] == "Cezary"
    assert response_body["salary"] == 3000
    assert response_body["age"] == 30
    assert response_body["position"] == "Junior QA"
    assert response_body["on_leave"] == False

