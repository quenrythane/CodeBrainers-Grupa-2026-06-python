
# scope zmiennych
xd = "scope globalnego"

def print_scope_xd():
    # spróbuj uruchomić kod raz z poniższą linijką zakomentowaą, drugi raz z odkomentowaną
    xd = "scope lokalny"
    print(xd)

print(xd)  # scope globalnego
print_scope_xd()  # scope lokalny
print(xd)  # scope globalnego