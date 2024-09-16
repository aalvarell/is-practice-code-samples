from dataclasses import dataclass

@dataclass  # decorador
class Person():
    name: str
    surname: str
    age: int

pepe = Person('Pepe', 'López', 55)
ana = Person('Ana', 'Rodríguez', 33)

# al usar print con un objeto llama al método __str__
# para imprimir el objeto. Python lo creó por nosotros
print(pepe)
print(ana)
