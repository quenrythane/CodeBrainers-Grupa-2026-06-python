
# metody vs funckje
moja_lista = [1, 2, 3]
sorted(moja_lista)

moja_lista.sort()



pitagoras = lambda a, b: (a**2 + b**2)**0.5

def pitagoras_klasycznie(a, b):
  return (a**2 + b**2)**0.5


wynik_lambda = pitagoras(6, 8)
wynik_funckja = pitagoras_klasycznie(6, 8)

print(wynik_lambda)
print(wynik_funckja)

print(pitagoras)
print(pitagoras_klasycznie)
