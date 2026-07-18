lista = [1, 2, 3, 4, 5]

# podejście normalne
lista_kwadratow = []
for liczba in lista:
  if liczba % 2 == 1:
    lista_kwadratow.append(liczba ** 2)

print(lista_kwadratow)

# # list comprehension
lista_kwadratow_lc = [liczba ** 2 for liczba in lista if liczba % 2 == 1]

print(lista_kwadratow_lc)

