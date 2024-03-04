# Задание 13-2
# Выводит количество полиндромов согласно указанному числу
# def pal():
#     n = 0
#     while True:
#         n += 1
#         if str(n) == str(n)[::-1]:
#             yield n
# gf = pal()
# for _ in range(int(input())):
#     print(next(gf), end=' ')

# Задание 13-3
# def odd(lst):
#     for i in lst:
#         if i % 2:
#             yield i
# lst = list(map(int, input().split()))
# df = odd(lst)
# for i in df:
#     print(i, end=' ')

# Лоаушка для двух исключений
# def div(x,y):
#     dct = {1: 11}
#     print(dct['abc'])
#     return x / y
# try:
#     res = div(100, 0)
#     print('Успешно')
# except (ZeroDivisionError, KeyError) as er:
#     print('Ошибка деления или обращения по ключу. ', er)

# Несколько ловушек
# def div(x,y):
#     return x / y
# try:
#     res = div(100, 0)
#     print('Успешно')
# except ZeroDivisionError as er:
#     print('Ошибка деления:', er)
# except KeyError as er:
#     print('Ошибка обращения по ключу:', er)

# Порядок следования обработки согласно иерархии
# def div(x,y):
#     return x / y
# try:
#     res = div(100, 0)
#     print('Успешно')
# except ZeroDivisionError as er:
#     print('Ошибка деления на ноль:', er)
# except ArithmeticError as er:
#     print('Ошибка деление на ноль:', er)

# Каскадно включение перехватчиков
# def div(x, y):
#     try:
#         out = x / y
#     except:
#         try:
#             import math
#             out = math.inf * x / abs(x)
#         except:
#             out = None
#     finally:
#         return out
# print(div(15, 3))
# print(div(15, 0))
# print(div(-15, 0))
# print(div(0, 0))

# Генерация исключений в Python (RAISE)
# try:
#     raise Exception('Что-то не так')   # Для принудительной генерации исключений используется raise
# except Exception as e:
#     print('Информация: ' + str(e))

# Валидатор входного стргокового значения на имя человка
# def val(name):
#     if len(name) < 10:
#         raise ValueError
# try:
#     name = input('Введите имя: ')
#     val(name)
# except ValueError:
#     print('Слишком короткое имя')

# Пользовательские исключения
# ДЛя увеличения гибкости процесса обработки ошибок в рамках
# той предметной области

# class NameTooShortError(ValueError):
#     pass
# def val(name):
#     if len(name) < 10:
#         raise NameTooShortError
# try:
#     name = input('Введите имя: ')
#     val(name)
# except ValueError as re:
#     print('Слишком короткое имя: ', re)

# Пользовательсткие исключения
# class NegValException(Exception):
#     pass
# try:
#     val = int(input('Введите положительное число '))
#     if val < 0:
#         raise NegValException('Число отрицательное: ', str(val))
#     print(val + 10)
# except NegValException as e:
#     print(e)


# class OnlyLetters(Exception):
#     pass
# class OnlyDigit(Exception):
#     pass
# try:
#     pas = input('Введите пароль: ')
#     if pas.isalpha():
#         raise OnlyLetters('Добавьте цифры. ' + str(pas))
#     elif pas.isdigit():
#         raise OnlyDigit('Добавьте буквы. ' + str(pas))
#
#     print('Пароль принят')
# except OnlyLetters as e:
#     print('Введены только буквы: ' + str(e))
# except OnlyDigit as e:
#     print('Введены только цифры: ' + str(e))

# Функция генератора
# def fun(n):
#     for x in range(n):
#         yield x * x
#
# dg = fun(3)   # Вызов генератора 3 раза
# # print(next(dg))
# # print(next(dg))
# # print(next(dg))
# # print(next(dg))   # Если кол-во итераций будет больше, что заданное число, будет
# # ошибка, чтобы этого избежать, можно задать исключение в цикле
# for k in range(10):
#     try:
#         print(next(dg))
#     except StopIteration:   # Способ прервать генератор, через исключение, при выдачи генератора меньше, чем range
#         break

# Прекращение генерации внутри генератора
# def fun(val, max_rep):
#     cou = 0
#     while True:
#         if cou >= max_rep:
#             return   # Прекращение программы с помощью return
#         cou += 1
#         yield val
#
# for x in fun('Повтор', 5):   # float(inf) - бесконечное кол-во раз
#     print(x)

# Что можно сдлеать с функцией генератора
# def rep123():
#     yield 1
#     yield 2
#     yield 3
# # Можно вызвать всё 3 print
# print(*rep123())   # Распаковская значение (*)
# print(2 in rep123())   # Использование функции (in). Входит ли знаение в генератор
#
# n1, n2, n3 = rep123()   # Множество присвоение значений
# print(n1, n2, n3)
#
# n1, n2, n3 = rep123()   # Столько значений, сколько в генераторе, не больше, не меньше
# print(n1, n2)

# def rep123():
#     yield 1
#     yield 2
#     yield 3
# df = rep123()
# # print(*df)   # Выдает все значения, которые есть, поэтому следующий print ничего не напечатает
# # # Генератор опустошен
# # print(2 in df)
# n1, n2, n3 = df
# print(n1, n2, n3)
# print(2 in rep123())   # Если снова вызвать генератор, то print будет выдавать значения

