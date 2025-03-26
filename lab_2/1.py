print("Все числа должны быть целыми")
a = int(input("Введите начало отрезка a: "))
b = int(input("Введите конец отрезка b: "))
h = int(input("Введите шаг h: "))

for x in range(a, b+1, h):
    y = abs(x**2 - 5*x + 6) - 0.5
    print("значения y: ", "{:.2f}".format(y), "при a = ", x)

print("###############################")

while a <= b:
    y = abs(a ** 2 - 5 * a + 6) - 0.5
    print("значения y: ", "{:.2f}".format(y), "при a = ", a)
    a += h
