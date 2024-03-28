# [i for i in range(10)] - список
# (i for i in range(10)) - генератор
# {i for i in range(10)} - множество
# {i:i**2 for i in range(10)} - словарь

# print(print(10))   # Сначала 10, потом None

# Задание 14-1
# def num_dig(n):
#     if n < 10:   # Если  число меньше 10, то возвращает 1, т.к сумма чисел равно 1
#         return 1
#     else:
#         return 1 + num_dig(n // 10)
#
# print(num_dig(int(input())))

# Задание 14-2
# def num_dig(n):
#     if n < 10:   # Если  число меньше 10, то возвращает n
#         return n
#     else:
#         return n % 10 + num_dig(n // 10)
#
# print(num_dig(int(input())))

# Задание 14-3
# def tri(n):
#     if n == 1:
#         print('*')
#     elif n < 1:
#         pass
#     else:
#         print('*' * n)   # Часть до вызова фунции
#         tri(n - 1)
#         print('*' * n)   # Часть после выхова функции
#
# print(tri(int(input())))
# При n == 3
# 1. Формируется первый эезкмпляр, где выполняется '*' * n и f(2)
# 2. Формируется второй экземпляр, где выполняется '*' * n и f(1)
# 3. Формируется трерий экземпляр, где выполняется n == 1 и возвращается return('*')
# 4. На последнем принт идет обратно по всем экземплярям возвращая значения, которые были в экземплярах
# 5. При экземпляре, где n == 2, возвращаем '*' * n
# 6. При экземпляре, где n == 3, возвращаем '*' * n

#  ПЕСОЧНЫЕ ЧАСЫ
# def fun(n, d=0):
#     if n == 1:
#         print(' ' * d + '* ' * n)
#         return
#     else:
#         print(' ' * d + '* ' * n)
#         fun(n - 1, d + 1)
#         print(' ' * d + '* ' * n)
#
# print(fun(int(input())))

# FINALLY
# def f(x, y):
#     try:
#         return x / y
#     except:
#         return x, y
#     finally:
#         print('finally')
# print(f(1, 2))
# finally сильнее, чем return внутри функции
# выводит для начала finally, потом уже значение выполняющегося return


# def fun():
#     yield from range(10)
# for i in fun():
#     print(i)

# МЕМОИЗАЦИЯ
# Количество вызовов функции для расчета чисел Фибоначчи
# d = {}
# def fibo(n):
#     d[n] = d.get(n, 0) + 1   # подсчет сколько раз вызывалась функция при каждоем значении n
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)
# fibo(17)
# print(d)

# d = {}
# res = {1: 0, 2: 1}
# def fibo(n):
#     d[n] = d.get(n, 0) + 1   # подсчет сколько раз вызывалась функция при каждоем значении n
#     if n not in res:   # Если n нет есть в словаре res
#         if n > 2:   # если ключ n уже есть в словаре значений, то просто возвращаем
#             res[n] = fibo(n - 1) + fibo(n - 2)
#     return res[n]   # Сначала запоминаем результат, потом возвращаем
# fibo(17)
# print(d)   # количество запущенный раз с помощью запоминания помежуточных результатов
# print(res)

# MATCH ... CASE ... - замена большого количества if

# # lst = [1, 'a', [11, 'cd', 22, [111, 222, [1111, 'sg', 2222, 3333], 333, 444, [555, 666]], 3], 4]
# lst = [1, 'asdf', 3, 5, '4', [23, 23, 45, 'ff'], 342, [234, 555]]
# # lst = [1, 'jhk', 3, [5, 'ghj', 3]]
# res = []
# def rek(lst):
#     for i in lst:
#         print(i, res)
#         if type(i) == int or type(i) == float:   # если просто число, строка или еще что-то, то пропускаем (записываем в res)
#             res.append(i)
#         elif type(i) == list:   # Если список, то происходит рекурсивный спуск
#             rek(i)
# rek(lst)
# print(res)


# lst = [1, 'asdf', 3, 5, '4', [23, 23, 45, 'ff'], 342, [234, 555]]
# def rek(lst):
#     res = []
#     for i in lst:
#         print(i, res)
#         if type(i) == int or type(i) == float:   # если просто число, строка или еще что-то, то пропускаем (записываем в res)
#             res.append(i)
#         elif type(i) == list:   # Если список, то происходит рекурсивный спуск
#             res.extend(rek(i))
#     return res
# print(rek(lst))


# Настройка глубины рекурсии
# import sys
# print(sys.getrecursionlimit())
# get - достает, set - устанавливает
# без необходимости не переустанавливать глубину рекурсии

# re - модуль Python (import re)
# Позволяет использовать все богаство регурлярных выражений по поиску, замене, выборке
# Не только в Питоне
# Проверка текста по шаблону

