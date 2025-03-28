import math as m


def check_point(r, x, y):
    """
    Для начала находим гипотенузу нашей точки, а дальше находим стороны нашего радиуса

    """
    g = m.sqrt((x ** 2 + y ** 2))
    a = r * m.cos(45)
    b = r * m.sin(45)
    if g > r:
        print('Точка вне окружности')
    elif m.fabs(x) > a or m.fabs(y) > b:
        print('Точка вне окружности')
    else:
        print('Вы попали')


r = float(input('Введите радиус окружности: '))
x = float(input('Введите x: '))
y = float(input('Введите y: '))
check_point(r, x, y)
