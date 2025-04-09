string = input("Введите строку: ")

consonants = "бвгджзйклмнпрстфхцчшщъьБВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ"

i = 0
for sogl in string:
    if sogl in consonants:
        i += 1

# Вывод результата
print("Количество согласных букв:", i)
