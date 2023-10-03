class Person(): # superclase
    def __init__(self, name, surname, age) -> None:
        self.name = name 
        self.surname = surname
        self.age = age	
    
    def __str__(self) -> str:
        return (f'Nombre: {self.name} {self.surname}.'
                f' Edad {self.age} años.')

class Student(Person): # subclase
    # constructor de Alumno, con un parámetro más que Person
    def __init__(self, name, surname, age, course) -> None:
        super().__init__(name, surname, age)
        # también se podría usar Person.__init__, no recomendado
        self.course = course # atributo solo de la subclase
	
    # se redefine el método para incluir el curso
    def __str__(self) -> str:
        return (f'Nombre: {self.name} {self.surname}.'
                f' Edad {self.age} años.'
                f' {self.course}º curso.')

lucia = Person("Lucía", "Ramírez", 54)
print(lucia)
juan = Student("Juan", "López", 18, 2)
print(juan)