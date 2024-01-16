x, y = int(input('Введите 1-ое число: ')), int(input('Введите 2-е число: '))
if y == 0:
    print('Введите новое число, на 0 делить нельзя: ')
    y = int(input('Введите 2-е число: '))
p1, p2, p3, p4, p5 = x+y, x-y, x*y, x/y, x//y
print(p1, p2, p3, p4, p5)   # для поверки значений
print('Второе наибольшее из чисел:')
if p1 >= p2 and p1 >= p3 and p1 >= p4 and p1 >= p5:
    if p2 >= p3 and p2 >= p4 and p2 >= p5:
        print(p2)
    else:
        if p3 >= p4 and p3 >= p5:
            print(p3)
        else:
            if p4 >= p5:
                print(p4)
            else:
                print(p5)
else:
    if p2 >= p1 and p2 >= p3 and p2 >= p4 and p2 >= p5:
        if p3 >= p1 and p3 >= p4 and p3 >= p5:
            print(p3)
        else:
            if p4 >= p1 and p4 >= p5:
                print(p4)
            else:
                if p1 >= p5:
                    print(p1)
                else:
                    print(p5)
    else:
        if p3 >= p1 and p3 >= p2 and p3 >= p4 and p3 >= p5:
            if p2 >= p1 and p2 >= p4 and p2 >= p5:
                print(p2)
            else:
                if p4 >= p1 and p4 >= p5:
                    print(p4)
                else:
                    if p1 >= p5:
                        print(p1)
                    else:
                        print(p5)
        else:
            if p4 >= p1 and p4 >= p2 and p4 >= p3 and p4 >= p5:
                if p1 >= p2 and p1 >= p3 and p1 >= p5:
                    print(p1)
                else:
                    if p2 >= p3 and p2 >= p5:
                        print(p2)
                    else:
                        if p3 >= p5:
                            print(p3)
                        else:
                            print(p5)
            else:
                if p5 >= p1 and p5 >= p2 and p5 >= p3 and p5 >= p4:
                    if p1 >= p2 and p1 >= p3 and p1 >= p4:
                        print(p1)
                    else:
                        if p2 >= p3 and p2 >= p4:
                            print(p2)
                        else:
                            if p3 >= p4:
                                print(p3)
                            else:
                                print(p4)