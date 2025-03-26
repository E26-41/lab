import math as m


def piecedef(a, b, x):
    if x <= -4:
        y = a * m.cos(a + m.pi * x)
    elif -4 < x <= 4:
        y = abs(a - b * m.e ** (a * x) + 3)
    elif x > 4:
        y = x - 4
    return y


for x in range(-5, 6, 1):
    y = piecedef(3, 4, x)
    print(f"Значение y: {y:.2f}, при x: {x}")
