import math

def calcular_area_rectangulo():
    """Función para calcular el área de un rectángulo."""
    ancho = float(input("Introduce el ancho del rectángulo: "))
    alto = float(input("Introduce el alto del rectángulo: "))
    return ancho * alto

def calcular_area_circulo():
    """Función para calcular el área de un círculo."""
    radio = float(input("Introduce el radio del círculo: "))
    return math.pi * radio * radio

def mostrar_menu():
    """Función que muestra el menú de opciones."""
    print("Elige una opción para calcular el área:")
    print("1. Rectángulo")
    print("2. Círculo")

def main():
    mostrar_menu()
    opcion = int(input("Introduce la opción (1 o 2): "))

    if opcion == 1:
        area = calcular_area_rectangulo()
        print(f"El área del rectángulo es {area}")
    elif opcion == 2:
        area = calcular_area_circulo()
        print(f"El área del círculo es {area}")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
