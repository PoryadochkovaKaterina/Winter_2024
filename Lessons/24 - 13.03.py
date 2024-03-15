# a = [7, 71, 72]
# big = sorted(map(str, a), reverse=True)
# print(big)
#
# bigs = lambda a: int(''.join(sorted(map(str, a), reverse=True)))
# print(bigs([7, 71, 72]))

# Задание 23-1
# def max_pal(s):
#     len_s = len(s)
#     for i in range(len_s, -1, -1):
#         for j in range(len_s - i):
#             ss = s[j:i+j+1]
#             if ss == ss[::-1]:
#                 return ss, len(ss)
# s = input()
# print(max_pal(s))

# Импорт в Эксель
# import psycopg2
# import openpyxl
#
# con = psycopg2.connect(
#     database='postgres',
#     user='postgres',
#     password='*****',
#     host='127.0.0.1',
#     port='5432')
#
# cur = con.cursor()
# cur.execute('''SELECT author, title FROM book ''')
# # rows = cur.fetchall()
# # for row in cur:
# #     print(row)
#
# xlfile = 'File/book.xlsx'
# wb = openpyxl.Workbook()
# ws = wb.active
# ws.append(['Автор', 'Название'])   # Название столбцов по-руссски
# for row in cur:
#     ws.append(row)
# con.close()
# wb.save(xlfile)


# import psycopg2
# con = psycopg2.connect(
#     database='postgres',
#     user='postgres',
#     password='*****',
#     host='127.0.0.1',
#     port='5432')
#
# cur = con.cursor()
# cur.execute('''SELECT book_id, author_name, title, 100 - amount AS order
#         FROM book INNER JOIN author
#         ON book.author_id = author.author_id
#         ORDER BY book_id''')
# s = 0
# for i in cur:
#     print(f'{i[0]:5} | {i[1]:10} | {i[2]:25} | {i[3]:5}')
#     s += int(i[3])
# print(f'{'ИТОГО':5} | {' ':10} | {' ':25} | {s:5}')
# con.close()

# Создание базы в PyCharm
# import sqlite3
# con = sqlite3.connect('my_database.db')
# cursor = con.cursor()
# #  Создаем таблицу Users
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Users
#         (
#         id INTEGET PRIMARY KEY,
#         username TEXT NOT NULL,
#         age INTEGET
#         )
#     ''')
# #  Сохраняем изменения и закрываем соединения
# con.commit()
# con.close()

# Добавление данных в таблицу БД в PyCharm
# import sqlite3
# # Устанавливаем соединение с базой данных
# con = sqlite3.connect('my_database.db')
# cursor = con.cursor()
# # Добавляем новых пользователей
# cursor.execute('''INSERT INTO Users VALUES
#     (1, 'user1', 18),
#     (2, 'usee2', 20)''')
# # Сохраняем изменения и закрываем соединение
# con.commit()
# con.close()

# Вывод на экран данных из БД в PyCharm
import sqlite3
# Устанавливаем соединение с базой данных
con = sqlite3.connect('File/my_database.db')
cursor = con.cursor()
# Выбираем пользователей
cursor.execute('''SELECT * FROM Users''')
users = cursor.fetchall()
# Выводим результат
for user in users:
    print(user)
# Закрываем соединение
con.close()

