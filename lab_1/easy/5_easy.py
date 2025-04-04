import math as m
# Плотность стали кг/м^3
p = 7850
print('Введите входные данные:')
a = int(input('Длина стороны: '))
angle1 = int(input('1 угол: '))
angle2 = int(input('2 угол: '))
h = int(input('Высота призмы: '))
# По теореме синусов мы находим остальные стороны
b = (a * m.sin(angle1)) / (m.sin(angle1 + angle2))
c = (a * m.sin(angle2)) / (m.sin(angle1 + angle2))
# Угол С можно найти так:
angle3 = 180 - m.fabs(angle1 - angle2)
# Вычислим площадь треугольника по формуле синуса
s = m.fabs(0.5 * a * b * m.sin(angle3))
# Найдём объём призмы
v = s * h
# Определяем площадь поверхности призмы
s_full = 2 * s + (a + b + c) * h
# Определяем массу призмы
m = v * p
print('Площадь поверхности призмы: ', round(s_full, 1), '\n', 'Объём: ', round(v, 1), '\n', 'Масса: ', round(m, 1))
