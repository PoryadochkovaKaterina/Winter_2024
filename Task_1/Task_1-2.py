x, y = int(input('Введите 1-ое число: ')), int(input('Введите 2-е число: '))
if y == 0:
    print('Введите новое число, на 0 делить нельзя: ')
    y = int(input('Введите 2-е число: '))
p1, p2, p3, p4, p5 = x+y, x-y, x*y, x/y, x//y
print(p1, p2, p3, p4, p5)   # для поверки значений
print('Наибольшее из чисел:')
max_1 = 0
if p1 >= p2 and p1 >= p3 and p1 >= p4 and p1 >= p5:
    max_1 = p1
if p2 >= p1 and p2 >= p3 and p2 >= p4 and p2 >= p5:
    max_1 = p2
if p3 >= p1 and p3 >= p2 and p3 >= p4 and p3 >= p5:
    max_1 = p3
if p4 >= p1 and p4 >= p2 and p4 >= p3 and p4 >= p5:
    max_1 = p4
if p5 >= p1 and p5 >= p2 and p5 >= p3 and p5 >= p4:
    max_1 = p5
print(max_1)
