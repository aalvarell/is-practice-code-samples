import oo_exercise_module as mod

s_1 = mod.Square(2)
s_2 = mod.Square(3)
c_1 = mod.Circle(5)
c_2 = mod.Circle(10)
r_1 = mod.Rectangle(2,3)
r_2 = mod.Rectangle(7,2)

geometries = [s_1, s_2, c_1, c_2, r_1, r_2]
area = sum(g.get_area() for g in geometries)
print(f'Area total: {area}')
