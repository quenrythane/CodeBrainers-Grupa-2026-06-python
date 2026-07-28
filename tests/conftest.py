import pytest

@pytest.fixture
def payload_data():
    payload_data = {
        "name": "Dominik",
        "salary": 4000,
        "age": 40,
        "position": "Junior QA",
        "on_leave": False
    }

    return payload_data


@pytest.fixture(scope="session", autouse=True)
def hello_fixture():
    print("\nHello from fixture!")
    # szykować dane
    # pobierać dane z bazy danych
    yield
    print("\nGoodbye from fixture!")
    # sprzątać po sobie
    # czyścić bazę danych
