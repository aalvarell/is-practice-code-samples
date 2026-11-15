import pytest
from exceptions_main import dividir

# Pruebas unitarias
def test_dividir():
    # Caso válido
    assert dividir(10, 2) == 5

    # Caso de error: división por cero
    try:
        dividir(10, 0)
    except ValueError as e:
        assert str(e) == "División por cero no permitida"

    # Caso de error: entrada no numérica
    try:
        dividir("10", 2)
    except TypeError as e:
        assert "unsupported operand" in str(e)