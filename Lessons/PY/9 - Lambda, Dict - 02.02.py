# Задача 8-1
# s = list(input())
# i = 0
# while i < len(s) - 1:
#     if s[i] + s[i + 1] in "АГА":
#         s[i], s[i + 1] = s[i + 1], s[i]
#         i += 1
#     elif s[i] + s[i + 1] in 'ТЦТ':
#         s.insert(i + 1, 'АГ')
#         i += 2
#     i += 1
# print(''.join(s))

# Задача 8-2
# ldt = [[1, 5, 3], [2, 44, 1, 4], [3, 33333]]
# def digits(ldt):
#     res = 0
#     for i in ldt:
#         res += len(str(i))
#     return res
# new_lst = sorted(ldt, key = digits)
# print(new_lst)
# res = []
# for i in new_lst:
#     res.append(sorted(i, reverse = True))
# print(res)

# Задача 8-3
# lst = ['abab', 'xx', 'aaaaaaaaa', 'yy', 'abcbab']
# print(sorted(lst, key=lambda x: (-len(set(x)), x)))

# print((lambda x: x * x)(12))

# Печать квадрата чисел от 0 до 9, через lambda
# print(*list(map(lambda x: x*x, range(10))))   # * Распаковывает список, без скобок, только его значения

# Та же самая задача, но без lambda
# def kva(x):
#     return x*x
# # print(*list(map(kva, range(10))))
# for i in map(kva, range(10)):
#     print(i, end=' ')

# Lambda функцию можно наименовать
# kva = lambda x: x * x
# print(*list(map(kva, range(10))))

# fun = lambda x, y, *args, **kwargs: x + y
# print(fun('abc', 'def'))

# fu = lambda x: (x.lower()[::2])
# print(fu('ABCDDFabcdfe'))

# Список целых чисел по возрастанию. сначала четные
# lst = [1, 4, 3, 2, 5, 4, 7, 9, 0, 5]
# print(sorted(lst, key=lambda x: x % 2))

# Список слов независимо от регистра
# print(sorted(['x', 'a', 'A', 'X', 'B', 'b'], key=lambda x: (x.upper(), x)))

# y = 16
# lst = [1, 10, 21, 30]
# print(min(lst, key=lambda x: abs(x - y)))

# Лямбда-выражения как элементы кортежей
# Формируется кортеж, в котором элементы являются lambda-функцией считающей выражения
# import random
# T = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
# for t in T:
#     print(t('abc'))
#
# T = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
# y = 'abc'
# for t in T:
#     print(t(y))

# Использование лямбда-выражения для формирования словаря функции
# def rand():
#     print('****')
#
# dict = {
#     1: (lambda: print('Monday')),
#     2: (lambda: print('Tuesday')),
#     3: (lambda: print('Wednesday')),
#     4: (lambda: print('Thursday')),
#     5: (lambda: print('Friday')),
#     6: rand   # Вызов функции в словаре
# }
# print(dict[1]())

# Если убрать == после x % 2, то будут считаться нечетные числа
# Лямбда выдается либо True, либо False
# numb = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(filter(lambda x: x % 2, numb)))

# lst = [123, 234, 345, 456]
# print(list(map(lambda x: sum(map(int, list(str(x)))), lst)))

# Работа программы
# 123
# str(123) -> '123'
# list(str(123)) -> ['1', '2', '3']
# map(int, list(str(123))) -> [1, 2, 3]
# sum(map(int, list(str(123)))) -> 6

# Сортировка списка по первой цифре каждого элемента
# sp = [222, 31, 1, 711, 82, 322]
# print(sorted(sp, key=lambda x: int(str(x)[0])))

# Тернальный оператор
# x = 1
# y = 2
# maximum = x if y > y else y   # Это x если x больше y
# print(maximum)

# В lambda нельзя использовать if, else, for, но можно Тернарный оператор
# low = (lambda x, y: x if x < y else y)
# print((lambda x, y: x if x < y else y)(10,3))
# print(low(10,3))

# Подоходный налог, более 5000000 налог 15%, менее 5000000 налог 13%
# print((lambda d, lim: d * 0.13 if d <= lim else lim * 0.13 + (d - lim) * 0.15)(5000100, 5000000))

# lst = [('Иванов', 100), ('Петров', 300),
#         ('Сидоров', 200), ('Воробьев', 100),
#         ('Лунин', 200)]
# print(sorted(lst, key=lambda x: (-x[1], x[0])))

# Вложенные словари
# Ключами словаря могут быть ЧИСЛА, СТРОКИ, КОРТЕЖИ, True, False
# Значениями VALUE может быть всё, что угодно: ЧИСЛА, СТРОКИ, КОРТЕЖИ, СПИСКИ, МНОЖЕСТВА, ФУНКЦИИ и т.д.
# a = {True: abs,
#      False: lambda x: x*x,
#      3: {1, 2, 3},
#      '1': [1, 2],
#      'Город': 'Москва'}
# print(a[True](-123))
# print(a[False](5))

# stud = {0: {'name': 'Иванов', 'age': 22},
#         1: {'name': 'Петров', 'age': 24},
#         2: {'name': 'Сидоров', 'age': 26}}
# # print(stud[0])
# # print(stud[0]['name'])
# # print(stud[2]['age'])
# # Для обращения к жлементам внутренних словарей нужны 2 ключа
# # Печать всех ключей и значений всех словарей
# for i in stud:
#     # print(i, stud[i])
#     for j in stud[i]:
#         print(j, stud[i][j])

# stud = {1: 123,
#         2: 234,
#         3: {1: 111, 2: 222},
#         4: {1: 'abc', 2: 'def'}}
# x = 1
# for i in stud:
#     print(i, stud[i])
#     if stud[i] == type(dict):
#         for j in stud[i]:
#             print(j, stud[i][j])
# for k, v in stud.items():
#     if k == x:
#         print(v)
#     if type(v) == dict:
#         for a, b in v.items():
#             if a == x:
#                 print(b)

# TXT
# С файлом можно: открыть, прочитать, дописать, переписать, закрыть
# После того как сделали всю необходимую работу - его следует закрыть

# Открытие - Закрытие файла
# f = open('File/text.txt', encoding='utf-8')
# f.close()

# Запись в файл. Обязательный атрибут 'w'
# f = open('File/text.txt', 'w', encoding='utf-8')
# for i in range(5):
#     s = input()
#     print(s, file = f)
# f.close()

# Чтение данных из файла
# f = open('File/text.txt', encoding='utf-8')
# s = f.readlines()
# for i in s:
#     print(i.strip())
# f.close()

# Чтение файлом самого себя (смотреть на название файла)
f = open('9 - Lambda, Dict - 02.02.py', encoding='utf-8')
for i in f:
    if i[0] != '#' or i[0] == ' ' or i[0] == '\n':
        print(i.strip())
f.close()


