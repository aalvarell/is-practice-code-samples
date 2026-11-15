import oo_exercise_module as mod

square_1 = mod.Square(2)
square_2 = mod.Square(3)
circle_1 = mod.Circle(5)
circle_2 = mod.Circle(10)
rectangle_1 = mod.Rectangle(2,3)
rectangle_2 = mod.Rectangle(7,2)

geometries = [square_1, square_2, circle_1, circle_2, rectangle_1, rectangle_2]

area = sum(g.get_area() for g in geometries)

print(f'Area total: {area:.2f}')
