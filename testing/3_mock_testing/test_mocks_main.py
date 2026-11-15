from unittest.mock import Mock

from mocks_main import procesar_datos

# Caso de prueba con stub (mock)
def test_procesar_datos():
    # Stub: simula la función validadora
    stub_validador = Mock()
    stub_validador.return_value = True  # Configuración del comportamiento

    # Prueba
    resultado = procesar_datos(stub_validador, "test")
    assert resultado == "Datos válidos: test"

    # Verifica que el stub fue invocado correctamente
    stub_validador.assert_called_once_with("test")