import array
import random
import math


def arrr(arr):
    s = 1
    for index, x in enumerate(arr):
        if index % 2 == 0 and x > 0:
            s *= x
    return s


def fibonacci(n):
    a, b = 0, 1
    fib = []
    for _ in range(n):
        fib.append(b)
        a, b = b, a + b
    return fib


def pair(arr):
    k = 0
    for index, x in enumerate(arr[:-1]):
        if x > arr[index + 1]:
            k += 1
    return k


def first_min(arr):
    min_f = None
    min_index = -1
    for index, x in enumerate(arr):
        if x % 2 == 0:
            if min_f is None or x < min_f:
                min_f = x
                min_index = index
    return min_f, min_index


def max_in_array(arr):
    max_a = arr[0]
    for x in arr:
        if x > max_a:
            max_a = x
    return max_a


def multiplication(arr):
    array_in_mult = array.array(arr.typecode)
    max_value = max_in_array(arr)
    for index, x in enumerate(arr):
        x += max_value
        array_in_mult.append(x)
    return array_in_mult


print('Всё вводимое должно быть целыми')
n = int(input('Ведите кол-во элементов: '))
# Вводимое с клавиатуры
array_1 = array.array('i', [int(input(f"Элемент {i + 1}: ")) for i in range(n)])

# Случайным образом
array_2 = array.array('i', [random.randint(1, 100) for i in range(n)])

# Генерация по формуле
array_3 = array.array('i', fibonacci(n))

# Пользовательская функция
array_4 = array.array('i', [math.factorial(x) for x in range(1, n+1)])


print("Результат для 1 задачи:")
print(f"1. Ввод с клавиатуры: {arrr(array_1)}; массив {list(array_1)}")
print(f"2. Случайные числа: {arrr(array_2)}; массив {list(array_2)}")
print(f"3. Числа Фибоначчи: {arrr(array_3)}; массив {list(array_3)}")
print(f"4. Факториалы: {arrr(array_4)}; массив {list(array_4)}")

print("###################################################################")
print("Результат для 2 задачи:")
print(f"1. Ввод с клавиатуры: {pair(array_1)}; массив {list(array_1)}")
print(f"2. Случайные числа: {pair(array_2)}; массив {list(array_2)}")
print(f"3. Числа Фибоначчи: {pair(array_3)}; массив {list(array_3)}")
print(f"4. Факториалы: {pair(array_4)}; массив {list(array_4)}")

print("###################################################################")
print("Результат для 3 задачи:")
print(f"1. Ввод с клавиатуры: {first_min(array_1)}; массив {list(array_1)}")
print(f"2. Случайные числа: {first_min(array_2)}; массив {list(array_2)}")
print(f"3. Числа Фибоначчи: {first_min(array_3)}; массив {list(array_3)}")
print(f"4. Факториалы: {first_min(array_4)}; массив {list(array_4)}")

print("###################################################################")
print("Результат для 4 задачи:")
print(f"1. Ввод с клавиатуры: {max_in_array(array_1)}; массив {list(array_1)}; "
      f"обновлённый массив {list(multiplication(array_1))}")
print(f"2. Случайные числа: {max_in_array(array_2)}; массив {list(array_2)}; "
      f"обновлённый массив {list(multiplication(array_2))}")
print(f"3. Числа Фибоначчи: {max_in_array(array_3)}; массив {list(array_3)}; "
      f"обновлённый массив {list(multiplication(array_3))}")
print(f"4. Факториалы: {max_in_array(array_4)}; массив {list(array_4)}; обновлённый массив {list(multiplication(array_4))}")
