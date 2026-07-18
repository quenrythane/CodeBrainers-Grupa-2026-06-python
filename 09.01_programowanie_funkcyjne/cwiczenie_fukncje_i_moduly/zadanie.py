"""
ZADANIE NA 5 MINUT: Kalkulator Zamówień w Herbaciarni

Twoim zadaniem jest napisanie prostego programu rozbitego na dwa pliki (moduły), który obliczy koszt zamówienia herbaty.

KROK 1:
Stwórz plik `cennik.py`, a w nim funkcję:
`oblicz_koszt(rodzaj: str, ilosc: int, rabat_procent: int = 0) -> float`

Funkcja ma:
- Założyć ceny bazowe:
  * "czarna" -> 8.0 zł za sztukę
  * "zielona" -> 10.0 zł za sztukę
  * każda inna -> 9.0 zł za sztukę
- Obliczyć koszt całkowity (cena * ilość).
- Uwzględnić rabat (np. rabat_procent = 10 oznacza 10% zniżki).
- Zwrócić ostateczną kwotę zaokrągloną do 2 miejsc po przecinku.
- Posiadać type hinting oraz krótki docstring.

KROK 2 (w tym pliku - `zadanie.py`):
- Zaimportuj funkcję `oblicz_koszt` z modułu `cennik`.
- Przetestuj jej działanie, wypisując w konsoli koszt dla:
  1. 3 czarnych herbat bez rabatu (oczekiwany wynik: 24.0 zł)
  2. 2 zielonych herbat z rabatem 20% (oczekiwany wynik: 16.0 zł)
"""

# def oblicz_koszt(rodzaj: str, ilosc: int, rabat_procent: int = 0) -> float:
#     cennik = {
#         "czarna": 8.0,
#         "zielona": 10.0,
#     }
#     cena = cennik.get(rodzaj, 9.0)
#     koszt = cena * ilosc
#     koszt *= (1 - rabat_procent / 100)
#     return round(koszt, 2)



# def oblicz_koszt(rodzaj: str, ilosc: int, rabat_procent: int = 0) -> float:
#   rodzaje = {'czarna': 8, 'zielona': 10}
#   if rodzaj in rodzaje:
#     cena = (rodzaje[rodzaj]*ilosc)*(1 - rabat_procent*0.01)
#   else:
#     cena = (9*ilosc)*(1 - rabat_procent*0.01)
#   return round(cena,2)

# DRY - Don't Repeat Yourself
# S.O.L.I.D programowanie
def oblicz_koszt(rodzaj: str, ilosc: int, rabat_procent: int = 0) -> float:
  cennik = {
    'czarna': 8,
    'zielona': 10,
    'czerwona': 12
  }

  cena_produktu = cennik.get(rodzaj, 9.0)
  cena_finalna = (cena_produktu * ilosc) * (1 - rabat_procent * 0.01)
  return round(cena_finalna, 2)

