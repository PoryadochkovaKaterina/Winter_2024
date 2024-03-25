# Второй read, если он прочитал всё из файла, то уже ничего не прочтет
# Расчет медианы
# leng = len(lst)
# if leng > 0:   # Проверка на то, есть ли длинна вообще
#     medi - lst[leng//2] if leng%2 else (lst[leng//2 - 1] + lst[leng//2]) / 2
#     ws.cell(5,1).value = 'Медиана'
#     ws.cell(5,2).value = medi
import datetime

# Работа с файлами
# Печать выражения по буквенно
# with open('File/text.txt', 'r+', encoding='utf-8') as f:
#     s = f.read()
#     print(s)
#     dic = {}
#     for i in s.lower():
#         if i not in '\n ':
#             dic[i] = dic.get(i, 0) + 1   # добавление элемента в словарь, если его нет, о добавить новый элеменет
#
# with open('File/text.txt', 'a', encoding='utf-8') as fi:   # Неинтерабельная программа
#     for i in sorted(dic):   # sorted всё превращает в список
#         print(i * dic[i], file=fi)
#         print(i * dic[i])
#
# with open('File/text.txt', encoding='utf-8') as f2:
#     for i in f2:
#         print(i)

# Если что-то с большой буквы, то с большей вероятностью это класс
# import openpyxl
# from openpyxl import Workbook
# wb = Workbook()   # создаем экземплря класса Workbook
# wb.save('File/test.xlsx')   # сохраняем пустой

# print(wb.sheetnames)   # список листов
# ws = wb.active   # активный рабочий лист
# print(ws.title)   # просмотр
# ws.title = 'NewPage'   # Изменение имени
# print(ws.title)   # Просмотр
# ws2 = wb['NewPage']   # другой лист
# wb.active = wb['NewPage']    # назначение активного листа
# wb.remove(ws)   # удаление рабочего листа
# sheet['A1'].value   # значение, которое храниться в ячейке
# c = sheet['B2']   # выбрать ячейку
# c.row    # номер строки
# c.column   # номер колонки
# c.coordinate   # координаты
# ws.max_row   # максимальная длинна строки
# ws_max_column   # максимальная длинна колонки

# import openpyxl
# from openpyxl import Workbook
# wb = Workbook()
# wb.save('File/test.xlsx')
# wb.sheetnames
# ws = wb['Sheet']
# print(ws.max_row, ws.max_column)
# ws['A1'].value = 'sdfrefcvhb'
# print(ws['A1'].value is None)
# c = ws['B1']
# print(c.coordinate, c.row, c.column)
# for cellObj in ws['A1':'C3']:
#     for cell in cellObj:
#         print(cell.coordinate)

# import openpyxl
# wb = openpyxl.load_workbook('File/test.xlsx')
# print(wb.sheetnames)
# ws = wb['Sheet']
# ws.append(['Алексеев', 1300, True])   # Добавление данных после всего
# ws.append({1: 'Жуков', 2: 950, 3: False})   # Добавление данных в виде словаря. Ключи номера столбцов
# n = int(input())
# m = int(input())
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         ws.cell(row=i, column=j).value = str(i) + str(j)
# # Создание матрицы из чисел не сложенных между собой, а рядом стоящих
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         print(ws.cell(row=i, column=j).value)
#
# wb.save('File/test.xlsx')

# TIME, DATETIME, CALENDAR
# import time   # Удобен для технческой работы со временем
# time.sleep(2)   # сон на указанное время в секундах
# t0 = time.time()
# t1 = time.time()
# print(t1 - t0, t0, t1)   # время в секундах с определенного времени, если это не указано, то с 1970г


# import time   # Оценка работы программы!!!
# x = 10000000
# for i in range(1, 10+1):
#     t0 = time.time()
#     su = 0
#     for j in range(i * x):
#         su += j
#     t1 = time.time()
#     print(i, t1 - t0, su)

# time.time()
# time.ctime()   # Текущее время в секундах
# time.ctime(t)   # Текущее время
# time.sleep()


