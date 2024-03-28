# Задача 7-1
# Решение 1
# s = list(map(int, input().split()))
# res = 1
# for k in s: res *= k
# for n in range(res, 0, -1):
#     for m in s:
#         if n % m: break
#     else:
#         nok = n
# print(nok)
# import math
# Решение 2
# s = list(map(int, input().split()))
# def nod(a, b):
#     while a != 0 and b != 0:
#         if a > b:
#             a = a % b
#         else:
#             b = b % a
#     return a + b
# def nok(a, b):
#     return a * b // nod(a, b)
#
# x = 1
# for i in s:
#     x = nok(x, i)
# print(x)

# Задача 7-2
# def code(string, n):
#     res = ''
#     for i in string:
#         n_ord = ord(i) + n
#         if chr(ord('a')) <= i <= (chr(ord('a')) + 25):
#             n_ord = ord('a') + (n_ord - ord('a')) % 26
#             res += chr(n_ord)
#         elif chr(ord('A')) <= i <= (chr(ord('A')) + 25):
#             n_ord = ord('A') + (n_ord - ord('A')) % 26
#             res += chr(n_ord)
#         else:
#             res += i
#     return res
# st = str(input())
# numb = int(input())
# print(code(st, numb))

# Задача 7-3
# lst = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# res = []
# for i in lst:
#     for j in i:
#         res.append(j)
# print(res)
# a = sorted(res)
# print(a[-3:])

# ZIP создание кортежей из разных итереиблов
# REVERSED - переворачивание списка или срез -1
# FILTER - выдает только те элементы, которые возвращают True (0 - False, остальное - True)
# print(list(filter(bool, [0, 1, 2])))

# def chet(x):
#     if x % 2 == 0: return True   # Для четных чисел возвращает True
#     return False   # Для остальных чисел возвращает False
# print(list(filter(chet, [0, 1, 2, 3, 4, 5, 6, 7])))

# ANY - все ли логические выражение True
# ALL

# print(any((True, False, False)))
# print(all((True, True, False)))

# MAP
# s = list(map(int, input().split()))
# for i in map(int, input().split()):
#     print(i)

# k = 123
# print(sum(map(int, list(str(k)))))

# Модуль - фаил содержащий код на Python
# Каждый модуль в Python может содержать переменные, объявления классов и функций
# В модуле находиться исполняемый код

# import module_1[, module_2[,... module_N]]

# Модуль загружается однажды

# import math
# print(math.sqrt(9))
# print(math.pi)
#
# from math import sqrt, pi   # Можно импортировать отдельные функции
# print(sqrt(9), pi)

# from math import *   # Если необходимы все функции
# print(sqrt(9), pi, e)

# # Название программы test_a
# print('++++ test_a')
# from test_b import *
# func_test_b
# if __name__ ** '__main__':
#     print('++++ test_a', __name__)
#
# # Название программы test_b
# print('++++ test_b')
# def func_test_b():
#     print('++++ func_test_b')
# if __name__ ** '__main__':
#     print('++++ test_b', __name__)

# НОК через функцию math.lcm
# from math import lcm
# a, b = map(int, input().split())
# nok = math.lcm(a, b)
# print(nok)
# print(math.lcm(a, b))

# from math import pi
# def s_cir(r):
#     s_cir = pi * (r ** 2)
#     return s_cir
# print(s_cir(float(input())))

# SORTED - отсортированный список
# print(sorted([1, -2, 3, -4, 5]))
# print(sorted([1, -2, 3, -4, 5], key=abs))

# 1 - ключ 1, -2 - ключ 2, 3 - ключ 3 и т.д.
# def minus_abs(x):
#     return -abs(x)
# print(sorted([1, -2, 3, -4, 5], key = minus_abs))

# t = [(1, 2), (0, 2), (1, 1), (0, 0), (0, 1), (1, 0)]
# print(sorted(t))
# print(sorted(t, reverse=True))

