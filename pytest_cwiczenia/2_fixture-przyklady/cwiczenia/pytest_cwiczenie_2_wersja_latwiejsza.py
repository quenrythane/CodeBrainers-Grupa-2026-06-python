"""
ŁATWIEJSZE ZADANIE (5 minut) - pytest & fixture dla Junior Testera

Scenariusz:
Testujemy klasę `Portfel`, która przechowuje stan konta (domyślnie 100 zł)
oraz pozwala na wpłatę i wypłatę pieniędzy.

Twoje zadanie:
1. Stwórz fixturę `@pytest.fixture` o nazwie `moj_portfel`, która zwraca obiekt `Portfel(100)`
   (portfel z początkowym stanem 100 zł).
2. Napisz test `test_wplata(moj_portfel)`, który:
   - Wpłaca 50 zł (`moj_portfel.wplata(50)`).
   - Sprawdza (assert), czy `moj_portfel.stan` wynosi 150.
3. Napisz test `test_wyplata(moj_portfel)`, który:
   - Wypłaca 30 zł (`moj_portfel.wyplata(30)`).
   - Sprawdza (assert), czy `moj_portfel.stan` wynosi 70.

Uruchomienie testów z terminala:
python -m pytest -v pytest_cwiczenia/pytest_cwiczenie_2.py
"""

import pytest


class Portfel:
    def __init__(self, stan_poczatkowy: int = 100):
        self.stan = stan_poczatkowy

    def wplata(self, kwota: int):
        self.stan += kwota

    def wyplata(self, kwota: int):
        self.stan -= kwota


# ==============================================================================
# MIEJSCE NA TWOJE ROZWIĄZANIE (Zadanie dla Junior Testera):
# ==============================================================================

# TODO 1: Stwórz fixturę `moj_portfel` zwracającą Portfel(100)
# @pytest.fixture
# def moj_portfel():
#     ...

# TODO 2: Napisz test_wplata(moj_portfel)

# TODO 3: Napisz test_wyplata(moj_portfel)
