import math as m
print('Введите исходные данные x, y, z:')
x = float(input('Введите x: '))
y = float(input('Введите y: '))
z = float(input('Введите z: '))
a = (2 * m.cos(x - m.pi / 6)) / (0.5 + m.sin(y) ** 2)
b = 1 + ((z ** 2) / (3 + z ** 2 / 5))
print("{:.2f}".format(a), "{:.2f}".format(b))
