import math as m


print("Все числа должны быть целыми")
N = int(input("Введите кол-во членов N: "))
s = 0
for k in range(1, N+1, 1):
    x = (k ** 5) / (2 * m.factorial(2 * k))
    s += x
print(s)
print("{:.2f}".format(s))
