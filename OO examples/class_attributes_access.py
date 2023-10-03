class Person():
    people_created = 0 # atributo de clase público

    def __init__(self, name, surname, age) -> None:
        # atributos de instancia públicos
        self.name = name 
        self.surname = surname
        self.age = age
        # atributo de instancia privado: usamos el orden 
        # de creación como identificador de la persona
        self._id = type(self).people_created
        
        type(self).people_created += 1
    
    def __str__(self) -> str: # método
        return (f'Nombre: {self.name} {self.surname}.'
                f' Edad {self.age} años.')
    
    # para acceder a miembros privados se suele usar un "getter”
    def get_id(self) -> str:
        return self._id

pepe = Person('Pepe', 'López', 55)  # creamos un objeto
ana = Person('Ana', 'Rodríguez', 33)  # creamos otro objeto
print(f'{pepe.get_id()} --> {pepe}')
print(f'{ana.get_id()} --> {ana}')