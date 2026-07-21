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




class KoszykSklepowy:
    def __init__(self):
        self.produkty = []

    def dodaj_produkt(self, nazwa: str, cena: float):
        self.produkty.append({"nazwa": nazwa, "cena": cena})

    def pobierz_suma(self) -> float:
        # produkt = {"nazwa": "Chleb", "cena": 4.50}
        lista_z_cenami = [produkt["cena"] for produkt in self.produkty]
        return sum(lista_z_cenami)

    def czysc(self):
        self.produkty.clear()


# ==============================================================================
# MIEJSCE NA TWOJE ROZWIĄZANIE (Zadanie dla Junior Testera):
# ==============================================================================
import pytest

# TODO 1: Stwórz fixturę `koszyk` zwracającą instancję KoszykSklepowy
@pytest.fixture
def koszyk():
    return KoszykSklepowy()


# TODO 2: Napisz test_dodawanie_produktow(koszyk)
def test_dodawanie_psroduktow(koszyk):
    koszyk.dodaj_produkt("Chleb", 4.50)
    koszyk.dodaj_produkt("Mleko", 3.20)
    assert koszyk.pobierz_suma() == 7.70
    assert len(koszyk.produkty) == 2


# TODO 3: Napisz test_czyszczenie_koszyka(koszyk)
def test_czyszczenie_koszyka(koszyk):
    koszyk.dodaj_produkt("Chleb", 4.50)
    koszyk.czysc()
    assert koszyk.pobierz_suma() == 0
    assert len(koszyk.produkty) == 0