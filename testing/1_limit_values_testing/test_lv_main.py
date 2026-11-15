import pytest
from lv_main import obtener_elemento

# Pruebas unitarias
def test_obtener_elemento():
    lista = [10, 20, 30, 40, 50]
    # Valores en los límites
    assert obtener_elemento(lista, 0) == 10  # Primer elemento
    assert obtener_elemento(lista, 4) == 50  # Último elemento
    # Valores fuera de los límites
    try:
        obtener_elemento(lista, -1)
    except IndexError:
        pass
    try:
        obtener_elemento(lista, 5)
    except IndexError:
        pass