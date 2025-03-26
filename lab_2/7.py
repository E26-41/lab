import math as m


N = int(input("Введите кол-во членов N: "))
e = float(input("Введите точность e: "))
s = 0
k = 1
while True:
    x = (k ** 5) / (2 * m.factorial(2 * k))
    if x < e:
        break
    s += x
    k += 1
print(f"Сумма: {s:.2f}, число членов: {k}")
