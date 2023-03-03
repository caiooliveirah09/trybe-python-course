from testes_automatizados import is_odd, return_hello_my_name, divide

import pytest


def test_is_odd_when_number_is_odd_returns_true():
    "Para um número ímpar a função deve retornar o valor True"
    assert is_odd(3) is True


def test_is_odd_when_number_is_even_returns_false():
    "Para um número par a função deve retornar o valor False"
    assert is_odd(2) is False


def test_return_hello_my_name():
    "Passando o nome Elros, retorna 'Hello Elros'"
    assert return_hello_my_name("Elros") == "Hello Elros"


def test_divide():
    "Testa se divide o número 10 por 2 e o resultado é 5"
    assert divide(10, 2) == 5


def test_divide_number_by_zero_raises_an_exeception():
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        divide(2, 0)
