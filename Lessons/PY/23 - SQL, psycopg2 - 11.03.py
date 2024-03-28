# dict1 = {'яблоки': 200, 'апельсины': 100}
# dict2 = {'груши': 300, 'яблоки': 150}
#
# print(dict1 | dict2)
#
# res = {}
# for key in dict1 | dict2:
#     res[key] = dict1.get(key, 0) + dict2.get(key, 0)
# print(res)

# Задача 22-2
# Первое решение (Снизу - вверх)
# tree = [(1, 2), (1, 3), (2, 4), (2, 5), (4, 6), (3, 7), (7, 8), (8, 9)]
# max_path, max_v = 0, 0
# for i, j in tree:
#     cur_path = 0
#     tf = True
#     while tf:
#         cur_path += 1
#         for x, y in tree:
#             if y == i:
#                 i = x
#                 break
#         else:
#             tf = False
#     if cur_path > max_path:
#         max_path = cur_path
#         max_v = j
# print(max_path, max_v)

# Второе решение (Сверху - вниз)
# tree = [(11, 2), (11, 3), (2, 4), (2, 5), (3, 6), (6, 7), (7, 8), (8, 9), (5, 10)]
# tes = set([j for i, j in tree])
# for i, j in tree:
#     if i not in tes:
#         v = i
#         break
# p = {v: 0}
# tf = True
# while tf:
#     tf = False
#     for i, j in tree:
#         if j not in p and i in p:
#             p[j] = p[i] + 1
#             tf = True
#             break
#     print(p)
#     input()
# print(max(p.values()))

# Задача 22-3
# s = input().split()
# import keyword
# for i in sorted(keyword.kwlist, key=len, reverse= True):
#     s = s.replace(i, '<kw>')
# print(s)


# import psycopg2
# con = psycopg2.connect(
#     database='postgres',
#     user='postgres',
#     password='*****',
#     host='127.0.0.1',
#     port='5432'
# )

# cur = con.cursor()
# cur.execute('''SELECT * FROM book WHERE author = 'Кинг' ORDER BY book_id''')
# rows = cur.fetchone()
# print(rows)
# for row in rows:
#     print(f'book_id = {row[0]}', end=' ')
#     print(f'title = {row[1]}', end=' ')
#     print(f'author = {row[2]}')
# con.close()

# cur = con.cursor()
# cur.execute('''INSERT INTO book
#             VALUES (10, 'Тихий дон', 'Шолохов', 10, 160)''')
# con.commit()
# con.close()

# cur = con.cursor()
# # cur.execute('''CREATE TABLE city (code int PRIMARY KEY, city_name text, size int)''')
# cur.execute('''INSERT INTO city VALUES
#     (1, 'Москва', 13104177),
#     (2, 'Казань', 1314685),
#     (3, 'Самара', 1163645),
#     (4, 'Санкт-Петербург', 5600044)''')
# con.commit()
# con.close()

# from collections import Counter
# # t = input()
# t = input().split()
# # a = Counter('aabbcccccdddeeeeabcdef')
# # a = Counter('abracadabra')
# # a = Counter((1, 1, 2, 3, 3, 3, 3, 2, 2, 1, 1, 1, 4, 4, 3, 4, 5, 6))
# a = Counter(t)
# print(f'{a=}')
# b = dict(a)
# print(f'{b=}')

# Задача 23-1
# Даже одна буква это палиндромм
# Лучше отрезать от наибольшего слова

# Задача 23-3
# Количество ЧИСЕЛ
# 1 21 3 = 3 21 1 = 3211
# 9 81 25 = 9 81 25 = 98125
# Проверять различные варианты
# с 0, 1, одинаковыми значениями. Положительные целые ЧИСЛА
