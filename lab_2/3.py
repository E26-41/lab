e = float(input("Введите точность e: "))
s = 0
k = 1
while True:
    x = 1/((2*k-1)*(2*k+1))
    if x < e:
        break
    s += x
    k += 1
print(f"Сумма: {s:.2f}, число членов: {k}")