# def sotr_t(x):
#     return x[1], x[0]   # Сортировка по второму элементу, а потом по второму
# print(sorted(t, key=sotr_t))

# def sort_t(x):
#     return x[0]+x[1]   # Сортировка по сумме кортежей 1 и 2 элемента
# print(sorted(t, key=sort_t))

# def sort_t(x):
#     return x[0]*x[1]   # Сортировка по произведению кортежей 1 и 2 элемента
# print(sorted(t, key=sort_t))

# def sort_t(x):
#     return x[0], x[1]   # Сортировка по возрастанию кортежей 1 и 2 элемента
# print(sorted(t, key=sort_t))

# def sort_t(x):
#     return x[0]*x[1]   # Сортировка по произведению кортежей 1 и 2 элемента
# print(sorted(t, key=sort_t))

# def sort_t(x):
#     return (x[0] + x[1]) % 2, x[0]   # Сортировка по четности, потом по первому элементу кортежей 1 и 2 элемента
# print(sorted(t, key=sort_t))

# p = [123, 3, 33, 231, 1, 11, 120, 345, 762]
# def sort_p(x):
#     return x % 10, x   # сортировка по последней числе и по возрастания числа внутри группы
# print(sorted(p, key = sort_p))

# def sort_p(x):
#     return x % 10    # сортировка по последнему числу
# print(sorted(p, key = sort_p, reverse = True))
# print(sorted(p, key = sort_p)[::-1])

# sorted(iterable, key=None, reverse=False)
# reverse = True - обратный порядок
# reverse = False - по умолчанию

# EVAL EXEC
# EVAL - (оценка, вычисление
# x = 5
# print(eval('12 + 36'))
# print(eval('x + 36'))
# print(eval('divmod(x,2)'))

# y = 6
# stroka = '"y" + " + " + "12"'   # Контактинация строк
# print(eval(stroka))

# EXEC - выполнение, лучше не использовать
# a = 'x = 5'
# # print(x)   # ошибка, значению x еще ничего не присвоено
# exec(a)   # присваивается x - присвоить значение
# print(x)
# b = 'print(x)'
# exec(b)
# exec('''   # программа пишет программу
# for i in range(5):
#     print(i)
# ''')

# capitalize - первая буква строки верхняя, остальные нижние
# title - каждая первая буква слова верхняя, остальные нижняя

# s = 'All you need is love'
# if s.find('Hello') == -1:
#     print('No')
# print(s.index('love'))

# txt = 'i like bananas'
# x = txt.replace('bananas', 'apple')
# print(x)
#
# y = txt.replace('a', 'o', 2)
# print(y)

# s = 'I like bananas'
# z = s.split()
# print('__'.join(z))   # Значения добавляются только между
# print('-'.join('abc-xyz-fgh'.split('-')))

# txt = ',,,,,rrggee....banana////rrrr'
# x = txt.strip(',r/a')   # удаление всех символов узананных в параметрах
# print(x)

# a = '   gfyujhv   ' * 3   # Повторение строки
# print(a)

# a = 'gfyujhv'
# print(a.partition('yu'))   # деление строки до указанных элементов, на указанные элементы и после указанных элементов

# a = 'gfyujhv'
# print(a.center(15, '*'))   # помещение строки в центр и добавление недостающих элементов, по указанному кол-ву

# a = 'gfyujghv'
# print(a.count('g'))   # кол-во вхождение в строку указанного элемента

# st = str(input())
# dct = {}
# for i in st:
#     dct[i] = dct.get(i, 0) + 1
# ma_l, ma_hm = '', 0
# for i in dct:
#     if dct[i] > ma_hm:
#         ma_l = i
#         ma_hm = dct[i]
# print(ma_l, dct[ma_l])
# # n = int(input())

# lambda - однострочная анонимная функция
# def fun(x):
#     return x % 10
# sp = [223, 12, 1, 111, 21, 322]
# # print(sorted(sp, key=fun))
# print(sorted(sp, key=lambda x: (x % 2, x)))

