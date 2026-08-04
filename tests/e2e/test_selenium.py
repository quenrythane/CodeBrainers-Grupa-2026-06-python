import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# id - preferowany (unikalny)
# class LUB name - preferowane, jezeli sa unikalne
# xpath - preferowany, jezeli id nie ma lub nie jest unikalny

@pytest.mark.skip
def test_selenium(driver):
    oczekiwany_tytul = "Employee Manager"
    tytul_strony = driver.title
    assert tytul_strony == oczekiwany_tytul


@pytest.mark.selenium
def test_add_user(driver, user):
    driver.find_element(By.ID, "name").send_keys(user.name)
    driver.find_element(By.ID, "salary").send_keys(user.salary)
    driver.find_element(By.ID, "age").send_keys(user.age)
    Select(driver.find_element(By.ID, "position")).select_by_value(user.position)
    driver.find_element(By.ID, "on_leave").click()
    driver.find_element(By.ID, "submitBtn").click()

    tablerow = WebDriverWait(
        driver,
        timeout=2,
        poll_frequency=0.5
    ).until(EC.visibility_of_element_located((By.TAG_NAME, "tr")))

    last_row = driver.find_elements(By.TAG_NAME, "tr")[-1]
    row_data = last_row.find_elements(By.TAG_NAME, "td")

    assert row_data[1].text == user.name
    assert row_data[2].text == user.salary
    assert row_data[3].text == user.age
    assert row_data[4].text == user.position
    assert row_data[5].text == user.on_leave
