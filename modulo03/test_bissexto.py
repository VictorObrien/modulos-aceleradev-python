import pytest


def eh_bissexto(ano):
    resto = ano % 4
    resto100 = ano % 100
    resto400 = ano % 400

    if not resto:
        if not resto400:
            return True
        elif resto100:
            return True

    return False

   # if resto or not resto100 and resto400
    # return False
    # return True"""


# primeiro parametro é uma variavel e o segundo são os valores para essa variável
@pytest.mark.parametrize('ano', [1600, 1732, 1888, 1944, 2008])
def test_deve_ser_ano_bissexto(ano):
    resp = eh_bissexto(ano)

    assert resp is True


@pytest.mark.parametrize('ano', [500, 1742, 1889, 1951, 2011])
def test_nao_deve_ser_bissexto(ano):
    resp = eh_bissexto(ano)

    assert resp is False
