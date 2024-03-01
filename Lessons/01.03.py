# a = {True: '1', 1: 'one', '1': '1', "1": "1"}
# print(a)

# a = {1: '1', True: 'one'}   # ключ вытесняет значение
# print(a)

# a = {False: '0', 0: 'zero'}
# print(a)
#
# a = {0: '0', False: 'zero'}
# print(a)
# когда пара с одинаковыми ключами, то остается первый ключ
# значение, если одинковые, то берется второе значение
# import numpy
# Задание 19-1
# import itertools
# s = [10, 50, 100, 200, 500, 1000, 2000, 5000]
# tes = set()
# for i in range(1, len(s)+1):
#     for x in itertools.combinations(s, i):
#         tes.add(sum(x))
# print(*sorted(tes))

# Задание 19-2
# class Fibo:
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.a, self.b = self.b, self.b + self.a
#         return self.a
#
# fibo = Fibo()
# for _ in range(10):
#     print(next(fibo), end=' ')

# Задача 19-3
# class Person:
#     def __init__(self, *args):
#         self.args = args
#     def __str__(self):
#         return ''.join(self.args)[::-1]
# p = Person('Abc', 'Def', 'Ert', 'Gkt')
# print(p)

# import itertools
# for x in itertools.permutations([1, 2, 3, 1]):   # перестановки (все значения, без уникальности)
#     print(x, end=' ')

# for x in itertools.combinations([1, 2, 3], 2):   # несовпадающие элементы без повторов
#     print(x, end=' ')

# for x in itertools.combinations_with_replacement([1, 2, 3], 2):   # несовпадающие элементы с повторами
#     print(x, end=' ')

# for x in itertools.cycle([1, 2, 3]):   # повторение столько раз сколько необходимо
#     print(x, end=' ')

# for x in itertools.chain([1, 2, 3, 4], 'abc', {10: 100, 20: 200}):
#     print(x, end=' ')

# list = zip([1, 2, 3], 'ab', [11, 22, 33, 44])   # по наименьшему значению
# for i in list:
#     print(i)

# list = itertools.zip_longest([1, 2, 3], 'ab', [11, 22, 33, 44])   # по наибольшему значению
# for i in list:
#     print(i)

# s = 'aaabbbaaaabbbbdddcccddddbbb'
# for k, v in itertools.groupby(s, key=lambda x: x < 'c'):   # key - ключ по которому группируем
#     print(k)   # группирует пока значения одинаковые
#     for j in v:
#         print(j, end=' ')
#     print()
# в группу попадаются все значения, которые меньше или больше с

# s = [1, 3, 5, 2, 4, 8, 7, 11, 13, 12, 14, 121]
# for k, v in itertools.groupby(s, key=lambda x: x % 2):   # key - ключ по которому группируем
#     print(k, ':', *v)   # группа 1, когда остаток 1, группа 2, когда остаток 2 и т.д.

# s = [-1, -2, -3, 1, 2, 3, 4, 0, -10, -7, -5]
# for k, v in itertools.groupby(s, key=lambda x: x <= 0):
#     print(*v)   # звезддочка распаковыевает все значения для itertools.group

# import numpy as np   # обязательно as np
# # import pandas as pd   # обязательно as pd
# #import matplotlib as plt   # обязательно as plt
# lst = [1, 11, 111, 1111, 2, 22, 222, 2222]
# arr = np.array(lst, dtype=float)   # если добавить dtype=float, то все значения, становятся float
# print(arr)   # append не работает, len - работает
# print(arr.dtype)
# # если хоть одно число float, то все числа становятся float

# import numpy as np   # обязательно as np
# lst = [[1, 11], [111, 1111]], [[2, 22], [222, 2222]]
# arr = np.array(lst)
# print(arr)   # arr.shape сколько строк и элекментов в них

# import numpy as np
# lst = [1, 2, 3, 4, 5, 6]
# arr1 = np.array(lst)
# arr2 = np.array((11, 22, 33, 44, 55, 66))
# print(arr1+arr2)   # складываение элементами 1 и 11, 22 и 2, 33 и 3 и т.д.

# import numpy as np
# a = np.zeros((2, 3), dtype= int)
# print(a)   # создание двумерной матрицы из 0 из 2 строк и 3 столбцов
#
# a = np.ones((2, 3), dtype= int)
# print(a)   # создание двумерной матрицы из 1 из 2 строк и 3 столбцов

