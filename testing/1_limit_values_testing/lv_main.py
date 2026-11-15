# Código a probar
def obtener_elemento(lista, indice):
    if 0 <= indice < len(lista):
        return lista[indice]
    else:
        raise IndexError("Índice fuera de rango")
