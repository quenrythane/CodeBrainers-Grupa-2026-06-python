from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# POM - Page Object Model

# id - preferowany (unikalny)
# class LUB name - preferowane, jezeli sa unikalne
# xpath - preferowany, jezeli id nie ma lub nie jest unikalny

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    URL = "http://127.0.0.1:8000/"
    NAME_INPUT_LOCATOR = (By.ID, "name")
    SALARY_INPUT_LOCATOR = (By.ID, "salary")
    AGE_INPUT_LOCATOR = (By.ID, "age")
    POSITION_SELECT_LOCATOR = (By.ID, "position")
    ON_LEAVE_CHECKBOX_LOCATOR = (By.ID, "on_leave")
    SUBMIT_BUTTON_LOCATOR = (By.ID, "submitBtn")
    TABLE_ROW_LOCATOR = (By.TAG_NAME, "tr")
    TABLE_CELL_LOCATOR = (By.TAG_NAME, "td")

    def fill_name_input(self, name_data):
        self.driver.find_element(*self.NAME_INPUT_LOCATOR).send_keys(name_data)

    def fill_salary_input(self, salary_data):
        self.driver.find_element(*self.SALARY_INPUT_LOCATOR).send_keys(salary_data)

    def fill_age_input(self, age_data):
        self.driver.find_element(*self.AGE_INPUT_LOCATOR).send_keys(age_data)

    def fill_employee_form(self, user_data):
        self.driver.find_element(*self.NAME_INPUT_LOCATOR).send_keys(user_data.name)
        self.driver.find_element(*self.SALARY_INPUT_LOCATOR).send_keys(user_data.salary)
        self.driver.find_element(*self.AGE_INPUT_LOCATOR).send_keys(user_data.age)
        Select(self.driver.find_element(*self.POSITION_SELECT_LOCATOR)).select_by_value(user_data.position)
        if user_data.on_leave == "✅":
            self.driver.find_element(*self.ON_LEAVE_CHECKBOX_LOCATOR).click()
        self.driver.find_element(*self.SUBMIT_BUTTON_LOCATOR).click()

    def get_last_table_row(self):
        table_row = WebDriverWait(
            self.driver,
            timeout=2,
            poll_frequency=0.5
        ).until(EC.visibility_of_element_located(self.TABLE_ROW_LOCATOR))
        return self.driver.find_elements(*self.TABLE_ROW_LOCATOR)[-1]

    def get_table_row_data(self, table_row):
        return table_row.find_elements(*self.TABLE_CELL_LOCATOR)

