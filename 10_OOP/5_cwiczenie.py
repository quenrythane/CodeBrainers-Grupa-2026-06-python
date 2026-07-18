# ZADANIE (5 minut): Klasa KartaMiejska
# 
# Cel dydaktyczny:
# - Ćwiczenie tworzenia klasy, konstruktora i metod.
# - Zwrócenie szczególnej uwagi na warunki brzegowe (np. gdy stan konta jest dokładnie równy cenie biletu).
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
#    - doladuj(kwota): dodaje podaną kwotę do środków i wypisuje komunikat o doładowaniu.
#    - skasuj_bilet():
#      * Jeśli środki na karcie są WIĘKSZE LUB RÓWNE cenie biletu: odejmuje cenę biletu i wypisuje komunikat o pomyślnym skasowaniu oraz pozostałych środkach.
#      * W przeciwnym razie: informuje o braku środków (wypisując cenę biletu oraz aktualny stan karty).
#    - pokaz_stan(): wypisuje numer karty oraz aktualny stan środków.
# 
# 4. Scenariusz testowy (testujemy warunki brzegowe!):
#    - Stwórz obiekt dla karty "KM-777" z domyślnym stanem środków (0.0 zł) i ceną biletu ustawioną na 4.0 zł.
#    - Spróbuj skasować bilet (powinno się nie udać).
#    - Doładuj kartę kwotą dokładnie 4.0 zł.
#    - Spróbuj skasować bilet (powinno się udać, stan konta powinien wynieść dokładnie 0.0 zł).
#    - Doładuj kartę kwotą 10.0 zł.
#    - Skasuj bilet (powinno się udać, stan konta = 6.0 zł).
#    - Wyświetl stan karty na koniec.
