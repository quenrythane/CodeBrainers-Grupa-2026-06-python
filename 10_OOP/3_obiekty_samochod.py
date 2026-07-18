class Car:
    ilosc_kol = 4
    ilosc_miejsc = 5

    def __init__(self, marka, rocznik, kolor, rodzaj_paliwa):
        self.marka = marka
        self.rocznik = rocznik
        self.kolor = kolor
        self.rodzaj_paliwa = rodzaj_paliwa

    def jedz(self, dystans):
        print(f"{self.marka} jedzie... Przejechany dystans: {dystans} km")

    def zatankuj_paliwo(self, ilosc_paliwa):
        return f"{self.marka} tankuje {ilosc_paliwa} litrów {self.rodzaj_paliwa}"



polonez = Car("Polonez", 2000, "czerwony", "benzyna")
fiat = Car("Fiat", 2019, "czarny", "diesel")

print(polonez.marka)
polonez.jedz(10)
fiat.jedz(20)

polonez.ilosc_kol = 3
print(polonez.ilosc_kol)
print(fiat.ilosc_kol)
print(polonez.zatankuj_paliwo(50))