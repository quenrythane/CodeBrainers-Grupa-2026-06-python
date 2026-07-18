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
#      Jeżeli nie - informuje o braku wystarczających środków.
#    - pokaz_saldo(): wypisuje aktualne saldo i właściciela konta.
# 
# 4. Stwórz obiekt dla Jana Kowalskiego (saldo początkowe 100 zł).
#    Przetestuj działanie:
#    - Wyświetl saldo
#    - Wpłać 200 zł
#    - Spróbuj wypłacić 400 zł (powinien pojawić się błąd o braku środków)
#    - Wypłać 150 zł
#    - Wyświetl końcowe saldo
