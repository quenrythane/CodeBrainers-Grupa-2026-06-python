# ZADANIE (5 minut): Klasa KartaMiejska
#
# Cel dydaktyczny:
# - Ćwiczenie tworzenia klasy, konstruktora i metod.
# - Zwrócenie szczególnej uwagi na warunki brzegowe
# (np. gdy stan konta jest dokładnie równy cenie biletu).
#
# Treść zadania:
# 1. Stwórz klasę o nazwie KartaMiejska.
#
# 2. W metodzie __init__ zdefiniuj atrybuty:
#    - numer_karty (przekazywany przy tworzeniu obiektu)
#    - srodki (stan konta karty, domyślnie 0.0)
#    - cena_biletu (cena pojedynczego przejazdu, domyślnie 4.50)
#
# 3. Dodaj metody:
#    - doladuj(kwota): dodaje podaną kwotę do środków i wypisuje
#  komunikat o doładowaniu.
#    - skasuj_bilet():
#      * Jeśli środki na karcie są WIĘKSZE LUB RÓWNE cenie biletu:
#  odejmuje cenę biletu i wypisuje komunikat o pomyślnym
# skasowaniu oraz pozostałych środkach.
#      * W przeciwnym razie: informuje o braku środków
# (wypisując cenę biletu oraz aktualny stan karty).
#    - pokaz_stan(): wypisuje numer karty oraz aktualny
# stan środków.
#
# 4. Scenariusz testowy (testujemy warunki brzegowe!):
#    - Stwórz obiekt dla karty "KM-777" z domyślnym stanem
# środków (0.0 zł) i ceną biletu ustawioną na 4.0 zł.
#    - Spróbuj skasować bilet (powinno się nie udać).
#    - Doładuj kartę kwotą dokładnie 4.0 zł.
#    - Spróbuj skasować bilet (powinno się udać, stan konta
# powinien wynieść dokładnie 0.0 zł).
#    - Doładuj kartę kwotą 10.0 zł.
#    - Skasuj bilet (powinno się udać, stan konta = 6.0 zł).
#    - Wyświetl stan karty na koniec.


class KartaMiejska:
    def __init__(self, numer_karty, srodki=0.0, cena_biletu=4.50):
        self.numer_karty = numer_karty
        self.srodki = srodki
        self.cena_biletu = cena_biletu

    def doladuj(self, kwota):
        self.srodki += kwota
        print(f"Doładowano kartę {self.numer_karty} kwotą {kwota} zł. Stan konta: {self.srodki} zł.")

    def skasuj_bilet(self):
        if self.srodki >= self.cena_biletu:
            self.srodki -= self.cena_biletu
            print(f"Bilet skasowany! Pozostałe środki: {self.srodki} zł.")
        else:
            print(f"Brak środków na bilet. Cena biletu: {self.cena_biletu} zł, Stan karty: {self.srodki} zł.")

    def pokaz_stan(self):
        print(f"Karta: {self.numer_karty}, Środki: {self.srodki} zł, Cena biletu: {self.cena_biletu} zł.")

        
# Testy
karta = KartaMiejska("KM-777", cena_biletu=4.0)
karta.skasuj_bilet()         # Odrzucone (0.0 < 4.0)
karta.doladuj(4.0)           # Doładowanie dokładnie o cenę biletu
karta.skasuj_bilet()         # Sukces (saldo spada dokładnie do 0.0)
karta.doladuj(10.0)
karta.skasuj_bilet()         # Sukces (zostaje 6.0)
karta.pokaz_stan()
