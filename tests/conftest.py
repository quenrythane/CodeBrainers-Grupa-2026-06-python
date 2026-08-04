import pytest
from dataclasses import dataclass
from selenium import webdriver

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


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--popup-blocker-enable")

    # options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    # driver.implicitly_wait(2)
    yield driver
    driver.quit()


@dataclass
class User:
    id: str = "1"
    name: str = "Asia"
    salary: str = "1000"
    age: str = "18"
    position: str = "Junior QA"
    on_leave: str = "✅"




@pytest.fixture
def user():
    return User()
