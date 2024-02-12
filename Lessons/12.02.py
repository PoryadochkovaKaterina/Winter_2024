# Задача 12-1
# x = [1, 2, 3, 4, 1, 2, 3, 4, 1]
# # s = list(map(int, input().split()))
# # z = [int(i) for i in input().split()]
# print(x)
# # print(s)
# # print(z)

# mi = min(x)
# ma = max(x)
# print([i for i in range(len(x)) if x[i] == mi])
# print([i for i in range(len(x)) if x[i] == ma])
# import functools
# import itertools

# Задача 12-2
# res = [i for i in range(1, int(input()) + 1) for j in range(i)]
# print(*res)

# i = '5'
# print([int(i)] * int(i))
# print(i * int(5))

# Задача 12-3
# s = input().split(',')
# res = []
# for z in s:
#     if '-' in z:
#         x, y = map(int, z.split('-'))
#         for u in range(x, y + 1):
#             res.append(u)
#     else:
#         res.append(int(z))
# print(res)

# DICTIONARE COMPREHENSION
# print({i: i ** 2 for i in range(10)})   # Квадрат чисел до 10
# print({i: i ** 2 if i % 2 else i ** 3 for i in range(10)})   # Четный квадрат, нечетный куб

# Если делится на 2, то квадрат числа, если не делится, то куб
# print([i ** 2 if i % 2 == 0 else i ** 3 for i in range(1, 11)])

# finctools.reduce(function, iterable[, initialixer])
# Принимает стоящий первым аргумент функцию для двух начальных элементов списка,
# а затем использует в качестве аргументов этой функции полученное значение вместе
# со следующим элементом списка и так до тех пор, пока весь список не будет пройден,
# а итоговое значение не будет возвращено

# import functools
# print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5], 100))
# print(functools.reduce(lambda x, y: x*y, [1, 2, 3, 4, 5]))   # Факториал 5
# # Перемножение всех значений между друг другом
# print(functools.reduce(lambda x, y: x*y, [1, 2, 3, 4, 5], 10))
# # 10*20*30*40*50 = 1200

# import functools
# functools.cmp_to_key(func)   # превращаем фукнцию
# Строки сравниваются по первому символу

# from functools import cmp_to_key
# x = ['d', 'cc', 'bbb', 'aaaa']
# def cmp_string(x, y):   # сортировка по длинне строки, а не символам
#     if len(x) < len(y): return -1
#     elif len(x) == len(y): return 0
#     else: return 1
# print(*sorted(x))
# print(*sorted(x, key=cmp_to_key(cmp_string)))
# Сортируем строку (каждый элемент списка) x ключу, указанному в key. Функция является аргументов другой функции
# Функция в данном случае не вызвается и параметры не нужны

# itertools.combinations(inretable, r)
# Все комбинации из списка по две элемента
# import itertools
# for k in itertools.combinations([1, 2, 3, 4, 5], 2):
#     print(k)
# for k in itertools.combinations('abcde', 2):
#     print(k)

# itertools.combinations_with_replacement(iterable, r)
# import itertools
# for k in itertools.combinations_with_replacement([1, 2, 3], 3):
#     print(k)

# Монетка 1 руб, 2 руб, 5 руб, 10 руб
# Сколько вариантов сумм денег если взять 3 монетки
# import itertools
# tes = set()   # убираем уникальность сумм
# for k in itertools.combinations([1, 2, 5, 10], 3):
#     tes.add(sum(k))
# print(tes)
# # Сколько вариантов сумм денег если взять 2 каждого достоинства монетки
# import itertools
# tes = set()   # убираем уникальность сумм
# for k in itertools.combinations([1, 1, 2, 2, 5, 5, 10, 10], 3):
#     tes.add(sum(k))
# print(tes)


# ОБРАТОКА ИСКЛЮЧЕНИЙ
# s = int(input())
# print(s)
# # ОШИБКИ:
# Синтаксические - не соотвествие правилам языка
# Логические - логика правильная, но не так, которая должна быть
# Исключения - работа с файлами, с СУБД, с сетью, с различными библиотеками

# try:
#     s = int(input())
#     print(s)
# except:
#     print('Ошибка ввода данных')

# try:
#     Запуск кода
# except:
#     Запуск кода, елси возникло исключение
# else:
#     Запуск кода, если не было исключения
# finally:
#     Запуск кода всегда

