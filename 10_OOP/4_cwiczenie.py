# ZADANIE (5 minut): Klasa KontoBankowe
#
# 1. Stwórz klasę o nazwie KontoBankowe.
#
# 2. W metodzie __init__ zdefiniuj atrybuty:
#    - wlasciciel (imię i nazwisko, przekazywane przy tworzeniu obiektu)
#    - saldo (początkowy stan konta, z wartością domyślną 0)
#
# 3. Dodaj metody:
#    - wplac(kwota): dodaje kwotę do salda i wypisuje komunikat na konsoli.
#    - wyplac(kwota): sprawdza, czy na koncie jest wystarczająco środków.
#      Jeżeli tak - odejmuje kwotę i wypisuje komunikat.
#      Jeżeli nie L- informuje o braku wystarczających środków.
#    - pokaz_saldo(): wypisuje aktualne saldo i właściciela konta.
#
# 4. Stwórz obiekt dla Jana Kowalskiego (saldo początkowe 100 zł).
#    Przetestuj działanie:
#    - Wyświetl saldo
#    - Wpłać 200 zł
#    - Spróbuj wypłacić 400 zł (powinien pojawić się błąd o braku środków)
#    - Wypłać 150 zł
#    - Wyświetl końcowe saldo



class KontoBankowe:
    def __init__(self, wlasciciel, saldo=0):
        self.wlasciciel = wlasciciel
        self.saldo = saldo

    def wplac(self, kwota):
        self.saldo += kwota
        print(f"Dodano {kwota} zł do salda. Obecne saldo = {self.saldo} zł")

    def wyplac(self, kwota):
        if self.saldo <= kwota:
            print(f"Brak wystarczających środków na koncie. Próbujesz wypłacić {kwota} zł, gdy obecne saldo {self.saldo} zł")
        elif self.saldo >= kwota:
            self.saldo -= kwota
            print(f"Odjeto {kwota} zł od salda. Obecne saldo = {self.saldo} zł")

    def pokaz_saldo(self):
        print(f"Obecne saldo = {self.saldo} zł")


Jan_Kowalksi = KontoBankowe("Jan Kowalksi", 100)
Jan_Kowalksi.pokaz_saldo()
Jan_Kowalksi.wplac(200)
Jan_Kowalksi.wyplac(400)
Jan_Kowalksi.wyplac(100)
Jan_Kowalksi.wplac(150)
Jan_Kowalksi.pokaz_saldo



# kobieta
# > 18
# musi być czerwona sukienka
# if plec != "kobieta":
#     print("Nie możesz wejść bo NIE jesteś kobietą")
# elif wiek < 18:
#     print("Nie możesz wejść bo masz mniej niż 18 lat")
# elif kolor_suknieki != "czerwona":
#     print("Nie możesz wejść bo nie masz czerwonej sukienki")
# else:
#     print("Możesz wejść")


# if plec == "kobieta":
#     if wiek > 18:
#         if kolor_suknieki == "czerwona":
#             print("Możesz wejść")
#         else:
#             print("Nie możesz wejść bo nie masz czerwonej sukienki")
#     else:
#         print("Nie możesz wejść bo masz mniej niż 18 lat")
# else:
#     print("Nie możesz wejść bo NIE jesteś kobietą")