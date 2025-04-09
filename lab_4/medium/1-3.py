import numpy as np


def create_array(n, m):
    return np.fromfunction(lambda i, j: 0 + i, (n, m), dtype=int)


def chet(arr):
    new_rows = []
    for i in range(arr.shape[0]):
        new_rows.append(arr[i])
        if i % 2 == 1:
            new_rows.append(arr[0])
    return np.vstack(new_rows)


def find_max_element(arr):
    return np.max(arr)


N = int(input("Введите количество строк N: "))
M = int(input("Введите количество столбцов M: "))

array = create_array(N, M)
print("Массив:")
print(array)

# Нахождение макс элемента
print('Максимальный элемент в массиве: ', find_max_element(array))

# Вставка первой строки после каждой чётной строки
print('Вставка: ')
print(f"{chet(array)}")