# import numpy as np
# a = np.zeros((8,), dtype=int)
# # b = a.reshape(6)   # создание линейного массива для (2, 3)
# b = a.reshape((2, 2, 2))   # создание двух двумерных массивов для (8)
# print(b)

# import numpy as np
# a = np.zeros(6, dtype=int)
# print(a.shape)   # кортеж с параметром длины 6
# b = a.reshape((3, 2))   # массив из 3 строк по 2 элемента (2 столбца)
# print(b)

# import numpy as np
# a1 = np.array([[1, 2, 3], [10, 20, 30]])
# print(np.sum(a1))   # сумма всех элементов
# print(np.sum(a1, axis=0))   # поэлементное сложение по вертикали
# print(np.sum(a1, axis=1))   # поэлементное сложение по вертикали
# print(np.sum(a1, axis=None))   # идентично просто sum

# import numpy as np
# print(np.gcd([6, 24, 72], [24, 12, 36]))   # наибольший общий множитель
# print(np.lcm([6, 24, 72], [24, 12, 36]))   # наименьший общий множитель

# ГРАФИК
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.linspace(0, 5, num=50)
# # y = np.exp(x)
# y = np.sqrt(x)
#
# plt.plot(x, y)   # график без разметки и название
# plt.grid()   # график с разметкой, но без названия
# # _ = plt.title('y=exp()')   # название графика
# _ = plt.title('y=sqrt()')
# plt.show()

# import numpy as np
# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, np.nan])
# print(np.mean(x, axis=None))   # среднее значение, возвращает nan, если в массиве содержится константа np.nan
# print(np.nanmean(x, axis=None))   # среднее значение, игнорируя nan
# print(np.average(x, axis=None, weights=None))   # считает среднее, может вычислять взвешенное среднее, не обрабатывая np.nan
# print(np.max(x, axis=None))   # максимум, выбирает nan если оно содержится в массиве
# print(np.min(x, axis=None))   # минимум, выбирает nan если оно содержится в массиве
# print(np.nanmin(x, axis=None))   # минимум, игнорируя nan
# print(np.nanmax(x, axis=None))   # максимум, игнорируя nan
# print(np.median(x, axis=None))   # медиальное значение, возвращает nan, если оно есть в массиве
# print(np.nanmedian(x, axis=None))   # медиальное значение, игнорируя nan
# print(np.percentile(x, 10))   # процентиль q возвращает nan если он есть в списке
# print(np.nanpercentile(x, 10))   # процентиль q, игнорируя nan

# import numpy as np
# a1 = np.array([1, 2, 3])
# a2 = np.array([2, 2, 2])
# print(a1 == a2)   # поэлементное сравнение массивов
# print(a1 > a2)
# print(a1 > 1.5)
# x = a1 != a2
# x = a1 > a2
# x = a1 == a2
# print(a1[x])

# индексация булевскими массивами
# arr = np.array([3, 4, 5, 1])
# mean = np.mean(arr)   # 3.25
# con = arr > mean   # [False, True, True, False] - сравнение каждого элемента arr с mean
# print(arr[con])   # вывоз значений, которые True

# Выборка и печать элементов, которые строка меньше 25 процентиля
# import numpy as np
# arr = np.array([2, 7, 4, 5, 6, 3, 4, 5, 6, 7, 8, 9, 10])
# con = arr < np.percentile(arr, 25)   # con или True, или False
# # print(arr[arr < np.percentile(arr, 25)])
# print(arr[con])   # тоже самое, что и в строке выше

#  np.where(condition, x1, x2) - по условия или из х1 или из х2
# import numpy as np
# x = np.array([3, 5, 1, 8, 14, 17, 3, 10, 15, 18])
# y = x * 10
# print(np.where(x > 5, x, y))   # печать x, если оно больше 5, и x*10, если оно меньше 5

# np.sort(x, axis=None)   # сортировка
# import numpy as np
# x = np.array([[19, 3, 9, 19, 10], [1, 4, 12, 16, 7]])
# # sorted_x = np.sort(x, axis=None)   # сортировка всего массива
# # sorted_x = np.sort(x, axis=0)   # сортировка по столбцам
# sorted_x = np.sort(x, axis=1)   # сортировка по строкам
# print(sorted_x)

