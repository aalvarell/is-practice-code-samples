class Person():
    __people_created = 0

    def __init__(self, name, surname, age) -> None: # constructor
        self.name = name 
        self.surname = surname
        self.age = age    
        type(self).__people_created += 1
    
    def say_hi(self) -> str: # metodo de instancia
        print(f'Hola, mi nombre es {self.name} {self.surname}.')

    @classmethod # método de clase
    def get_people_created(cls) -> int:
        return cls.__people_created
    
    @staticmethod # método estático
    def print_header(times:int) -> None:
        print('-'*times)

pepe = Person('Íñigo', 'Montoya', 55)
# método estático (se llama desde la clase/instancia)
Person.print_header(35) 
# método de isntancia (se llama desde la instancia)
pepe.say_hi()
 # método estático llamado desde la instancia
pepe.print_header(35)
# método de clase (se llama desde la clase/instancia)
print(Person.get_people_created())
print(pepe.get_people_created())
