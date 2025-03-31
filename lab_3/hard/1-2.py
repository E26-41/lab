import array
import random
import math


def fibonacci(n):
    a, b = 0, 1
    fib = []
    for _ in range(n):
        fib.append(b)
        a, b = b, a + b
    return fib


def last_num(arr):
    new_array = array.array(arr.typecode)
    for x in arr:
        if (abs(x) % 10) % 2 == 0:
            new_array.append(x)
    return new_array


def k(arr, k_):
    new_array = array.array(arr.typecode)
    for x in arr:
        if (abs(x) % 10) == 1:
            new_value = int(f"{k_}{abs(x)}") * (-1 if x < 0 else 1)
            new_array.append(new_value)
        else:
            new_array.append(x)
    return new_array


print('Всё вводимое должно быть целыми')
n = int(input('Ведите кол-во элементов: '))
k_ = int(input('Ведите K: '))
# Вводимое с клавиатуры
array_1 = array.array('i', [int(input(f"Элемент {i + 1}: ")) for i in range(n)])

# Случайным образом
array_2 = array.array('i', [random.randint(1, 100) for i in range(n)])

# Генерация по формуле
array_3 = array.array('i', fibonacci(n))

# Пользовательская функция
array_4 = array.array('i', [math.factorial(x) for x in range(1, n + 1)])

print("Результат для 1 задачи:")
print(f"1. Ввод с клавиатуры: {list(last_num(array_1))}; массив {list(array_1)}")
print(f"2. Случайные числа: {list(last_num(array_2))}; массив {list(array_2)}")
print(f"3. Числа Фибоначчи: {list(last_num(array_3))}; массив {list(array_3)}")
print(f"4. Факториалы: {list(last_num(array_4))}; массив {list(array_4)}")

print("###################################################################")
print("Результат для 2 задачи:")
print(f"1. Ввод с клавиатуры: {list(k(array_1, k_))}; массив {list(array_1)}")
print(f"2. Случайные числа: {list(k(array_2, k_))}; массив {list(array_2)}")
print(f"3. Числа Фибоначчи: {list(k(array_3, k_))}; массив {list(array_3)}")
print(f"4. Факториалы: {list(k(array_4, k_))}; массив {list(array_4)}")
