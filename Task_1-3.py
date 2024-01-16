x, y = float(input('Введите 1-ое число: ')), float(input('Введите 2-е число: '))
if y == 0:
    print('Введите новое число, на 0 делить нельзя: ')
    y = float(input('Введите 2-е число: '))
p1, p2, p3, p4, p5 = x+y, x-y, x*y, x/y, x//y
print(p1, p2, p3, p4, p5)   # для поверки значений
print('Второе наибольшее из чисел: ')
max_1, max_2 = 0, 0

if p1 >= p2 and p1 >= p3 and p1 >= p4 and p1 >= p5: max_1 = p1
if p2 >= p1 and p2 >= p3 and p2 >= p4 and p2 >= p5: max_1 = p2
if p3 >= p1 and p3 >= p2 and p3 >= p4 and p3 >= p5: max_1 = p3
if p4 >= p1 and p4 >= p2 and p4 >= p3 and p4 >= p5: max_1 = p4
if p5 >= p1 and p5 >= p2 and p5 >= p3 and p5 >= p4: max_1 = p5

if max_1 == p1:
    if p2 > p3 and p2 > p4 and p2 > p5:
        max_2 = p2
    else:
        if p3 > p4 and p3 > p5:
            max_2 = p3
        else:
            if p4 > p5:
                max_2 = p4
            else: max_2 = p5
if max_1 == p2:
    if p1 >= p3 and p1 >= p4 and p1 >= p5:
        max_2 = p1
    else:
        if p3 >= p4 and p3 >= p5:
            max_2 = p3
        else:
            if p4 >= p5:
                max_2 = p4
            else: max_2 = p5
if max_1 == p3:
    if p1 >= p2 and p1 >= p4 and p1 >= p5:
        max_2 = p1
    else:
        if p2 >= p4 and p2 >= p5:
            max_2 = p2
        else:
            if p4 >= p5:
                max_2 = p4
            else: max_2= p5
if max_1 == p4:
    if p1 >= p2 and p1 >= p3 and p1 >= p5:
        max_2 = p1
    else:
        if p2 >= p3 and p2 >= p5:
            max_2 = p2
        else:
            if p3 >= p5:
                max_2 = p3
            else: max_2 = p5
if max_1 == p5:
    if p1 >= p2 and p1 >= p3 and p1 >= p4:
        max_2 = p1
    else:
        if p2 >= p3 and p2 >= p4:
            max_2 = p2
        else:
            if p3 >= p4:
                max_2 = p3
            else: max_2 = p4

print(max_2)