tekst = "google.com"
wystapienia = {znak: tekst.count(znak) for znak in tekst}


print(wystapienia.items())
for znak, liczba in wystapienia.items():  # (klucz, wartość)
    print(f"{znak}: {liczba}")

# rozpakowanie wartości ciągu
imie, *nazwisko = ("Artur", "Babiński", "xd")
print(imie)
print(nazwisko)



def print_z_funkcja_args(*znaki):
    for znak in znaki:
        print(znak)


print_z_funkcja_args("a", "b", "c")

def print_z_funkcja_kwargs(**znaki):
    for klucz, wartość in znaki.items():
        print(f" Klucz {klucz}: Wartość {wartość}")

print_z_funkcja_kwargs(a=1, b=2, c=3)