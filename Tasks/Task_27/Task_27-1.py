# n = int(input('Введите число: '))
# dct = [[0] * n] * n   # Создание подсписков с нулевыми значениями
# for i in range(n):   # Расположение подсписков в виде массива
#     dct[i] = [0] * n
# #    print(dct[i])
# p = 0
# val = 1
# while (p < n // 2):
#     k = n - p*2 - 1
#     for x in range(k):   # Перемещение по строке x до предпоследней ячейки вправо (сверху)
#         dct[p][p+x] = val
#     for y in range(k):   # Перемещение по строке y до предпоследней ячейки вниз (справа)
#         dct[y+p][n-1-p] = val
#     for x in range(k):   # Перемещение по строке x до предпоследней ячейки влево (внизу)
#         dct[n-1-p][n-1-p-x] = val
#     for y in range(k):   # Перемещение по строке y до предпоследней ячейки вверх (слева)
#         dct[n-1-p-y][p] = val
#     p += 1
#     val += 1
# if n % 2 != 0:   # Условие для заполнения центральной ячейки при нечетных числах
#     dct[p][p] = val
#
# for t in range(n):
#     d = dct[t]
#     print(*d)

def sq_mat(n):
    for i in range(n):
        for j in range(n):
            x = min(i, j, n - 1 - i, n - 1 - j) + 1
            print(x, end=' ')
        print()
sq_mat(7)
