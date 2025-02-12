import math as m

print('Введите исходные данные x, y, z:')
x = float(input('Введите x: '))
y = float(input('Введите y: '))
z = float(input('Введите z: '))
r = str(input('Какая переменная вам нужна a или b:'))

a = (2 * m.cos(x - m.pi / 6)) / (0.5 + m.sin(y) ** 2)
b = 1 + ((z ** 2) / (3 + z ** 2 / 5))

if r == "a":
    print("{:.2f}".format(a))
elif r == "b":
    print("{:.2f}".format(b))
else:
    print('Вы ввели недопустимое значение')
# С match-case аналогично
