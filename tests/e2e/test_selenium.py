from dataclasses import dataclass
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# id - preferowany (unikalny)
# class LUB name - preferowane, jezeli sa unikalne
# xpath - preferowany, jezeli id nie ma lub nie jest unikalny

@dataclass
class User:
    id: str = "20"
    name: str = "Asia"
    salary: str = "1000"
    age: str = "18"
    position: str = "Junior QA"
    on_leave: str = "✅"


@pytest.fixture
def driver():
    URL = "http://127.0.0.1:8000/"
    options = webdriver.ChromeOptions()
    # options.add_argument("--start-maximized")
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(URL)
    yield driver
    driver.quit()


@pytest.fixture
def user():
    return User()


@pytest.mark.skip
def test_selenium(driver):
    # Arrange
    oczekiwany_tytul = "Employee Manager"

    # Act
    tytul_strony = driver.title

    # Assert
    assert tytul_strony == oczekiwany_tytul
    # input("Wcisnij enter zeby zamknac")


@pytest.mark.selenium
def test_add_user(driver, user):
    # Arrange

    # Act
    driver.find_element(By.ID, "name").send_keys(user.name)
    driver.find_element(By.ID, "salary").send_keys(user.salary)
    driver.find_element(By.ID, "age").send_keys(user.age)
    Select(driver.find_element(By.ID, "position")).select_by_value(user.position)
    driver.find_element(By.ID, "on_leave").click()
    driver.find_element(By.ID, "submitBtn").click()

    # Assert
    WebDriverWait(
        driver,
        timeout=10,
        poll_frequency=0.5
    ).until(EC.visibility_of_element_located((By.TAG_NAME, "table")))


    table_row = [row.find_elements(By.TAG_NAME, "td") for row in driver.find_elements(By.TAG_NAME, "tr") if row.text.split(" ")[0] == user.id][0]
    assert user.id in table_row[0].text
    assert user.name in table_row[1].text
    assert user.salary in table_row[2].text
    assert user.age in table_row[3].text
    assert user.position in table_row[4].text
    assert user.on_leave in table_row[5].text

    # table_rows = driver.find_elements(By.TAG_NAME, "tr")  # pobieramy wiersze tabeli
    # for row in table_rows:
    #     table_cells = driver.find_elements(By.TAG_NAME, "td")  # pobieramy komórki Z TEGO WIERSZA
    #     if table_cells[0].text == user.id:
    #         assert user.id in table_cells[0].text
    #         assert user.name in table_cells[1].text
    #         assert user.salary in table_cells[2].text
    #         assert user.age in table_cells[3].text
    #         assert user.position in table_cells[4].text
    #         assert user.on_leave in table_cells[5].text
            # break




