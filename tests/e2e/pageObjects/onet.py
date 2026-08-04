from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# POM - Page Object Model

# id - preferowany (unikalny)
# class LUB name - preferowane, jezeli sa unikalne
# xpath - preferowany, jezeli id nie ma lub nie jest unikalny

class Onet:
    def __init__(self, driver):
        self.driver = driver

    URL = "https://www.onet.pl"
    NEWS_TITLE = (By.XPATH, "//h1/a/span")
    LOGIN_BUTTON = (By.XPATH, "/html/body/div[1]/header/div[3]/div/div[2]/div/div/button")
    COOKIE_WINDOW = (By.XPATH, '/html/body/div[15]/div/div[2]/div/div[6]/button[2]')

    def open(self):
        self.driver.get(self.URL)

    def get_news_title(self):
        return self.driver.find_element(*self.NEWS_TITLE).text

    def close_cookie_window(self):
        cookie_window = WebDriverWait(
            self.driver,
            timeout=5,
            poll_frequency=0.5
        ).until(EC.visibility_of_element_located(self.COOKIE_WINDOW))
        cookie_window.click()

    def click_button(self, button_selector):
        button = WebDriverWait(
            self.driver,
            timeout=5,
            poll_frequency=0.5
        ).until(EC.element_to_be_clickable(button_selector))


        button.click()