# def rep123():
#     yield 1
#     yield 2
#     yield 3
# df = rep123()
# print(next(df))
# print(next(rep123()))
# print(next(df))
# print(next(rep123()))

# В генераторе нельзя:
# * получить длину
# * итерацию по индексу

# YIELD FROM <ITERABLE>
# def fun_gen(n):
#     for x in range(n):
#         yield x
# for i in fun_gen(5):
#     print(i)
# def fun_gen2(n):   # упрощенная запись генератора сверху
#     yield from range(n)
# for i in fun_gen2(5):
#     print(i)

# def df():
#     # yield from {1: 11, 2: 22, 3: 33}   # Выведет только ключи
#     yield from (1, 22, 333, 4444)
# print(*df())

# Вложенный генератор
# def fg1():
#     yield 'Red'
#     yield 'Green'
#     yield 'Blue'
#
# def fg2():   # Для начала выведет Round, потом 1-ый генератор, потом Square
#     yield 'Round'
#     yield from  fg1()
#     yield 'Square'
#
# print(*fg2())

# ГЕНЕРАТОРНЫЕ ВЫРАЖЕНИЯ
# li_com = [x for x in range(10)]   # Список. Будет сразу создан
# print(*li_com)
# g_exp = (x for x in range(10))   # Генератор. Не будет создан, пока не запустят
# print(*g_exp)
#
# for x in g_exp:   # Обращение как с функцией генератора
#     print(x)
#
# # После использования генераторное выражение остается пустым

# КОНВЕЙЕРЫ ГЕНЕРАТОРОВ
# def inter(n):
#     # for i in range(1, n + 1):
#     #     yield i
#     yield from range(1, n + 1)   # Сокращенная форма записи выше
# # print(*inter(10))   # Значения от 1 до 10
#
# def eve(iter):
#     for i in iter:
#         if not i % 2:
#             yield i
# # print(*eve(inter(10)))   # Четные значения от 1 до 10
#
# def squa(iter):
#     for k in iter:
#         yield k * k
#
# ch = squa(eve(inter(10)))    # Квадраты четных значений от 1 до 10
# print(*ch)

# Создание конвейра генератора
# Первый перебирает значение от 65 до 90
# Второй применяет к каждому числу функцию chr()
# Получить последовательность больших латинских букв
# def pos


# def pos(n):
#     yield from range(n, n + 26)
# def pos2(iter):
#     for i in iter:
#         yield chr(i)
#
# print(*pos2(pos(97)))   # 97 - мелкие буквы

# РЕКУРСИВНЫЕ ФУНКЦИИ
# def fun():
#     print('fun')
#     input()
#     fun()
# fun()

# def func(n):
#     print('func', n)
#     input()
#     n -= 1
#     if n > 0:
#         func(n)
# func(7)   # Вызов функцией самой себя с параметром


# def func(n):
#     print('func1', n)
#     input()
#     n -= 1
#     if n > 0:
#         func(n)
#     print('func2', n)   # Начнет выполняться, после того, как сработает if, который вызывает функцию
#     # Происходит возврат функции
#     input()
#     return
# func(3)
# Запустили при n = 3, при n = 2, при n = 1, после if func2 пошла в обратном порядке
# Для начала рекурсивный спуск, потом рекурсивный подъем
# Откат с возвратом экземляров функции, через оператор return
# return возвращает на следующую строчку, после запуска функции
# return возвращает в предыдущую итерацию
# Для начала 3, 2, 1, потом при возвращении return, обращается к значениям
# Получается 2, 1, 0 и выводит в порядке возвращения, а именно в обратном
# Получается 3, 2, 1, 0, 1, 2

# Рекурсия - расчет факториала
# def fact(n):
#     if n == 1:
#         return 1   # базовый случай - вариант решения без рекурсии
#     else:
#         return n * fact(n - 1)   # Рекурсивный случай - сведение задачи к более простой
# print(fact(1))   # 1
# print(fact(2))   # 2 != 1 -> 2 * fact(1) -> 2 * 1 = 2
# print(fact(3))   # 3 != 1 -> 3 * fact(3-1) -> 3 * fact(2) -> 3 * 2 * fact(1) -> 3 * 2 * 1
# print(fact(4))   # 4 != 1 -> 4 * fact(4-1) -> 4 * 3 * fact(2) -> 4 * 3 * 2 * fact(1) -> 4 * 3 * 2 * 1

# Рекурсивная функция печати треугольника из звездочек
# def star(n):
#     if n == 1:
#         print('*')   # печать (*), если n == 1
#         return
#     else:
#         print('*' * n)   # печать (*) умноженных на n
#         star(n-1)   # вычитание из n
# star(int(input()))

# Рекурсивная сумма чисел от 0 до n
# def summ(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return n + summ(n - 1)
# print(summ(int(input())))

# Рекурсивная фукнция чисел Фибоначчи
def fiba(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fiba(n-1) + fiba(n-2)
print(fiba(8))