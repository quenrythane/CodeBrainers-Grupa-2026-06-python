
from pytest_bdd import given, parsers, scenarios, then, when
from tests.e2e.pageObjects.onet import Onet
# pip install pytest-bdd


scenarios("../features/onet_login.feature")


@given("użytkownik otwiera stronę główną")
def onet_open(driver):
    onet_page = Onet(driver)
    onet_page.open()

@given("użytkownik akceptuje pliki cookies")
def onet_close_cookie_window(driver):
    onet_page = Onet(driver)
    onet_page.close_cookie_window()

@when("użytkownik klika w przycisk logowania")
def onet_click_login_button(driver):
    onet_page = Onet(driver)
    onet_page.click_button(onet_page.LOGIN_BUTTON)

@when('użytkownik podaje email')
def onet_enter_login_credentials(driver):
    onet_page = Onet(driver)
    onet_page.enter_login_credentials("abc@wp.pl")

@when("użytkownik przełącza się na okno logowania")
def onet_switch_to_login_window(driver):
    onet_page = Onet(driver)
    onet_page.switch_to_login_window()

@then("pojawia się ekran wysłania hasła")
def onet_email_sent_page(driver):
    onet_page = Onet(driver)
    assert onet_page.driver.find_element(*onet_page.SEND_CHANGE_PASSWORD_BUTTON).is_displayed()
