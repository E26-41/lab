import numpy as np


def create_array(n, m):
    return np.random.randint(0, 101, size=(n, m))


def find_max_element(arr):
    return np.max(arr)


def find_row_with_min_sum(arr):
    row_sums = np.sum(arr, axis=1)
    min_sum_row_index = np.argmin(row_sums)
    max_elem = int(np.max(arr[min_sum_row_index]))
    row = arr[min_sum_row_index].tolist()
    return row, max_elem


def swap_middle_columns(arr):
    n, m = arr.shape
    if m % 2 != 0:
        print("Число столбцов нечетное, операция невозможна.")
        return arr
    middle = m // 2
    arr[:, [middle - 1, middle]] = arr[:, [middle, middle - 1]]
    return arr


N = int(input("Введите количество строк N: "))
M = int(input("Введите количество столбцов M: "))

array = create_array(N, M)
print("Массив:")
print(array)

# Нахождение макс элемента
print('Максимальный элемент в массиве: ', find_max_element(array))

# Минимальная сумма строки и её макс элемент
print('Строка с минимальной суммой и макс элемент: ', find_row_with_min_sum(array))

# Меняем местами средние части массива
print(swap_middle_columns(array))