# import pandas as pd
# основные объекты Series и DataFrame
# создание из двумерного списка
# df1 = pd.DataFrame([[1, 'Bob', 'Builder'],
#                     [2, 'Sally', 'Baker'],
#                     [3, 'Scott', 'Candle Stick']],
#     columns = ['id', 'name', 'third'])   # название колонок
# print(df1)

# создание из словаря
# df2 = pd.DataFrame({
#     'country': ['Kazakhstan', 'Russia', 'Belarus'],
#     'popoulatin': [17.04, 143.5, 9.5],
#     'square': [2724902, 17125191, 207600]
# })
# print(df2)

# df = pd.DataFrame()   # создание пустого фрейма
# # print(df)
#
# lst = ['First', 'Second', 'Third']  # заполнение фрейма значениями из списка
# # print(pd.DataFrame(lst))
#
# lst = {'ID': ['First', 'Second', 'Third'],
#        'DEPT': ['Dev', 'BA', 'Test']}
# df = pd.DataFrame(lst)
# print(pd.DataFrame(lst))
#
# df['xxx'] = df['ID'] + df['DEPT']   # новый столбец с названием xxx и значениям объединенными из is и dept
# df['yyy'] = [123, 456, 678]   # новый столбец с новыми значениями
# print(df)

# dct = {'Год': [2001, 2002, 2003, 2004, 2005],
#        'Товар': ['A', 'B', 'C', 'D', 'E'],
#        'Количество': [10, 20, 30, 40, 50],
#        'Цена': [100, 50, 30, 20, 5]}
# df = pd.DataFrame(dct)
# print(df)
# df['Итого'] = df['Цена'] * df['Количество']
# print(df)
# # df_from_excel = pd.read_excel('text.xlsx')   # импорт
# df.to_excel('test.xlsx')   # экспорт
# df1 = pd.read_excel('test.xlsx')   # импорт
# print(df1)

#  ГИСТОГРАММА
# import pandas as pd
# import matplotlib.pyplot as plt
#
# df = pd.DataFrame({'Год': [2001, 2002, 2003, 2004],
#                    'Прибыль': [111, 444, 222, 333]})
# df.index = df['Год']
# df['Прибыль'].plot(kind='barh')   # колонки по прибыли
#
# plt.grid()
# _ = plt.title('Прибыль')
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
#
# df = pd.DataFrame({'Год': [2001, 2002, 2003, 2004, 2005],
#                   'Товар': ['A', 'B', 'C', 'D', 'E'],
#                   'Количество': [10, 20, 30, 40, 50],
#                   'Цена': [100, 50, 30, 20, 5]})
# print(df[['Год', 'Цена']])   # обращение к выбранным колонкам
# print(df.loc[2003, 'Цена'])   # выбор одной строки
# print(df.loc[0:2])   # выбора нескольких строк
# print(df[df['Цена'] > 25])   # выбор по условию
# print(df[(df['Год'] == '2002') | (df['Цена'] == 30)])   # выбор по условию
# print(df.iloc[0])   # выбор одной строки
# print(df[0:3])

# New_df = df.T   # Транспонирование
# df.loc[0, 'Количество'] = 123
# print(df.index)
# print(df.columns)
# df1 = df.set_index('Год')
# print(df1.index)
# print(df1.loc[2002:2003])
# print(df1.iloc[1:3])
# print(df1.loc[2003] = ['F', 30, 100, 3000])

# ЦИКЛ ПЕРЕБОРА МАССИВА
# for i in df.index:
#        for j in df.columns:
#               print(i, j, df.loc[i, j])

# print(df[df['Год'] == 2001])   # строка, где год == определенному значению
# print(df[df['Год'] > 2002])   # строки, где год больше 2002
# print(df[(df['Год'] > 2002) & (df['Цена'] > 25)])   # строки, где год больше 2002 и цена более 25

# ВСЕ ЭЛЕМЕНТЫ МАССИВА
# import pandas as pd
# df = pd.DataFrame({'Год': [2001, 2002, 2003, 2004, 2005],
#                   'Товар': ['A', 'B', 'C', 'D', 'E'],
#                   'Количество': [10, 20, 30, 40, 50],
#                   'Цена': [100, 50, 30, 20, 5]})
# for i in df.index:
#        for j in df.columns:
#               print(i, j, df.loc[i, j])

# loc по значениям индексов и колонок
# iloc по физическим номерам

