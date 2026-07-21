from kalkulator import dodawanie, odejmowanie
from dane_testowe import dane_testowe_dodawanie
import pytest

"""" stara "sztywna" wersja """
# def test_add_positive():
#     assert add(2, 2) == 4
#     assert add(0, 2) == 2
#     assert add(25, 44) == 69


"""" nowa "elsatyczna" wersja """
@pytest.mark.parametrize("number_1, number_2, expected_result", dane_testowe_dodawanie)
def test_dodawanie_positive(number_1, number_2, expected_result):
    assert dodawanie(number_1, number_2) == expected_result



