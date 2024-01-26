# nums = [1,2,3,4,5]
# nums.append((nums[:]))   # Добавление списка в виде подсписка
# print(len(nums))
import shlex

#  nums[:] - делает копию списка nums

# Ключами могут быть только неизменяемые объектов

# Задача 4-1
# Первый вариант решения
# s = input().split()
# print(s)
# if s[1] == '+': print(float(s[0] + float(s[2])))
# elif s[1] == '-': print(float(s[0] - float(s[2])))
# elif s[1] == '/': print(float(s[0] / float(s[2])))
# elif s[1] == '*': print(float(s[0] * float(s[2])))

# Второй вариант решения
# print(eval(input()))   # eval вычисляет значение, которое внутри него

# Задача 4-2
# Первое решение
# n = int(input())
# d, x, y, z = {}, 0, 0, 0
#
# for i in range(n):
#     for j in range(n):
#         d[i, j] = 0
#
# def pri():   # Функция печати
#     for i in range(n):
#         for j in range(n):
#             print(f'{d[i, j]:2}', end=' ')
#         print()
# pri()
# input()
#
# dx, dy = 0, 1
# for i in range(n * n):
#     z +=1
#     d[x, y] = z
#     if d.get((x + dx, y + dy), -1) != 0:
#         if (dx, dy) == (0, 1): dx, dy = 1, 0
#         elif (dx, dy) == (1, 0): dx, dy = 0, -1
#         elif (dx, dy) == (0, -1): dx, dy = -1, 0
#         elif (dx, dy) == (-1, 0): dx, dy = 0, 1
#     x, y = x + dx, y +dy
#     pri()
#     input()
#
# for i in range(n):
#     for j in range(n):
#         print(f'{d[i, j]:2}', end=' ')
#     print()

# Задача 4-3
# s = input()
# z = input()
# ss, zz = {}, {}
# for i in s:
#     if i in 'Алфавит':
#         ss[i] = ss.get(i, 0) + 1
# for i in z:
#     if i in 'Алфавит':
#         zz[i] = zz.get(i, 0) + 1
# print(ss == zz)

# print('abcABC'.isalpha())   # Все ли значения буквенные
# print('abcDc'.isalnum())
# print('23424'.isdigit())
#
# import string
# print(string.ascii_letters)   # Все буквенные значения
# print(string.punctuation)   # Все знаки препинания

# get - получить и не изменять значение словаря
# get(key[, default])
# x = {'one':1, 'two':2, 'three':3}
# x.get('two',0)   # Получить ключ из словаря
# x.get('ten',0)   # Получить ключ из словаря, если отсутствует, то записать 0
# print(x.get('one', -1))
# print(x.get('two', -1))
# print(x.get('three', -1))
# print(x.get('five', -1))

# setdefault(key[, default]) - получает и меняет значение словаря
# x = {'one':1, 'two':2, 'three':3}
# print(x.setdefault('one', -1))
# print(x.setdefault('two', -1))
# print(x.setdefault('three', -1))
# print(x.setdefault('five', -1))
# print(x)

# n = int(input())
# dct = {}
# for i in range(n):
#     s1, s2 = input().split()
#     # print(s1, s2)
#     dct[s1] = s2
#     dct[s2] = s1
# # print(dct)
# while True:
#     z = input()
#     if z == 'stop': break
#     print(dct.get(z, 'Такого нет'))

# x = {'one': 0, 'two': 20, 'three': 3, 'four': 4}
# print(x.clear())   # Удаление элемента из словаря
# dct = x.copy()   # Копия словаря
# print(dct)
# del x   # Удаление словаря
# print(x)
# abckey = x.keys()
# x[5] = '333'
# print(abckey)   # Возвращает список всех ключей содержащихся в словаре
# # и x и abckey содержат один

# Задание на сортировку словаря
# dct = {5: 555, 3: 333, 7: 777, 1: 111}
# res = {}
# abc = sorted(dct.keys())   # Сортировка найденных ключей
# for i in abc:
#     res[i] = dct[i]
# print(res)

# values() - возвращает новый список всех значений словаря
# dct = {5: 555, 3: 333, 7: 777, 1: 111}
# x = dct.values()
# dct[2] = 222
#  print(x)

# items()  - новый список кортежей вида (keys, value)
# dct = {5: 555, 3: 333, 7: 777, 1: 111}
# x = dct.items()
# print(x)
# for k, v in dct.items():
#     print(k, v)

# lst = [int(k) for k in input().split()]   # Ввод строки состоящей из чисел, разделенных пробелом
# res = {}
# print(lst)
# for i, v in enumerate(lst):
#     res.setdefault(v, []).append(i)
#     print(res)
#     input()
# Проверяем значения, если значения уже есть в списке, то записываем индекс этого значения в подсписок
# Если значения нет, то создается новый подсписок с необходимым значением
# setdefault - заводит пару значение (keys и value) и если его нет, то создает новый подсписок с занчением

# fromkeys(iterable[, value]) - создание нового словаря с ключами из последовательности iterable и значениями из value
# x = dict.fromkeys(['a', 'b', 'c'],0)
# print(x)
# x = dict.fromkeys(['dfg'],0)
# print(x)

# update() - объединение словарей
# abc = {1: 11, 2: 22}
# bcd = {3: 33, 4: 44}
# abc.update(bcd)   # Если ключи совпадают, то заменяется на последне значение из последнего словаря
# print(abc)

# pop(key[, default]) - возвращение значени ключа, а также удаление его из словаря, если ключа нет, то default
# abc = {1: 11, 2: 22, 3: 33, 4: 44}
# lst = [1, 2, 3, 4]
# print(lst.pop(0))
# print(lst)

# popitem() - удаляет и возвращает двойной кортеж из словаря
# abc = {1: 11, 2: 22, 3: 33, 4: 44}
# print(abc.popitem())
# print(abc)
# abc[5] = 55
# print(abc.popitem())
# print(abc)

# Вывести список товаров и сумму их количества в алфавитном порядке
# res = {}
# while True:
#     s = input()
#     if s == '0':
#         break
#     # y = int(s1[1])
#     k, v = s.split()
#     # res.setdefault(k, []).append(int(v))
#     if k in res:
#         res[k] += float(v)
#     else:
#         res[k] = float(v)
# for k in sorted(res):   # В sorted  можно управлять сортировкой
#     print(k, res[k])

# divmod(x, y) = x // y, x % y
# pow(x, y[,z]) = x в степени y по модулю z
# print(divmod(23, 4))

# round() - округление
# print(round(1.1))
# print(round(1.5))
# print(round(2.6))

# for k in [4, 3, 2, 1, 0]:
#     print(k, round(12.3456, k))   # Округление числа до k запятой после точки

# print(float('inf')) = 2e400  # Самое максимальное число (бесконечность)
# print(float('-inf')) = -2e400  # Самое минимальное число

# print(int('10', 2))
# print(int('10', 8))
# print(int('10', 16))

# Выявить является ли число простым или составным
# n = int(input())
# for k in range(2, n):
#     for i in range(2, k):
#         if k % i == 0:
#             print(k, 'Составное')
#             break
#     else:
#         print(k, 'Простое')