# import re
# string = 'Числа 99, -72, -81, и 999 делятся на 9'
# print(re.findall(r'81', string))   # выводит все 81 из строки
# print(re.findall(r'[89]', string))   # один из символов, который в скобках
# print(re.findall(r'9', string))   # выводит все 9-ки из строки
# print(re.findall(r'[0-9]', string))   # все числа, которые входят в диапозон
# print(re.findall(r'\d', string))   # выводит все числа цифр
# print(re.findall(r'\d\d', string))   # выводит все числа, где две цифры подряд
# print(re.findall(r'\d\d\d', string))   # выводит все числа, где три цифры подряд
# print(re.findall(r'\d{1,3}', string))   # выводит все числа, где от 1 до 2 цифр подряд
# print(re.findall(r'\d{3}', string))   # тоже самое, что и \d\d\d
# print(re.findall(r'\d+', string))   # все числа
# print(re.findall(r'\d*', string))   # все цифры строки с пустыми значениями вместо букв и знаков
# print(re.findall(r'.\d*', string))   # каждый символ из строки
# print(re.findall(r'\d{2}', string))   # все числа, где 2 цифры рядом
# print(re.findall(r'\d{2},', string))   # все числа, где 2 цифры подряд с запятой
# print(re.findall(r' \d{2}', string))   # все числа, где 2 цифры подряд с пробелампи перед ними
# print(re.findall(r'\d, \d', string))   # последовательность символов = цифра, запятая, цифра
# print(re.findall(r'\w{3}', string))   # три любые символа
# print(re.findall(r'\w{7}', string))   # семь любых символов
# print(re.findall(r'[+-]\d+', string))   # значения со знаком
# print(re.findall(r'[+-]?\d+', string))   # т.к. плюс, тоже самое, что и просто число, то можно ввести ? и будут выведены все числа

# Спецсимволы . ^ $ * + ? [] {} \ | экранируются с помощью \
# import re
# string = 'Числа 99, -72, -81, и 999 делятся на 9 Ёё'
# print(re.findall(r'[а-я]', string))   # все буквы входящие в строку из диапозона, маленькие
# print(re.findall(r'[А-Яа-я]', string))   # все буквы диапозона и большие и маленькие тоде
# print(re.findall(r'[А-Яа-я]{2,3}', string))   # все 2 и 3 буквы идущие подряд из диапозона
# print(re.findall(r'[А-ЯЁа-яё]{2,3}', string))   # все 2 и 3 буквы идущие подряд из диапозона. Ёё указываестя дополнительно

# import re
# string = '0abracadabra1 abracadabra'
# print(re.findall(r'.a.', string)) # буква а, с символами и справа и слева
# print(re.findall(r'\wa\w', string))   # буква а, с символами и справа и слева, не считая пробела
# print(re.findall(r'\da\w|\wa\d', string))   # цифра - а - буква, буква - а - цифра, (|) - значение или

# Все значения от 100 до 199
# import re
# strint = '12i, 93, 745, 100, 2434, сумма, 200, 111, 432, 100'
# # reg = r'1\w{2}'   # Если нет числа с символами
# # reg = r'1\d\d'
# # reg = r'1[0-9]{2}'
# print(re.findall(reg, strint))

# \b - начало и конец слова
# \w - буквы
# \w+ - несколько букв, до какого либо знака или символа
# \w* - n-е кол-во символов
# . - точка всё, что угодно

# import re
# string = 'Косой: косил косой косой - траву. Напокосе'
# reg = r'\b\w+\b'
# # reg = r'\b\w*[Кк]ос\w*\b'   # все слова, в которые входит (Кос и кос)
# # reg = r'\b.*\b'   # вся строка
# print(re.findall(reg, string))

# c[auc]t - cat, cut, cit - символы
# c[a-c]t - cat, cbt, cct - символы из диапозона
# c[^auc]t - всё, кроме a, u, t - ни один из символов
# c[^a-c]t - всё, кроме a, b, c - ни один из символов

# \d - любая цифра
# \D - любая не цифра
# \w - любая буква-цифра и _
# \W - любая не \w
# \s - пробельный символ
# \S - непробельный символ
#
# {1,3} - от 1 до 3
# [2] - ровно 2
# [2,] - от 2 и более
# [,5] - не более 5

# import re
# string = 'Мой номер машины L645YU182 или P364RY87'
# reg = r'\b[A-Z]\d{3}[A-Z]{2}\d{2,3}\b'
# print(re.findall(reg, string))

# re.sub() - замена значения в строке
# import re
# string = 'Java самый популярный java язык программирования'
# reg = re.sub(r'[Jj]ava', r'Python', string)
# print(reg)

# re.subn()
# import re
# string = 'Java самый популярный java язык программирования'
# reg, n = re.subn(r'[Jj]ava', r'Python', string)
# print(reg, n)

# Четные числа
# import re
# string = 'Четные числа 13 1 0 2 11 456 34 23 12 33 22 342'
# reg = r'\d*[02468]\b'
# print(re.findall(reg, string))

# Кратное 5
# import re
# string = 'Кратное 13 1 0 2 11 10 34 55 12 33 45 342'
# reg = r'\d*[05]\b'
# print(re.findall(reg, string))

