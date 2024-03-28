# a = [1, 2, 3, 4]
# b = a   # b будет таки же как и a
# a = a + [5, 6, 7, 8]   # сложение с другим списком, но b не меняется
# # когда a = a + ..., то порождается новый список, и b остается прежним
#
# c = [1, 2, 3, 4]
# d = c
# c += [5, 6, 7, 8]   # c увеличивается на ..., но b меняется
# # когда += новый элемент не создается, c ссылается на то, что уже есть и появлсяется новый d и с
# print(a)
# print(b)
# print(c)
# print(d)
# import asyncio
# Задача 11-1
# from datetime import date
# for i in range(1, 13):
#     c = 0
#     for j in range(1, 29):
#         if date(2024, i, j).weekday() == 3:
#             c += 1
#             if c == 3:
#                 print(date(2024, i, j).strftime('%d.%m.%Y'))
#                 break

# Задача 11-2
# import openpyxl
# with open('...') as f:
#     lst = []
#     for i in f:
#         lst.append(i.strip().split(','))
#
# wb = openpyxl.load_workbook('...')
# if 'Sheet' not in wb.sheetnames:
#     wb.create_sheet('Sheet')
# ws = wb['Sheet']
# for i in range(1, ws.max_row + 1):
#     for j in range(1, ws.max_column + 1):
#         ws.cell(i, j).value = None
#
# lst_sor = sorted(lst, key=lambda x: (x[3], x[1], x[2]))
# total = 0
# for i, j in enumerate(lst_sor, 1):
#     for k in range(5):
#         if j[k].isdigit():   # для перевода в числа
#             ws.cell(i, k+1).value = int(j[k])
#         else:
#             ws.cell(i, k + 1).value = j[k]
#
#     total += int(j[4])
#
# ws.cell(i+1, 2).value = 'ИТОГО'
# ws.cell(i+1, 5).value = total
#
# ws.save('...')

# Задача 11-3   # НЕ РАБОТАЕТ, ПРОВЕРИТЬ, ЧТО БЫЛО НА ЗАНЯТИИ
# dict = {1000: 'M', 900: 'CM', 500: 'D', 400:'CD',
#         100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
#         10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
# def rim(x):
#     res = ''
#     while x > 0:
#         for i in dict:
#             if x >= 1:
#                 res += dict[i]
#                 x -= i
#                 break
#     return res
#
# print(rim(int(input())))
#
# def rim_2(x):
#     res = ''
#     for i in dict:
#         while x > 0 and x >= i:
#             res += dict[i]
#             x -= i
#     return res
#
# print(rim(int(input())))

# import time, math
# t0 = time.time()
# for i in range(1, 10000, 100):
#     s = 0
#     for j in range(1, i):
#         s += math.factorial(j)
#     t1 = time.time()   # с каким временем проходят интерации
#     print(i, t1-t0)

# import datetime, locale
# locale.setlocale(locale.LC_ALL, 'ru')   # Перевод на нужный язык
# a = datetime.datetime.today() + datetime.timedelta(days=14)   # Текущая дата +14 дней
# print(a)
# c = datetime.timedelta(days=1)   # дата + 1 день
# for _ in range(10):
#     a += c
#     print(a.strftime('%A %d, %B %Y'))   # вывод дня недели, числа, месяца, года через день


# from datetime import datetime
# print(datetime.strptime('09 02 2024 19:20', '%d %m %Y %H:%M'))

# Печать месяца календаря в виде кортежа в одну строку
# import calendar
# year, mon = tuple(map(int, input().split()))
# print(calendar.monthcalendar(year, mon))

# import itertools
# for i in itertools.chain('abc', [1, 2, 3, 4]):   # Последовательная печать всех существуеющих элементов
#     print(i)
#
# for i in itertools.chain('abcd', [1, 2, 3, 4], (11, 12, 13, 14, 15), {1:11, 2:12, 3:13}, (True, False, None)):
#     print(i, end='')

# a = [1, 2, 3]
# b = 'abcde'
# for k in zip(a, b):  # Попарное объединение, самое краткое
#     print(k)

# максимальное попарное объединение, если элемента нет, то заменяется на None
# если указать fillvalue, то заменается на указанный символ
# Работа по максимальному итереиблу
# from itertools import zip_longest
# for k in zip_longest(a, b, fillvalue='*'):
#     print(k)

# Функция flip_flop. Если flip - flop, если flop, то flip
# def fl_fl(x):
#     return 'flip' if x == 'flop' else 'flip'   # тернальный оператор для flip flop flip flop
#     # return 5 - x   # для вывода 3232323232
#     # return - x   # для вывода -2 2 -2 2 -2 2 -2 2
#
#     # if x == 'flop':   # Замена тернального оператора
#     #     return 'flip'
#     # else:
#     #     return 'flop'
#
# x = 'flip'
# # x = 2
# for i in range(10):   # попарный перебор
#     x = fl_fl(x)
#     print(x)

# Списковое включение (LIST COMPREHENSION)
# применение выражения к каждому элементу последовательности
# lst = [x ** 2 for x in range(10) if x % 2 == 0]   # квадраты всех четных чисел
# print(lst)
# для начало выражение, потом цикл, потом можно условие, можно без условия
# что хотим, в каком цикле, на основании какого условия

# Способы формирования списков
# 1. при помощи циклов
# 2. при помощи map
# 3. при помощи list comprehension

# Примеры
# lst_1 = []
# for i in range(10):
#     lst_1.append(i ** 2)
# print(lst_1)
#
# lst_2 = list(map(lambda x: x ** 2, range(10)))
# print(lst_2)
#
# lst_3 = [x ** 2 for x in range(10)]
# print(lst_3)

