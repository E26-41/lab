import numpy as np


def create_array(n, m):
    return np.random.randint(0, 101, size=(n, m))


def remove(arr):
    return arr[~np.any(arr == 0, axis=1)]


def symmetry(arr):
    if np.array_equal(arr, arr.T):
        return '\n'"Матрица симметрична"
    else:
        arr[:] = np.min(arr)
        return '\n'"Матрица не симметрична и все элементы заменены на минимальное значение"


N = int(input("Введите количество строк N: "))
M = int(input("Введите количество столбцов M: "))

array = create_array(N, M)
print("Массив:")
print(array)

# Удаление строк с нулем
print('\nБез нулей:')
print(f"{remove(array)}")

# Проверка на симметричность
print(symmetry(array))
print(array)

# Для проверки симметрии по главной диагонали
A = np.array([[1, 2, 3],
              [2, 5, 6],
              [3, 6, 9]])
print(symmetry(A))
print("Результат:\n", A)
