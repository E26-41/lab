print("Все числа должны быть целыми")
N = int(input("Введите кол-во членов N: "))
s = 0
for k in range(1, N+1, 1):
    x = 1/((2*k-1)*(2*k+1))
    s += x
print(s)
print("{:.2f}".format(s))

