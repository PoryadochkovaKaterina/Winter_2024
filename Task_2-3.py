n = int(input('Введите целое положительное число: '))
f1 = 1
if n == 0: print(n, '! = 1', sep = '')
elif n < 0: print('Факториала отрицательного числа не существует')
else:
    for i in range(1, n+1):
        f1 = f1 * i
    print(n, '! = ', f1, sep = '')