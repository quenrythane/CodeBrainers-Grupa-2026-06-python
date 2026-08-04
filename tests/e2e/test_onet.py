import pytest
from pageObjects.onet import Onet

@pytest.mark.onet
def test_onet(driver):
    onet_page = Onet(driver)

    onet_page.open()
    onet_page.close_cookie_window()
    onet_page.click_button(onet_page.LOGIN_BUTTON)
    input()
