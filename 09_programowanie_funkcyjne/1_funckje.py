
def zrob_herbate(rodzaj_herbaty: str, czy_dodać_cukier: bool = False) -> str :
    """ xd docstring = string który jest dokumentacją i mówi co funkcja robi
    druga linia """
    print("zaczynam robic herbatki!")
    print("zagotuj wodę")
    print(f"zaparz herbatke {rodzaj_herbaty}")
    if czy_dodać_cukier:
        print("dodaj CUKIER")
    print("herbatka gotowa\n")
    return rodzaj_herbaty.upper()


xd = zrob_herbate("czarna", True)
print(xd)

