import numpy as np


def find_max_element(arr):
    return np.max(arr)


with open("data1.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()


N = int(lines[0].strip())
M = int(lines[1].strip())
array = np.zeros((N, M), dtype=int)

for i in range(N):
    row_data = lines[i + 2].strip().split()
    for j in range(N):
        array[i, j] = int(row_data[j])

print("Массив:")
print(array)

print('Максимальный элемент в массиве: ', find_max_element(array))
