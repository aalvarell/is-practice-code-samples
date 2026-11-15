from white_box_main import es_primo

# Pruebas unitarias con caja blanca
def test_es_primo_rutas_independientes():
    # Probar rutas independientes
    # Ruta 1: Número menor que 2
    assert es_primo(-1) == False  # Negativos
    assert es_primo(0) == False   # Cero
    assert es_primo(1) == False  # Uno

    # Ruta 2: Número igual a 2 (primer número primo)
    assert es_primo(2) == True

    # Ruta 3: Número mayor que 2 y divisible por otro número
    assert es_primo(4) == False  # Divisible por 2
    assert es_primo(9) == False  # Divisible por 3

    # Ruta 4: Número mayor que 2 y no divisible por ningún número
    assert es_primo(3) == True  # Primo pequeño
    assert es_primo(17) == True  # Primo mayor

def test_es_primo_limites_bucles():
    # Probar límites de bucles
    assert es_primo(2) == True   # Caso sin iteraciones del bucle
    assert es_primo(3) == True   # Caso con una sola iteración
    assert es_primo(4) == False  # Caso con salida temprana del bucle
    assert es_primo(7) == True   # Caso con múltiples iteraciones completas
    assert es_primo(25) == False # Caso con salida en iteración intermedia
    assert es_primo(97) == True  # Caso con máximas iteraciones y primo

def test_es_primo_condiciones_extremas():
    # Probar condiciones extremas
    assert es_primo(-100) == False  # Número negativo grande
    assert es_primo(-5) == False    # Número negativo pequeño
    assert es_primo(-1) == False    # Negativo mínimo
    assert es_primo(0) == False     # Cero
    assert es_primo(1) == False     # Uno (caso especial)
    assert es_primo(2) == True      # Primer número primo
    assert es_primo(2.5) == False   # Número decimal
    assert es_primo(10000) == False # Número grande compuesto
    assert es_primo(9973) == True   # Número grande primo

def test_es_primo_decisiones_logicas():
    # Probar decisiones lógicas
    # Condición inicial n < 2
    assert es_primo(1) == False  # True branch: n < 2
    assert es_primo(2) == True   # False branch: n >= 2

    # Condición del bucle i <= n/2
    assert es_primo(3) == True   # Bucle completo sin encontrar divisores
    assert es_primo(4) == False  # Bucle con salida temprana

    # Decisiones de divisibilidad
    assert es_primo(8) == False  # Divisible por número pequeño
    assert es_primo(15) == False # Divisible por número intermedio
    assert es_primo(23) == True  # No divisible por ningún número