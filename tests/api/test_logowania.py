import requests
import pytest




@pytest.mark.auth
def test_auth_token():
    global token
    """Fixture pobierający token autoryzacyjny (accessToken) dla domyślnego użytkownika."""
    login_url = 'https://dummyjson.com/auth/login'

    headers = {
        'Content-Type': 'application/json'
    }

    payload = {
        "username": "michaelw",
        "password": "michaelwpass"
    }

    response = requests.post(login_url, headers=headers, json=payload)
    token = response.json()['accessToken']
    print(token)


@pytest.mark.auth
def test_get_user():
    global token
    url = "https://dummyjson.com/auth/me"

    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.get(url, headers=headers)
    response_body = response.json()
    print(response.status_code)
    print(response_body['firstName'])
    print(response_body['lastName'])
    print(response_body['email'])


