import requests


BASE_URL = "http://127.0.0.1:8000"
BASE_URL = "http://localhost:8000"
URL = f"{BASE_URL}/healthxd"

def test_health():
    try:
        response = requests.get(URL)


        print()
        print(response)
        print(response.json())
        print(response.status_code)


    except requests.exceptions.RequestException as e:
        print("Wystąpił błąd podczas wysyłania żądania:", e)