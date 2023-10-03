class Person():
    people_created = 0

    def __init__(self, name, surname, age) -> None:
        self.name = name 
        self.surname = surname
        self.age = age
        self._id = type(self).people_created
        # atributo privado usando name mangling
        self.__alt_id = type(self).people_created
        
        type(self).people_created += 1
    
    def __str__(self) -> str:
        return (f'Nombre: {self.name} {self.surname}.'
                f' Edad {self.age} años.')

pepe = Person('Pepe', 'López', 55)
print(vars(pepe)) # muestra los miembros del objeto
# podemos acceder a un atributo privado normal
print(f'{pepe._id} --> {pepe}')
# pero al usar name mangling "se oculta" el atributo
print(f'{pepe.__alt_id} --> {pepe}')
