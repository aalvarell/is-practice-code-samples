# Componente que vamos a probar
def procesar_datos(validador, datos):
    if validador(datos):
        return f"Datos válidos: {datos}"
    else:
        return "Error: Datos inválidos"