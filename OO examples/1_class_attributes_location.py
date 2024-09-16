class Person():
    # atributo de clase: se define al nivel de clase, fuera del constructor
    people_created = 0

    def __init__(self, name, surname, age) -> None:
        # atributos de instancia: se crean en el constructor
        self.name = name 
        self.surname = surname
        self.age = age
        # podemos modificar un atributo de clase referenciando la clase
        # Person.people_created += 1
        # también se puede hacer "más genérico"
        # así no escribimos el mombre de la clase:
        type(self).people_created += 1
    
    def __str__(self) -> str: # método
        return (f'Nombre: {self.name} {self.surname}.'
                f' Edad {self.age} años.')

pepe = Person('Pepe', 'López', 55)  # creamos un objeto
ana = Person('Ana', 'Rodríguez', 33)  # creamos otro objeto
# cada objeto tiene sus propios atributos de instancia
print(pepe)
print(ana)
# todos los objetos comparten los atributos de clase
print(pepe.people_created)
print(ana.people_created)