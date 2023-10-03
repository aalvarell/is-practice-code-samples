from math import pi

class Geometry(): 
    def get_area(self):
        pass 

class Circle(Geometry):
    def __init__(self, radius) -> None:
        self.radius = radius
    
    def get_area(self): 
         return pi*self.radius**2

class Rectangle(Geometry):
    def __init__(self, side_1, side_2) -> None:
        self.side_1 = side_1
        self.side_2 = side_2

    def get_area(self): 
        return self.side_1*self.side_2

class Square(Rectangle):
    def __init__(self, side) -> None:
        super().__init__(side, side)
