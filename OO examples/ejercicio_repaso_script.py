import ejercicio_repaso_modulo as mod

if(__name__=='__main__'):
    radio = float(input("Indica el radio del círculo:"))
    area_circulo = mod.area_circulo(radio)
    print(f"El área del círculo de radio {radio} es {area_circulo:.2f} u^2")