# Список четных чисел до 20 включительно
# lst = [x for x in range(20+1) if x % 2 == 0]   # с условием
# lst_1 = [x * 2 for x in range(20+1)]   # без условия
# print(lst)

# в конце может быть условие без ELSE,
# но условие можно включить в начало (перед циклом)
# если четное, то квадрат, если не четное, то куб
# lst = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(10)]
# print(lst)

# from string import ascii_letters
# letters = 'sbвeаrуfцvаsпкуbg'   # набор букв из разных алфавитов
# # разграничиваем буквы на английские и не английские буквы
# is_eng = [f'{let} - ДА' if let in ascii_letters else f'{let} - НЕТ' for let in letters]
# # через цикл в конце, проверяет побуквенно всё выражение
# # выводит ДА, если буква входит в ascii_letters
# # выводит НЕТ, если буква не входит в ascii_letters
# print(is_eng)

# import string
# gla = 'aeiouAEIOU'
# str = str(input())
# lst = [s for s in str if s in gla]
# lst_1 = [s for s in str if s.lower() in 'aoeiu']
# lst_2 = {s for s in str if s.lower() in 'aoeiu'}   # за счет скобок можно заменить set
# print(set(lst))
# print(lst_1)
# print(lst_2)

# # Замена отрицательных чисел на 0
# orig_pr = [1.25, -6.45, 10.22, 3.78, -5.92, 1.16]
# def get_pr(price):
#     return price if price > 0 else 0
# prices = [get_pr(i) for i in orig_pr]
# print(prices)
#
# res = [x if x >= 0 else 0 for x in orig_pr]
# print(res)

# Написать программа FizzBuzz, если на 3 и 5, то FB, если на 3, то F, если на 5, то B
# res = ['FB' if x % 15 == 0 else 'F' if x % 3 == 0 else 'B' if x % 5 == 0 else x for x in range(31)]
# print(*res)
#
# def fu(x):
#     return 'FB' if x % 15 == 0 else 'F' if x % 3 == 0 else 'B' if x % 5 == 0 else x
# a = [fu(x) for x in range(31)]
# print(*a)
#
# res = []
# for i in range(31):
#     if i % 15 == 0:
#         res.append('FB')
#     elif i % 3 == 0:
#         res.append('F')
#     elif i % 5 == 0:
#         res.append('B')
#     else:
#         res.append(i)
# print(*res)


# Вложенная генерация
# Представление списка из слов, который мы хотим привести к сплошному списку букв.
# Двойная интерация: по словам и по буквам
# str = ['To', 'be', 'or', 'not', 'to', 'be']
# res = [sim   for word in str   for sim in word]
# # каждый символ для каждого слова, для каждого символа в каждом слове
# print(*res)
#
# res_1 = []
# for word in str:
#     for sim in word:
#         res_1.append(sim)
# print(*res_1)


# key = ['name', 'age', 'weight']
# val = ['Lili', 25, 100]
#
# lst = [{x, y} for x in key for y in val]  # скобки {} показывают, что создается список из множеств
# lst_2 = [{x: y} for x in key for y in val]
# lst_3 = [[x, y] for x in key for y in val]
# lst_4 = [(x, y) for x in key for y in val]
# print(lst)
# print(lst_2)
# print(lst_3)
# print(lst_4)
#
# lst_1 = []
# for x in key:
#     for y in val:
#         lst_1.append({x, y})
# print(lst_1)

# Вложенная генерация для матриц
# matr = [[i for i in range(5)] for j in range(6)]
# print(matr)
# внутренний цикл заполняет строку значениями, а внешний указывает на количество строк
#
# matr_1 = [[i+j for i in range(5)] for j in range(7)]
# matr_2 = [[i*j for i in range(5)] for j in range(7)]
# for s in matr_2:
#     print(s)

#  Преобразование матрицы в плоский вид
# mat = [[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]]
# f = [num for row in mat for num in row]
# # Возвращаем число из матрица через цикл, который берет для начала строку из матрицы, а потом значение из строки
# print(f)

# Таблица умножения
# t = [[x * y for x in range(1, 10)] for y in range(1, 10)]
# for s in t:
#     print(*s)

# Для модификации
# Для увелечения производительности
# Для компактности
# Если можете прочесть, то использовать можно

# Написать программы спискового включения, которое работает аналогично
# lst = list(map(int, input().split()))
# print(lst)
#
# lst_1 = [int(x) for x in input().split()]
# print(lst_1)


# # Списковое включение
# a = [x for x in range(1000)]
# # Квадратные скобки, все объекты генерируются сразу
#
# # Генераторное выражение
# b = (i for i in range(1000))   # Выдает число за числом
# # Круглые скобки, это не кортеж, все объеты генерируются по запросу
#
# # for y in b:
# #     print(y)
#
# print(type(a))
# print(type(b))
#
# import sys
# print(sys.getsizeof(a))   # размеры объектов
# print(sys.getsizeof(b))   # размеры объектов


# Генерация словаря
# d = {k: k ** 2 for k in range(1, 11)}   # Генерация словаря для квадрата чисел до 10
# print(d)

# Создание словаря по списку кортежей
# items = [('a', 11), ('b', 22), ('c', 33), ('d', 44)]
# dic = {k: v for (k, v) in items}
# print(dic)
# если убрать :v, то получается множество из ключей


# lst = [('a', 1), ('b', 5), ('c', 2), ('d', 6)]
# filt = {k: v for (k, v) in lst if v % 2}
# print(filt)

# lst = {'a': 1, 'b': 5, 'c': 2, 'd': 6}
# x = lst.items()   # items меняется, после внесения в него нового значения без повторого вызова
# print(x)
# lst['e'] = 9
# print(x)

