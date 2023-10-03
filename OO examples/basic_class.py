class Person(): # clase
    def __init__(self, name, surname, age) -> None: # constructor
        self.name = name # atributo
        self.surname = surname # atributo
        self.age = age # atributo
    
    def __str__(self) -> str: # método
        return (f'Nombre: {self.name} {self.surname}.'
                f' Edad {self.age} años.')
		
pepe = Person('Pepe', 'López', 55)  # creamos un objeto
ana = Person('Ana', 'Rodríguez', 33)  # creamos otro objeto

# al usar print con un objeto llama 
# al método __str__ para imprimir el objeto
print(pepe)
print(ana)