import pytest
from pageObjects.base_page import BasePage


@pytest.mark.skip
def test_selenium(driver):
    oczekiwany_tytul = "Employee Manager"
    tytul_strony = driver.title
    assert tytul_strony == oczekiwany_tytul


@pytest.mark.selenium
def test_add_user(driver, user):
    base_page = BasePage(driver)

    base_page.fill_employee_form(user)
    last_row = base_page.get_last_table_row()
    row_data = base_page.get_table_row_data(last_row)

    assert row_data[1].text == user.name
    assert row_data[2].text == user.salary
    assert row_data[3].text == user.age
    assert row_data[4].text == user.position
    assert row_data[5].text == user.on_leave