# import time   # Удобен для технческой работы со временем
# def sleep2():   # функция, в которой программа спит 2 сек
#     time.sleep(2)
#     return 2
# def sleep3():   # функция, в которой программа спит 3 сек
#     time.sleep(3)
#     return 3
# odd, even = 0, 0
# for i in range(11):   # цикл, в котором, если число чет запуск сна 2сек, если нечет, то запуск сна 3 сек
#     if i % 2:
#         odd += sleep3()
#     else:
#         even += sleep2()
#     print(i, even, odd)   # Накопление и печать сумм

# datetime.date   # дата
# datetime.time   # время
# datetime.timedelta   # разницав между двумя моментами времни с точностью до микросекунды
# datetime.datetime   # комбинация даты и времени
# datetime.datetime.today()   # текущая дата и время

import datetime
# print(datetime.datetime.today())

# STRPTOIME
# from datetime import datetime
# print(datetime.strptime('07 02 2024 20:55', '%d %m %Y %H:%M'))   # вывод даты и времени в удобном для нас формате
# print(datetime.strptime('07_02_2024_20:55', '%d_%m_%Y_%H:%M'))

# DATETIME
# from datetime import date, time
# my_date = date(2024, 2, 7)
# my_time = time(21, 15, 35)   # Секунды не обязательны
#
# print(my_date, my_time)
#
# # Форматированный вывод даты
# print(my_date.strftime('%d/%m/%y'))   # день/месяц/год
# print(my_date.strftime('%A %d, %B %Y'))   # день недели, день, месяц, год
# print(my_time.strftime('%H:%M:%S'))   # час:минута:время
# print(my_date.strftime('%a %d, %b %Y'))   # сокращенный день недели, день, сокращенное название месяцев, год


# from datetime import datetime
# print(datetime.now())   # текущее время и дата
# print(datetime.today())   # текущее время и дата
#
# # Структурирование через кортеж чисел
# a = datetime(2024, 2, 7, 21, 10)
# print(a)
# print(a.year)   # чему равен год
# print(a.minute)   # сколько минут
#
# # Еще один способ получения текущей даты
# from datetime import date
# today = date.today()
# print('Date= ', today)

# ЛОКАЛИЗАЦИЯ
# from datetime import date
# import locale

# locale.setlocale(locale.LC_ALL, 'ru')   # Перевод в русский формат (локализация) ru_RU.UTF-8
# my_date = date(2024, 2, 7)
# print(my_date.strftime('%A %d, %B %Y'))

# locale.setlocale(locale.LC_ALL, 'en')
# my_date = date(2024, 2, 7)
# print(my_date.strftime('%A %d, %B %Y'))
#
# locale.setlocale(locale.LC_ALL, 'fr')
# my_date = date(2024, 2, 7)
# print(my_date.strftime('%A %d, %B %Y'))
#
# locale.setlocale(locale.LC_ALL, 'de')
# my_date = date(2024, 2, 7)
# print(my_date.strftime('%A %d, %B %Y'))


# from datetime import date
# import locale
#
# locale.setlocale(locale.LC_ALL, 'ru')
# my_date = date(1996, 7, 29)
#
# print(my_date.strftime('%B'))


# import calendar
# print(calendar.weekday(2024, 2, 7))   # день недели в виде целого числа начиная с 0
# print(calendar.monthrange(2024, 2))   # день недели первого дня месяца
# print(calendar.monthcalendar(2024, 2))   # матрица календаря месяца
# print(calendar.month(2024, 2, w=0))   # календарь на месяц в виде мнгогострочной матрицы
# print(calendar.calendar(2024))   # календарь года
# print(calendar.isleap(2024))   # является ли год високосным
#
# import calendar
# y = int(input())
# print(calendar.weekday(2024, 12, 31))
# print(calendar.weekday(2024, 1, 1))

# from datetime import timedelta, date
# for i in range(10):
#     a = date(2024, 2, 26) + timedelta(i)
#     print(a)
