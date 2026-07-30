from selenium import webdriver
import pytest

@pytest.mark.seler
def test_selenium():
    URL = "http://127.0.0.1:8000/"

    driver = webdriver.Chrome()  # tworzy robocika - przewodnika po przeglądarce
    driver.get(URL)

    tytul_strony = driver.title

    print(tytul_strony)
    assert tytul_strony == "Employee Manager"

    input("Wcisnij enter zeby zamknac")

    driver.close()  # zamyka robocika

