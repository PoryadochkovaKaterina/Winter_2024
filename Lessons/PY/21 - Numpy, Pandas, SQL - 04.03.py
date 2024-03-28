# a = ('Python', 'Java')
# b = ('Python',)
# c = ('Python')
# print(type(a))
# print(type(b))
# print(type(c))

# class A:
#     def __init__(self, limit):
#         self.limit = limit
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.limit <= 0:
#             raise StopIteration
#         else:
#             self.limit -= 1
#             #print(self.limit)
#             return self.limit
# b = A(10)
# for _ in range(10):
#     print(next(b))
# for i in b:
#     print(i)

# import numpy as np
# arr = np.array([8, 4, 9, 6, 7, 1, 3, 2])
# arr1 = arr.reshape((4, 2))
# sorted_arr = np.sort(arr)
# print(sorted_arr)
# sorted_arr[5] = 12
# print(sorted_arr)
# print(arr > sorted_arr)
# print(arr + sorted_arr)
# print(arr[arr > sorted_arr])   # сравнение между собой, где кто находится
# print(arr[arr <= sorted_arr])

# import pandas as pd
# import random
# df = pd.DataFrame(columns=['Год', 'Товар', 'Шт', 'Цена'], index=range(20))
# x = 0
# for i in range(2001, 2006):
#     for j in ['A', 'B', 'C', 'D']:
#         k = [10, 20, 30, 40, 50][random.randint(0,4)]
#         m = [100, 50, 30, 20, 5][random.randint(0,4)]
#         df.iloc[x] = [i, j, k, m]   # работает с физическим номером строки (логическая нумерация)
#         x += 1
# df['Итого'] = df['Цена'] * df['Шт']
# print(df['Шт'])   # тоже самое, что и print(df.Итого)
# print(df[['Шт', 'Цена', 'Итого']])
# print(df.loc[0])
# print(df[(df['Цена'] == 20) & (df['Товар'] == 'A')])
# print(df[(df['Цена'] == 20) | (df['Товар'] == 'A')])
# new_df = df.T   # Транспонирование
# print(new_df)
# print(df.index)
# print(df.columns)
# df1 = df.set_index('Год')
# print(df1)
# df.loc[20] = [2007, 'E', 100, 2, 200]   # добавление строки
# print(df)
# print(df.head(3))   # без ничего выдает 5 строк с головы
# print(df.tail(3))   # без ничего выдает 5 строк с хвоста
# print(len(df))   # длинна
# print(df['Цена'].unique())    # уникальные значения в столбце
# print(df.describe())   # статистика
# print(df.Итого, df.Итого.value_counts())   # Итого с количеством того, сколько раз встретилась
# print(df.sum())   # сложение всего
# print(df[['Шт', 'Цена']].mean())

# df1 = df[0:2]
# df2 = df[10:13]
# df3 = pd.concat([df1, df2], ignore_index=True)
# print(df3)

# df1 = df + df   # плюсует значения двух таблиц
# print(df1)

# print(df[df['Товар'].isin(['A', 'C'])])   # выборка по нескольким значениям
# print(df.sort_values(['Итого', 'Товар'], ascending=False))   # сортировка
# print(df.groupby('Итого').count())   # сколько строчек с каждым значеним в столбце

# print(df['Итого'].max())   # максимальная сделка
# print(df[df['Итого'] == df['Итого'].max()])   # значения с максимальной сделкой

# print(df[1:len(df):2])   # каждая вторая строка в DataFrame

# me = df['Цена'].mean()   # все строки у которых цена меньше среднего
# print(df[df['Цена'] < me])

# Найти минимальное значение для каждого столбца.
# Потом минимальное значение всех строковых значений
# mi = []
# for i in df.columns:
#     mi.append(df[i].min())
# mi_number = min(i for i in mi if isinstance(i, (int, float)))
# mi_str = min(i for i in mi if type(i) == str)
# print(mi, mi_number, mi_str)

# print(df.sort_values('Итого', ascending=False).head(3))   # три самые большие сделки
# print(df.sort_values('Итого', ascending=True).head(3))   # три самые маленькие сделки
# print(df.groupby('Товар').Итого.sum())   # сумма сделок для каждого товара
# print(df.groupby('Товар').Итого.sum().max())   # наибольшое число из сум сделок
# print(df.groupby('Год').Итого.sum())   # сумма сделок для каждого года
# print(df.groupby('Год').Итого.sum().max())   # максимальное из сумм сделок для каждого года
# print(df.groupby('Товар').Шт.sum())   # продажи товаров по Шт
# print(df[df['Год'] == 2003].Итого.sum())   # сумма продаж в конкретном году


# SQL в программе
# SELECT * FROM book   # просмотр всех записей, которые есть в таблице book
# CREATE TABLE book (book_id int, title text, author text, price int, amount int)   # создание таблицы со столбцами и их типами
# INSERT INTO book VALUES   # добавление значений в таблицу
# (2, 'Евгений Онегин', 'Пушкин', 200, 7)
# SELECT author, title FROM book   # выборка определенных столбцов
# SELECT author, title, price * amount FROM book   # выборка по столбцам с умножением значений колонок c создание новой колонки
# SELECT author, title, price * amount as total FROM book   # название новой колонки
# WHERE price * amount > 1000   # сравнение колонок со занчением
# WHERE author = 'Пушкин'   # фильтр по значениям
# WHERE title LIKE 'Р%'   # поиск в столбце по регулярному выражению
# WHERE title LIKE '% %'   # поиск в стоблце (книги с названием из двух слов
# ORDER BY author   # сортировка по автору
# SELECT 123   # выдает просто число. не связанное с каким-то сущесутвующзим элементом