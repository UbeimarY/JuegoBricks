import pytest
from src.palindromo import es_palindromo

def test_es_palindromo():
    assert es_palindromo("Anita lava la tina") is True
    assert es_palindromo("Oso") is True
    assert es_palindromo("Python") is False
    assert es_palindromo("A man a plan a canal Panama") is True
