# Задание 6-1
# Первое решение
# def roman_to_decimal(number):
#     dct = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40,
#            'IX': 9, 'IV': 4, 'M': 1000, 'D': 500,
#            'C': 100, 'L': 50, 'X': 10, 'V':5, 'I':1}
#
#     res = 0
#     while number != '':
#         for i in dct:
#             if number.startswith(i):
#                 res += dct[i]
#                 number = number[len(i):]
#                 break
#     return res
# print(roman_to_decimal(input()))

# Задание 6-2
# Первое решение
# f = input().split(', ')
# a = input().split(', ')
# print(len(set(f) & set(a)))

# Задание 6-3
# Первое решение
# s = input()
# let, dig, oht = set(), set(), set()
# for i in s:
#     if i.isalpha(): let.add(i)
#     elif i.isdigit(): dig.add(i)
#     else: oht.add(i)
# print(*sorted(let))
# print(*sorted(dig))
# print(*sorted(oht))

# Коллекции:
# Строка (str) ''
# Список (list) []
# Кортеж (tuple) ()
# Словарь (dict) {}
# Множество (set) {}
#
# set.isdisjoint() - есть ли общее
# set.issubset() -
# set.issuperset()
# set.union() - объединение (|)
# set.intersection() - пересечение (&)
# set.difference() - нет ни в первом, ни во второном (-)
# set.symmetric_difference() - есть в первом, но нет во втором (^)
# set.copy()

# frozenset  # Замороженное множество

# Функции
# Определение функции
# def suum(x, y):   # вход в функцию
#     res = x + y   # тело фунции
#     return res   # вывод из функции

# # вызов функции
# x = 100
# y = 50
# ans = suum(x, y)
# print(ans)

# Всё что внутри функции личное дело функции
# Вызвать переменную, объявленную в фунцкции вне функции нельзя
# Функция может и не принимать никаких параметров

# Роль функции в программировании
# 1. Сокращение кода
# 2. Логическое разделение программы
# 3. Проще тестировать
# 4. Более эффективная организация труда команды разработчиков

# def my_fun(пар1, пар2,...)Ж
#     тело функции
#
#     возвращаемое значение
#     return res # необязательно
#
# вызов функции
# my_fun([арг1, арг2, ...])
# или
# res = my_fun([арг1, арг2, ...])

# Возвращение функции без return
# def suum(x, y):
#     return x + y
# z = suum(10, 20)
# print(z)


# def suum(x, y):
#     res = x + y
#     return res;
#
# z = suum(10)
# print(z)

# Программа вычисление подоходного налога (13%) от суммы дохода
# def nal(doh, n13, n15):
#     if doh <= 5000000:
#         pod_nal = doh * n13 / 100
#         # return pod_nal
#     else:
#         doh15 = doh - 5000000
#         pod_nal = doh15 * n15 / 100 + 5000000 * n13 / 100
#     return pod_nal
#
# while True:
#     n = float(input())
#     if n == 0: break
#     print(f'{n} : {nal(n, 13, 15)}')   # Задаем значения параметров

# Параметры по умолчанию
# def prem(sal, per = 10):
#     p = sal * per / 100
#     return p
# res = prem(60000)   # указаны только sal
# print(res)
# print((prem(60000,20)))   # указаны и sal и per

# Пустая функция (функция необходима, но реализации еще нет). Заглушка
# def emp(va1, va2):
#     pass
#     return 'Еще не сделали'
# res = emp(8, 10)
# print(res)   # При выхове функции выдает None

# Именованные параметры
# def fun(a1, a2, a3, a4, a5, a6):
#     print(f'{a1=} : {a2=} : {a3=} : {a4=} : {a5=} : {a6=}')
#     return a1+a2+a3+a4+a5+a6
# print(fun(a1=6, a2=5, a3=4, a4=3, a5=2, a6=1))
# Без return будет None

# Функция с неограниченным количеством аргументов
# def fun(var1, *args):
#     print(var1)
#     print(args)
#     print(max(args))
#     return len(args)
#
# print(fun(11, 22, 33, 44))

# Фунция с любым количестовм элементов и возвращение их произведению
# def fun(*args):   # кортеж без ключей
#     prod = 1
#     for i in args:
#         prod *= i
#     return prod
# print(fun(1, 2, 3, 4, 5))

# **kwargs - произвольное число именованных аргументов
# def fun(**kwargs):   # словарь
#     print(kwargs)
#     print(type(kwargs))
# print(fun(x = 10, y = 20))

# Функция с любым кол-вом именнованных параментов, и возвращается произведение числовых параментов
# и конкатенацию текстовых, игнорируя остальные
# def kil(**kwargs):
#     res1 = 1
#     res2 = ''
#     for k in kwargs:
#         v = kwargs[k]
#         if type(v) == int:
#             res1 *= v
#         elif type(v) == str:
#             res2 += v
#     return res1, res2
# print(kil(a = 123, b = 'ábc', c = 'yvx', d = 456))
# При пустой строке выдаст те значения, которые указаны в res1 и res2 в самой функции

# def fun(var1, *args, **kwargs):
#     print(var1)
#     print(args)
#     print(kwargs)
#
# print(fun())

# Функция принимающая список слов и выводящая
# 1. Строку уникальных букв
# 2. Кол-во уникальных значений
# def un_let(lst):
#     res = set()
#     for i in lst:
#         res = res.union(set(list(i)))
#     result = ''.join(sorted(res))
#     return result, len(result)
# print(un_let(['мама', 'мыла', 'раму']))
# print(un_let(['all']))
# print(un_let(['áll', 'many']))
# print(un_let(['all', 'many', 'people']))
# print(un_let([]))

# def func(n):
#     def func_1(p):
#         return p * p
#     def func_2(w):
#         return w + w
#     if n < 10:
#         res = func_1(n)
#     else:
#         res = func_2(n)
#     return res
# x = int(input())
# print(func((x)))

# Нелокальная область видимости
# def cou():
#     num = 0
#     def inc():
#         nonlocal num
#         num += 1
#         return num
#     x = inc()
#     print(num)
#     return x
# cou()

# ZIP
# for k in zip([1, 2, 3, 4, 5], 'abcdef'):
#     print(k)

# for k in zip((1, 2, 3, 4), {1: 111, 2: 222}, {123,456, 789}):
#     print(k)
# zip останавливается по минимальному итерируему объекту

# REVERSED - Переворачивание значений (в обратном порядке)
# for k in reversed([1, 5, 2, 4, 3]):
#     print(k)

# MAP - применяет к каждому элементу списка фунцию первого параметра (в примере int)
# s = list(map(int, input().split()))
# k = 123
# print(s)
# print(sum(map(int, list(str(k)))))

# Разделение строки на числа
for i in map(int, input().split()):
    print(i)
