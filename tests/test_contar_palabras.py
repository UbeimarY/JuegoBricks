import pytest
from src.extra_utils import contar_palabras

def test_contar_palabras():
    assert contar_palabras("Hola mundo") == 2
    assert contar_palabras("El rápido zorro marrón salta sobre el perro perezoso") == 9
    assert contar_palabras("") == 0
    assert contar_palabras("   ") == 0
