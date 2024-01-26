# s = 'abracadaba'
# for k in s:
#     print(k, s.find(k))

# lang = 'Python'
# print(f'{"lang"} is the best!')

# print('All  you  need  is  love'.split())
# print('All  you  need  is  love'.split(' '))

# Задача 3-1
# su, hm = 0, 0
# while True:
#     s = int(input('Ввведите зп: '))
#     if s == 0:
#         break
#     su += s
#     hm += 1
# print(su/hm)

# Задача 3-2
# Первый варинт
# s = input()
# for k in '0123456789':
#     print(k, '-', s.count(k))

# Второй вариант
# hm = [0] * 10
# s = input()
# for k in s:
#     i = int(k)
#     hm[i] += 1
# for k, v in enumerate(hm):
#     print(k, '-', v)

# Задача 3-3
# Первый вариант
# s = input().split()
# # print(s)
# ma = '' # Потенциально максимально длинное слово
# for w in s:
#     if len(w) >= len(ma):
#         ma = w
# for w in s:
#     if len(w) == len(ma):
#         print(w)

# Второй вариант
# s = input().split()
# # print(s)
# res = ['']
# for w in s:
#     if len(w) == len(res[0]):
#         res.append(w)
#     elif len(w) < len(res[0]):
#         pass  # ничего не делает, можно и continue
#     elif len(w) > len(res[0]):
#         res = [w]
# print(*res) # убирает строковый тип и оставляет в удобном виде

# Словарь (dict)
# hm = {}   # Определяем пустой словарь
# s = input()
# for k in s:
#     if k not in hm:   # Есть ли наш символ в строке
#         hm[k] = 0   # Если нет, то заводим индеекс
#     hm[k] += 1   # Увеличиваем на 1 кол-во символов
# for k in hm:   # Перебираем все найденные символы = ключи словаря
#     print (k, hm[k])   # Печатаем ключи и значения

# s = input()
# dct = {}
# for k in s:
#     if k not in dct:
#         dct[k] = 0
#     dct[k] += 1
# print(dct)
# for k in dct:
#     print(k, dct[k])

# Словарь = ключь:значение (ключ - уникален)
# dic = {
#     <key>:<value>,
#     <key>:<value>,
#     ...
# }

# Доступ к элементам словаря идет только по ключу
# person = {
#     'name':'Masha',
#     'login':'Maria',
#     'age':25
# }
# print(person)
# person['name'] = 'Misha'
# print(person)

# Числа, строки и логические переменные могут быть ключом
# dct = {1:123, 2:'mango', 234:True}
# print(dct)

# HASH TABLE(Function) - мгновенный поиск в словаре
# dct = {}
# while True:
#     a = input('Товар: ') # Вводим данные в словарь
#     if a == '0': break
#     if a in dct:
#         dct[a] += 1 # Если данные уже есть, то увеличиваем кол-ов на 1
#     else:
#         dct[a] = 1 # Если данных нет, то записываем значение 1
# print(dct)

# dct_1 = {
#     False: 324,
#     True: 1234
# }
# dct_2 = {
#     True: 1234,
#     False: 324
# }
# print(dct_1)
# print(dct_2)
# print(dct_1 == dct_2)   # Так как ключи одинаковые и значения в них тоже одинаковые, то словари считаются одинаковыми

# dct = {
#     None: 'mango',
#     None: 'coco'   # Если в словаре два одинаковых ключа, то выводиться последнее значение указанное в словаре
# }
# print(dct)

# dct = {
#     '1': 'Один',
#     '2': 'Два',
#     '3': 'Три'
# }
# s = input()
# for i in s:   # Циклом ходим по s
#     if i in dct:   # Входит ли i в словарь и пропускать эти значения, если не входят или печать необходимые значения
#         print(dct[i], end = ' ')   # выводим из словаря значения, которые есть в s и dct
#     else:
#         print('*', end = ' ')   # Печать заданного символа, вместо тех значенмий, которые нет в словаре

