sum_1, sum_2, n = 0, 0, 1
while True: # Бесконечный цикл из которого надо обязательно выйти
    x = int(input(f'Введите зарплату сотрудника {n}: '))
    n += 1
    if x < 0:
        print('Зарплата не может быть отрицательной!')
        continue
    elif x == 0: break
    else:
        sum_1 += x
        sum_2 += 1
print(sum_1, sum_2)
print(f'Средняя зарплаты сотрудников: {sum_1/sum_2}')