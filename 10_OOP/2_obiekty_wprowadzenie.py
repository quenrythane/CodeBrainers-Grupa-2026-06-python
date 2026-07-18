class Osoba:
    def __init__(self, imie, wiek, plec):
        self.imie = imie
        self.wiek = wiek
        self.plec = plec


artur = Osoba("Artur", 20, "mężczyzna")
ania = Osoba("Ania", 44, "kobieta")

artur_slownik = {
    "imie": "Artur",
    "wiek": 20,
    "plec": "mężczyzna"
}


print(artur.imie)
print(artur.wiek)
artur.wiek = 21
print(artur.wiek)
artur.hobby = "Snowboarding"
print(artur.hobby)
print(ania.hobby)
