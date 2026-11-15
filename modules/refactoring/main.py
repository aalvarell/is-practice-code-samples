import math

# Programa principal
print("Elige una opción para calcular el área:")
print("1. Rectángulo")
print("2. Círculo")
opcion = int(input("Introduce la opción (1 o 2): "))

if opcion == 1:
    # Calcular área del rectángulo
    ancho = float(input("Introduce el ancho del rectángulo: "))
    alto = float(input("Introduce el alto del rectángulo: "))
    area_rectangulo = ancho * alto
    print(f"El área del rectángulo es {area_rectangulo}")

elif opcion == 2:
    # Calcular área del círculo
    radio = float(input("Introduce el radio del círculo: "))
    area_circulo = math.pi * radio * radio
    print(f"El área del círculo es {area_circulo}")

else:
    print("Opción no válida")
