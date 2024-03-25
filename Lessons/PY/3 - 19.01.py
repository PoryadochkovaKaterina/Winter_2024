n = int(input())
for i in range(1, 10):
   print(f"{i} x {n} = {i*n:2}")
#n:2 - для сдвига значения

# lst = [-1, 0, 3, -4, 3, 4]
# m = float('inf') # использование бесконечности
# print(m)
# for i in range(len(lst)):
#     if lst[i] < m: m = lst[i]
# print(m)

# import math
# print(math.factorial(int(input())))

# Печать всех строк списка
# lst = [1, 2, True, 'ABC', [3, 6, 8]]
# for i in range(len(lst)):
#     print(lst[i])

# Предпочтительная печать всех
# lst = [1, 2, 'ABC', True, [3, 6, 9]]
# for k, v in enumerate(lst):
#     print(k, v)

# Складывание списка
# lst1 = [1, 4, 8, 34,True, [3, 5, 7]]
# lst2 = lst1
# print(lst1 + lst2) #Складывание списка
# lst1[0] = 7777777
# print(lst1 + lst2) # Изменение значение списка,
#     # Несмотря на то, что lst1 присвоено lst2,
#     # то все значения, которые будут изменены в
#     # дальнейшем будут изменяться в обоих списках.
#     # При присвоении одного спика к другому то список
#     # остается один и тот же
# lst2 = lst1[:] # Создание нового списка

# lst1 = [1, 2, 3, True]
# lst2 = lst1 * 1
# print(lst1)
# print(lst2)
# lst1[0] = 8888
# print(lst1)
# print(lst2)

# Создание нового списка, каждый элемент которого является суммой
# первого списка с накопление [1, 2, 3, 4, 5] == [1, 3, 6, 10, 15]
# lst = [1, 2, 3, 4, 5]
# res = []
# for i, j in enumerate(lst):
#     sum_1 = 0
#     for k in range(i + 1):
#         sum_1 += lst[k]
#     res.append(sum_1)
# print(res)
# # Второй вариант решения
# lst = [1, 2, 3, 4, 5]
# res = []
# sum_1 = 0
# for i, j in enumerate(lst):
#     sum_1 += lst[i]
#     res.append(sum_1)
# print(res)
# # Третий вариант решения
# lst = [1, 2, 3, 4, 5]
# res = []
# for i, j in enumerate(lst):
#     res.append(sum(lst[0:i + 1]))
# print(res)

# # Сумма всех чисел списка (подсписков)
# lst = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
# sum_1 = 0
# for i in lst:
#     print(i)
#     for k in i:
#         sum_1 += k
# print(sum_1)
#
# # Вывод одного списка целиком из всех подсписков
# lst = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
# res = []
# for sub in lst:
#     res += sub
# print(res)

# msg = "Happy New Year!"
# for k in range(1, len(msg)):
#     print(-k, msg[k], end='')
#
# print(msg[::-1]) # Обратный порядок

# s = 'Abra cad abra'
# print('ad' in s) # Проверка входит ли строка
# print(s.find('ad')) # Поиск с какого индекса начинается необходимое значение
# print(len(s)) # Поиск длинны строки
# print(s.count('br')) # Поиск вхождения подстроки (сколько раз встречается узананная буква, цифра, сочитание
# print(s.upper(), s.lower()) # Большие букв/Маленькие буквы
# print(s.islower(), '123'.isdigit())
# print(str(123), str(True), str([1, 2, 3])) #Перевод в строковый тип данных
# print(s.split()) # Разбиение строки на элементы (Abra, cad, abra). Без параметров разделяет на слова.
# print(s.split('a'))# С параметрами разбивает строку на элеметы до знака, убирает знак и продолжает до знака
# print(dir(str)) # Функции str

# s = input()
# s_1 = s[::-1]
# if s_1 == s: print('True')
# else: print('False')


# lst = ['Я','пишу','программы','на','Питоне']
# print(' '.join(lst)) # Строка с одиним пробел после каждого элемента
# print(''.join(lst)) # Строка без пробелов после каждого элемента
# print(','.join(lst)) # Строка с запятой и пробелом после каждого элемента
# print('\n'.join(lst)) # Перенос строки после каждого элемента
# print('*'.join(lst)) # Звездочка после каждого элемента
# print('\t'.join(lst)) # Табуляция после каждого элемента
#
# print('Я пишу программы на Питоне'.split())
# print('Я пишу программы на Питоне'.split(''))
# print('Я пишу программы на Питоне'.split(maxsplit = 1))

# print(list('abc')) # Возвращает список
# print(list(123)) # Ошибка
# print(list([123])) # Возвращает список
# print(list((123))) # Возаращает список
# print(list({123})) # Возвращает список

# list.append() # Добавить в конец списка один элемент
# list.clear() # Очистить список
# list.copy() # Копировать список
# list.count() # Количество значений в списке
# list.extend() # Добавление элементов в список списком, тоже самое, что сложение двух списков
# list.index() # Поиск индекса числа
# list.insert() # Вставка в любой момент
# list.pop() # Выдать в качестве результата последний элемент и убрать его из списка
# list.remove() # Удаление элемента из списка
# list.reverse() # Возвращение списка в обратном порядке
# list.sort() # Сортировка списка с изменением списка
# list.sorted() # Сортировка списка без изменения самого списка

# Сгенерировать список последовательности чисел, где каждое число
# повторяется согласно порядковому номеру [1, 2, 2, 3, 3, 3, ..., n)
# n = int(input())
# lst = []
# for i in range(1, n+1):
#     lst.extend([i]*i)
# print(lst)
#
# n = int(input())
# lst = []
# for i in range(1, n+1):
#     for j in range(i):
#         lst.append(i)
# print(lst)

# max - максмальный
# min - минимальный
# sum - сумма

# # Программа формирующая и печатающая список
# n = 'abcdefghijklmnopqrstuvwxyz'
# lst = []
# for i in range(26):
#     lst.append(n[i] * (i + 1))
# print(lst)

# i = 0
# while i < 5:
#     print(i)
#     i += 2
# else: print('Else')

# Посчитать сумму строки до первого отрицательного числа
# sum_1 = 0
# while True: # Бесконечный цикл из которого надо обязательно выйти
#     x = int(input())
#     if x < 0:
#         break
#     sum_1 += x
# print(sum_1)
