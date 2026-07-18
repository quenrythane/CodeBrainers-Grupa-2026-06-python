
oceny_uczniow = {
    # klucz: wartość
    "Artur": 1,
    "Bartek": 2,
    "Czesław": 3,
    "Dawid": 4,
    "Eliza": 5,
}

klucze = oceny_uczniow.keys()
wartości = oceny_uczniow.values()
pary = oceny_uczniow.items()

print("klucze:", klucze)
print("wartości:", wartości)
print("pojedyncza para:",list(pary)[0])
print("'lista' par:", pary)

# print(list(klucze))
# print(type(list(klucze)))



