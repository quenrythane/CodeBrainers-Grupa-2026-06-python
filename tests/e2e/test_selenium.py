import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep


# id - preferowany (unikalny)
# class LUB name - preferowane, jezeli sa unikalne
# xpath - preferowany, jezeli id nie ma lub nie jest unikalny

@pytest.fixture
def driver():
    URL = "http://127.0.0.1:8000/"
    driver = webdriver.Chrome()
    driver.get(URL)
    yield driver
    driver.quit()


@pytest.fixture
def user():
    class User:
        def __init__(self):
            self.id = "1"
            self.name = "Asia"
            self.salary = "1000"
            self.age = "18"
            self.position = "Junior QA"
            self.on_leave = "✅"

    user = User()
    return user


@pytest.mark.skip
def test_selenium(driver):
    # Arrange
    oczekiwany_tytul = "Employee Manager"

    # Act
    tytul_strony = driver.title

    # Assert
    assert tytul_strony == oczekiwany_tytul
    # input("Wcisnij enter zeby zamknac")


@pytest.mark.seler
def test_add_user(driver, user):
    # Arrange

    # Act
    driver.find_element(By.ID, "name").send_keys(user.name)
    driver.find_element(By.ID, "salary").send_keys(user.salary)
    driver.find_element(By.ID, "age").send_keys(user.age)
    Select(driver.find_element(By.ID, "position")).select_by_value(user.position)
    driver.find_element(By.ID, "on_leave").click()
    driver.find_element(By.ID, "submitBtn").click()
    sleep(1)

    #Assert
    elements = driver.find_elements(By.TAG_NAME, "td")  # return a list [Asia, 1000, 18, Junior QA]
    assert user.id in elements[0].text
    assert user.name in elements[1].text
    assert user.salary in elements[2].text
    assert user.age in elements[3].text
    assert user.position in elements[4].text
    assert user.on_leave in elements[5].text

