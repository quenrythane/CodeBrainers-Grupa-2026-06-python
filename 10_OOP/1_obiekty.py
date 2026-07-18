
lista_1 = [1, 2, 3]
lista_2 = lista_1  # kopia płytka
lista_2 = lista_1.copy()  # kopia głęboka

print(lista_1)
print(lista_2)

print(id(lista_1))
print(id(lista_2))

lista_1.append(4)

print(lista_1)
print(lista_2)
