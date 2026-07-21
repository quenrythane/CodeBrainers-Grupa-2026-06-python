# ten plik jest w nawiązaniu do test_kalkulator2.py. Po to żeby pokazać że można wybierać sterowanie funkcjami

from kalkulator import add

# konwencja nazwy funkcji testowej test_<nazwa_testowanej_funkcji>
# print("\nxd xd xd")
def test_add_positive():
    assert add(2, 2) == 4
    assert add(0, 2) == 2
    assert add(25, 44) == 69
    assert add(2, 2) == 4
    assert add(0, 2) == 2


def test_add_negative():
    assert add(-2, -2) == -4
    assert add(-2, 0) == -2
    assert add(-2, 2) == 0
    assert add(-2, 20) == 18
