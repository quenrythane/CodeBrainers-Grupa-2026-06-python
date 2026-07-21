"""
ZADANIE (5 minut) - pytest & fixture dla Junior Testera

Scenariusz:
Mamy klasę `Portfel`, która przechowuje stan konta oraz pozwala na wpłatę i wypłatę środków.

Twoje zadanie:
1. Przygotuj fixturę `moj_portfel`, która dostarczy do testów nowy obiekt `Portfel` ze stanem początkowym 100 zł.
2. Napisz test `test_wplata`, który przy użyciu fixtury sprawdzi, czy po wpłacie 50 zł stan portfela wyniesie 150 zł.
3. Napisz test `test_wyplata`, który przy użyciu fixtury sprawdzi, czy po wypłacie 30 zł stan portfela wyniesie 70 zł.

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

# TODO 1: Stwórz fixturę `moj_portfel`

# TODO 2: Napisz test_wplata

# TODO 3: Napisz test_wyplata
