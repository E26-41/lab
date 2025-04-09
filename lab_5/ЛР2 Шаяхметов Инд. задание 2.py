with open("data0.txt", "r", encoding="utf-8") as file:
    content = file.read()

num = {
    '0': 'ноль',
    '1': 'один',
    '2': 'два',
    '3': 'три',
    '4': 'четыре',
    '5': 'пять',
}

new_content = []
for char in content:
    if char in num:
        new_content.append(num[char])
    else:
        new_content.append(char)

new_content = ''.join(new_content)
# Вывод результата
print("Результат замены:")
print(new_content)

with open("data.txt", "w", encoding="utf-8") as file:
    file.write(new_content)