# try:
#     s = int(input())
#     print('try', s)
# except:
#     print('Ошибка')
# else:
#     print('else', s)
# finally:
#     print('Finally')

# except может быть несколько. В приоритете те, которые в приоритете по иерархие классов
# try:
#     a = 1 / 0
# except Exception:
#     print('Exception')
# except ValueError:
#     print('ValueErroe')
# except ZeroDivisionError:
#     print('Ошибка, деление на ноль!')
#     a = 0
# else:
#     print('else')
# finally:
#     print('Finally')

# cou = 3
# while True:
#     try:
#         s = int(input('Введите целое число '))
#         print('Правильная строка: ', s)
#         break
#     except ValueError:
#         cou -= 1
#         print('Неправильная строка - повторите ввод. Осталось попыток: ', cou)
#         if cou < 1: break
#     except Exception:
#         print('Что-то случилось')

# while True:
#     try:
#         with open (input(), encoding='utf-8') as f:
#             print('Файл найден')
#             s = f.read()
#             print(s)
#             break
#     except FileNotFoundError:
#         print('Файл не найден')

# Функция генератор
# def fun(n):
#     for x in range(1, n):
#         # return x * x   # после выполнения return всегда покидает функцию
#         yield x * x   # возвращение значение с того момента, где вы остановились, после вызова функции до этого
# f = fun(6)   # создаем генератор, но без вызова функции
# for i in f:   # помешение функции в for
#     print(i)
# yield - многоразовый return, генератор

# def fun(n):
#     for x in range(1, n):
#         # return x * x   # после выполнения return всегда покидает функцию
#         yield x * x   # возвращение значение с того момента, где вы остановились, после вызова функции до этого
# f = fun(5)   # создаем генератор, но без вызова функции
# # print(next(f))   # Прямое использование функции
# # print(next(f))
# # print(next(f))
# # print(next(f))
# # print(next(f))   # Если n = 5, то появляется инсключение StopIteration
#
# print(next(f)) - for i in f:   # Примерно одно и тоже

# Возвращение квадрата, если четное и куб, если нечетное
# def fun(n):
#     for x in range(1, n + 1):
#         yield x, x ** 3 if x % 2 else x ** 2
# f = fun(int(input()))
# for i in f:
#     print(*i)

# def fun(n):
#     for x in range(1, n + 1):
#         yield x, x ** 3 if x % 2 else x ** 2
# f = fun(int(input()))
# while True:
#     try:
#         print(next(f))
#     except StopIteration:
#         print('Конец работы генератора!')
#         break


# lim = int(input())
# def fac():
#     f, k = 1, 1
#     while True:
#         yield f
#         k += 1
#         if k > lim:
#             break
#         f *= k
# gf = fac()
# Первый вариант вывода
# for m in range(int(input())):
#     print(next(gf))
# Второй вариант вывода
# lim = int(input())
# for i in gf:
#     print(i)
#     if i > lim:
#         break
# Третий вариант вывода
# for i in gf:
#     print(i)

# # Первый вариант, как глобальный
# lst = [1, 10, 100, 2, 20, 200]
# def su():
#     s = 0
#     for i in lst:
#         s += i
#         yield s
# x = su()
# for j in x:
#     print(j)


# # Второй вариант, список как параметр
# lst = [1, 10, 100, 2, 20, 200,]
# def su(lst):
#     s = 0
#     for i in lst:
#         s += i
#         yield s
# x = su(lst)
# for j in x:
#     print(j)


# # Вариант решения, если хотим сложить два раза список
# lst = [1, 10, 100, 2, 20, 200,]
# def su(lst):
#     s = 0
#     for i in lst + lst:
#         s += i
#         yield s
# x = su(lst)
# for j in x:
#     print(j)


# # Вариант решения, если хотим сложить два раза список
# lst = [1, 10, 100, 2, 20, 200,]
# def su(lst):
#     s = 0
#     for i in lst:
#         s += i
#         yield s
# x = su(lst + lst)
# for j in x:
#     print(j)

# Прекращение генерации return при yield
# def bou_rep(val, max_rep):
#     cou = 0
#     while True:
#         if cou >= max_rep:
#             return
#         cou += 1
#         yield val
#
# for x in bou_rep('Раз', 5):
#     print(x)


# Вывести последовательность 1 2 2 3 3 3 4 4 4 4 и т.д.
def pos(n):
    i = 0
    for i in range(i, n + 1):
        yield [i] * i

df = pos(int(input()))
for k in df:
    print(*k, end=' ')
