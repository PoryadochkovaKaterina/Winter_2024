# Задача 5-1
# Решение 1 - недостаток в том, что хранит полностью всю последовательность
# n = int(input())
# lst = [[1]]
# for i in range(1, n):
#     cur = [1]
#     for j in range(1, i):
#         cur.append(lst[-1][j-1] + lst[-1][j])
#     cur.append(1)
#     lst.append(cur)
# for k in lst:
#     print(*k)

# Решение 2 - недостаток в том, что хранит значение тех числел, которые не использоются
# а дальнейшем
# n = int(input())
# lst1 = [0, 1]
# for i in range(1, n+1):
#     lst2 = [0]
#     for j in range(i):
#         lst2.append((lst1[j]) + lst1[j + 1])
#         print(lst2[-1], end= ' ')
#     lst2.append(0)
#     print()
#     lst1 = lst2.copy()

# Решение 3 - проигрывает во времени
# n = int(input())
# lst = [0, 1, 0]
# for i in range(2, n+1):
#     x = lst[0]
#     for j in range(1, i+1):
#         y = x + lst[j]
#         print(y, end=' ')
#         x = lst[j]
#         lst[j] = y
#     print()
#     lst.append(0)

# Задача 5-2
# Решение 1
# n = int(input())
# for i in range(1, n+1):
#     if n % i == 0:
#         print(i, end=' ')

# Усложненное решение
# n = int(input())
# dct = {}
# for i in range(2, n+1):
#     while n % i == 0:   # Вместо if в некоторых условиях, можно использовать while
#         dct[i] = dct.get(i, 0) + 1   # сколько делителей есть в n столько и будет создано записей
#         n = n // i
#         print(dct, n, i)
# print(dct)

# Задача 5-3
# n = int(input())
# a, b = 0, 1
# for i in range(n):
#     print(b, end=' ')
# #     a, b = b, a + b   # самая экономная форма переприсвоения
#     c = a   # тоже вариант переприсвоения, чаще используется он
#     a = b
#     b = c + b

# a = {1:11, 5:55, 3:33}
# print(sorted(a))   # По взрастанию
# print(sorted(a, reverse = True))   # По убыванию

# Лоческие типы (Все что не 0 - True)
# x = True   # Как 1
# y = False   # Как 0
# print(x + x)
# print(bool(0))
# print(bool(1))
# print(str(x))

# Фунции символов
# x = ord('A')
# print(chr(x))
# for i in range(65, 91):
#     print(chr(i), end=' ')
# print()
# for i in range(97, 97 + 26):
#     print(chr(i), end=' ')
# print()
# for i in range(1072, 1072 + 32):
#     print(chr(i), end=' ')
#
# print(chr(ord('s')))   # chr - выдает код, ord - печает буквы

# Определить код больших лат. букв  и напечатать цикл пар (букв и код)
# a = ord('A')
# z = ord('Z')
# print(a, z)
# for i in range(a, z+1):
#     print(chr(i), i)

# a = ord('А')
# for i in range(a, a + 32):
#     print(chr(i), i)
#     if i == 1045:
#         print(chr(1025), ord('Ё'))

# Сравнение строк - результа True или False
# IS - проверка идентичности объекта

# Операторы сравнения
# a = 1000
# b = 10
# print(a is b)   # Являются ли они одинаковыми значениям

# Приоритетность операций
# 1 - not
# 2 - and
# 3 - or

# Найти високосный год
# n = int(input())
# if n % 400 == 0:
#     print('Y')
# elif n % 100 == 0: print('N')
# elif n % 4 == 0: print('Y')
# else: print('N')

# в одну строку
# n = int(input())
# if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
#     print('Y')
# else:
#     print('N')

# None
# a = None
# if a is None:   # С None лучше использовать is
#     print('Ничего нет')
# else:
#     print('a')

# Перетасуйте гласные и согласные, чтобы они шли по очереди, иначе "Impossible!"
# f = input()
# v, c = '', ''
# res = ''
# for i in f:
#     if i in 'aeiou': v += i
#     else: c += i
# if abs(len(v) - len(c)) > 1:
#     print('Impossible!')
# elif len(v) > len(c):
#     for i in range(len(c)):
#         res += v[i] + c[i]
#     res += v[-1]
#     print(res)
# elif len(v) < len(c):
#     for i in range(len(v)):
#         res += c[i] + v[i]
#     res += c[-1]
#     print(res)
# else:
#     for i in range(len(c)):
#         res += c[i] + v[i]
# print(res)

# Множества (set)
# неупорядоченный набор элементов
# набор элементов уникальный и неизменыемый
# tes = set()
# print(type(tes))

# tes = set((1, 2, 3, 4, 3, 2, 1, 3, 2))
# print(tes)   # остаются только уникальные множества
# множество может быть с элементами разных типов

# tes = set((1,2,3, 'ABC', True, 456, (1,22)))   # True не отображается, так как уже есть 1, а все значения уникальные
# print(tes)

# Создание пустого множества
# tes = set()   # пустое множество
# lst = []   # пустой список
# dct = {}   # пустой словарь
# print(tes, lst, dct)

# tes = set()
# tes.add(1)
# tes.add(2)
# tes.add(3)
# tes.add(1)
# print(tes)

# Чтобы узнать сколько уникальных элментов, переводим во множество и узнаем его длину
# lst = [1, 2, 2, 2, 3, 3, 3, 3, 4, 4]
# mn = set(lst)
# print(len(mn))

# Интегрирование множест
# mon = {'jan', 'feb', 'mar', 'apr', 'jun', 'jul', 'aug'}
# for i in mon:
#     print(i)
# # проверка на членство в множестве
# print('jun' in mon)

# Операции со множеством быстрее, чем списки или кортежи, но памяти берется больше

import math
# tes = set(map(int, input().split()))   # ввод ряда числе через в строку в множество
# print(sum(tes) / len(tes))

# mon = {'jan', 'feb', 'mar', 'apr', 'jun', 'jul', 'aug'}
# mon.add('feb')
# print(mon)

# Удаление remove или discard
# при отсутсвие элемета будет ошибка при использовании remove

# union - обхединение множеств
# mon_a = set(['jan', 'feb', 'mar', 'apr'])
# mon_b = set(['jul', 'aug', 'jan'])
# all_mon = mon_a.union(mon_b)
# print(all_mon)


# s = list('каждыйохотникжелаетзнатьгдесидитфазан')
# ab = set('ё')
# x = ord('а')
# for i in range(x, x + 32):
#     ab.add(chr(i))
# print(ab, len(ab))
#
# tes = set(s)
# print(len(tes))
#
# print(ab.difference(tes))   # Разница между множествами

# вычисление количества уникальных символов во всех словах
# n = input().split()
# res = set()
# for i in n:
#     res = res.union(set(list(i)))
#     print(res)
# print(len(res))