# Способы создания словаря:
# dct1 = {'a':123, 'b':234}
#
# dct2 = {}
# dct2['a'] = 123
# dct2['b'] = 345
#
# dct3 = dict(a=123, b=456)   # Функция для создания словаря
#
# letters = ['a', 'b']
# dig = [123, 789]
# dct4 = dict(zip(letters, dig))   # zip - передает пары из указанные элементов
#
# print(dct1, dct2, dct3, dct4, sep='\n')

# dct = {
#     1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
#     7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
# }
# while True:
#     ye = int(input())
#     mon = int(input())
#     if ye + mon == 0: break
#     if ye % 4 == 0 and mon == 2:
#         print(29)
#     else:
#         print(dct[mon])

# Удаление элементов del person
# dct = {
#     1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
#     7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
# }
# del dct[2]
# print(dct)

# Длина словаря
# dct = {
#     1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30
# }
# print(dct)
# print(len(dct))

# Составить словарь, который хранит слова и кол-во его вхождений из введенного текста
# tx = input().split()
# dct = {}
# for i in tx:
#     if i not in dct:   # Проверка на вхождения i в словарь
#         dct[i] = 0
#     dct[i] += 1
# print(dct)

# # Найти наиболее редко встречающееся слово, если несколько то укзаать все слова из списка
# tx = input().split()
# dct = {}
# for i in tx:
#     if i not in dct:   # Проверка на вхождения i в словарь
#         dct[i] = 0
#     dct[i] += 1
# # Наименее часто встречающиеся слова
# word = tx[0]
# for k in dct:
#     if dct[k] < dct[word]:
#         word = k
# print(word, dct[word])
# # Наиболее часто встречающиеся слова
# word = tx[0]
# for k in dct:
#     if dct[k] > dct[word]:
#         word = k
# print(word, dct[word])

# Являются ли слова анаграммами
# dct1, dct2 = {}, {}
# s = input().split()
# print(s)
# for w in s[0]:
#     if w not in dct1:   # не входит ли w в dct1
#         dct1[w] = 0
#     dct1[w] += 1
# for w in s[1]:
#     if w not in dct2:   # не входит ли w в dct2
#         dct2[w] = 0
#     dct2[w] += 1
# print(dct1)
# print(dct2)
# print(dct1 == dct2)

# Кортеж (tuple)
# Неизменяемой последовательности, кол-ция произвольных объектов
# Фиксированная длина, массив ссылок на объекты
# print(tuple([1,2,3]))
# print(tuple('abcd'))
# print(tuple((1,)))
#
# a,b,c = 1, 'á', True
# tpl = (a,b,c)
# print(tpl[0], tpl[1], tpl[2])

# (x, y) = (1, 2)
# print(x, y)

# lst = [11, 22, 33, 44, 55]
# for k in enumerate(lst):   # если убрать значение из списка и оставить только индекс, то это становиться кортежем
#     print(k, type(k), k[0], k[1])  # 0 - ключ, 1 - значение. Как добрать до значения из кортежа

# index(value,start,stop)  # индекс заданного элемента

# tpl = (1,2,3,[11,22,33])
# tpl[3].append(44)  # т.к. 3-й элемент список, то можно добавить изменить значение, при этом не изменяя кортеж,
# # который не меняется. Кортеж можно изменить, если изменять список внутри него
# print(tpl)

# tpl1 = (123,234,345,456,567,678,789,890)
# x = int(input())
# res = 0
# if x <= 123: res = (x,) + tpl1  # запятая после x, говорит о том, что добавляем в кортеж значение
# elif x >= 890: res = tpl1 + (x,)
# else:
#     for k, v in enumerate(tpl1[1:], 1):
#         if x >= tpl1[k-1] and x <= v:
#             res = tpl1[:k] + (x,) + tpl1[k:]
#             break
# print(res)