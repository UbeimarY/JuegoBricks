import pytest
from src.extra_utils import factorial

def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    assert factorial(7) == 5040
    with pytest.raises(ValueError):
        factorial(-3)  # Debe lanzar un error porque el factorial de negativos no existe
