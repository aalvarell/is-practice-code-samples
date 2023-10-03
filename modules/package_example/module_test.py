# necesario usar prefijo para el módulo
import mates.calculo.integrales
# podemos importar un elemento concreto
from mates.calculo.derivadas import derivar

print(derivar('x^3'))
print(mates.calculo.integrales.integrar('x^3'))

# from mates.calculo import *
# print(test_variable)
