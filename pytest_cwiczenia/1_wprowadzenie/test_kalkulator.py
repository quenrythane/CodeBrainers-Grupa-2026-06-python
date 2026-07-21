
# pip install pytest  <- instalacja
# python -m pytest --version  <- sprawdzenie wersji

# nazwa pliku musi zaczynać się od test_*.py
# nazwa funkcji musi zaczynać się od test_*

# python -m pytest <- odpalamy testy
# python -m pytest -v <- bardziej szczegółowe informacje o testach
# python -m pytest -s <- pokazuje printy
# python -m pytest -q <- mniej szczegółowe informacje o testach
# flagi łączą się <- python -m pytest -vsq   //   python -m pytest -v -s -q


""" Sterowanie które testy chcemy odpalić """
# python -m pytest -v <path/to/test_file>
# python -m pytest -v pytest_cwiczenia/test_kalkulator.py

# python -m pytest -v <path/to/test_file>::<test_function>
# python -m pytest -v pytest_cwiczenia/test_kalkulator.py::test_add_positive

# python -m pytest -v test_kalkulator.py::test_add_positive test_kalkulator2.py::test_add_negative


from kalkulator import add, odejmowanie
import pytest

# konwencja nazwy funkcji testowej test_<nazwa_testowanej_funkcji>
# print("\nxd xd xd")


def test_add_positive():
    assert add(2, 2) == 4
    assert add(0, 2) == 2
    assert add(25, 44) == 69
    assert add(2, 2) == 4
    assert add(0, 2) == 2


def test_add_negative():
    assert add(-2, -2) == -4
    assert add(-2, 0) == -2
    assert add(-2, 2) == 0
    assert add(-2, 20) == 18



@pytest.fixture
def moj_wspanialy_fixture():
    print("\npoczątek testu")
    yield
    print("\nkoniec testu")


def test_odejmowanie(moj_wspanialy_fixture):

    print("\npoczątek testu")

    assert odejmowanie(5, 2) == 3
    assert odejmowanie(0, 2) == -2
    assert odejmowanie(0, 0) == 0
    assert odejmowanie(10, 0.5) == 9.5


    print("\nkoniec testu")



