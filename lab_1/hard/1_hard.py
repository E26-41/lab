import math as m
x = int(input('Введите x: '))
if 4 >= x > 0:
    y = (m.fabs(x**2-5*x+6))-0.5
    print(y, 'при', x)
else:
    print('Вы ввели значения вне диапазона')
