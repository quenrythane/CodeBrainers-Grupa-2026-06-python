"""
ZADANIE (5 minut) - pytest & fixture dla Junior Testera

Scenariusz:
Testujemy klasę `KoszykSklepowy`, która obsługuje dodawanie produktów, obliczanie sumy oraz czyszczenie koszyka.

Twoje zadanie:
1. Stwórz fixturę `@pytest.fixture` o nazwie `koszyk`, która tworzy i zwraca nowy (pusty) obiekt klasy `KoszykSklepowy`.
2. Napisz test `test_dodawanie_produktow(koszyk)`, który:
   - Dodaje produkt "Chleb" o cenie 4.50
   - Dodaje produkt "Mleko" o cenie 3.20
   - Sprawdza (assert), czy suma koszyka wynosi 7.70 oraz czy w koszyku są 2 produkty (`len(koszyk.produkty) == 2`).
3. Napisz test `test_czyszczenie_koszyka(koszyk)`, który:
   - Dodaje dowolny produkt do koszyka.
   - Wywołuje metodę `czysc()`.
   - Sprawdza (assert), czy suma wynosi 0 oraz czy koszyk jest pusty.

Uruchomienie testów z terminala:
python -m pytest -v pytest_cwiczenia/pytest_cwiczenie.py
"""

import pytest


class KoszykSklepowy:
    def __init__(self):
        self.produkty = []

    def dodaj_produkt(self, nazwa: str, cena: float):
        self.produkty.append({"nazwa": nazwa, "cena": cena})

    def pobierz_suma(self) -> float:
        return sum(p["cena"] for p in self.produkty)

    def czysc(self):
        self.produkty.clear()


# ==============================================================================
# MIEJSCE NA TWOJE ROZWIĄZANIE (Zadanie dla Junior Testera):
# ==============================================================================

# TODO 1: Stwórz fixturę `koszyk` zwracającą instancję KoszykSklepowy
# @pytest.fixture
# def koszyk():
#     ...

# TODO 2: Napisz test_dodawanie_produktow(koszyk)

# TODO 3: Napisz test_czyszczenie_koszyka(koszyk)
