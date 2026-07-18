lista = [1, 2, 3, 4, 5]

# podejście normalne
lista_kwadratow = []
for liczba in lista:
  lista_kwadratow.append(liczba ** 2)

print(lista_kwadratow)

# list comprehension
lista_kwadratow_lc = [liczba ** 2 for liczba in lista]
lista_kwadratow_lc = [liczba ** 2 for liczba in lista]

print(lista_kwadratow_lc)

