print('Координаты должны быть с запятой')
x = float(input('Введите x: '))
y = float(input('Введите y: '))
if 0.52 <= x <= 2.62 and 0 <= y <= 0.5:
    print('Координата входит в закрашенную область')
else:
    print('Координата не входит в закрашенную область')
