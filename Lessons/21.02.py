# some = ([1, 2], [3, 4], [5, 6])
# try:
#     some[2] += [7, 8]   # при отдельном запуске будет ошибка
# except TypeError:
#     print(some)

# import re
# print(re.findall(r'<.*>', '<first><second><third>'))   # жадный поиск (целиком хватает всё)
# print(re.findall(r'<.*?>', '<first><second><third>'))   # ленивый поиск (хватает по первому элементу)
# print(re.findall(r'a.*a', 'abracadabra'))
# print(re.findall(r'a.*?a', 'abraacaadaabra'))

# Задание 1
# import re
# text = 'Московский государственный областной университет'
# print(re.sub(r'\b\w+\b', lambda x: x.group().title()[0], text).replace(' ', ''))

# Задание 2
# import re
# text = ' '.join([str(i) for i in range(123)])
# s = ''
# n = int(input())
# for i in range(n+1):
#     s += r'\b' + str(i) + r'\b' + '|'
# print(s)


# import re
# text = ' '.join([str(i) for i in range(123)])
# s = ''
# n = input()
# x = int(n[0])
# y = n[1]
# print(x, y)
# # r'\b\d\b'   # однозначные числа
# # print(re.findall(r'\b\d\b', text))
# # print(re.findall(r'\b1\d\b', text))   # все значения с 1
# # print(re.findall(r'\b2\d\b', text))   # все значения с 2
# # print(re.findall(r'\b3\d\b', text))   # все значения с 3
# # print(re.findall(r'\b[1-3]\d\b', text))   # все значения от 1 до 3
# # print(re.findall(r'\b4[0-5]\b', text))   # все значенич начинающиеся с 4 и заканчивающиеся на 5
# print(re.findall(rf'\b\d\b|\b[0-{x-1}]\d\b|\b{x}[0-{y}]\b', text))

# Задание 3
# def dec(fun):
#     def wra(text):
#         return fun(text).lower()
#     return wra
# @dec
# def hello(text):
#     return text
# print(hello('ТекСТ ДолЖЕН быть В НИЖнем РеГИСТре'))

# Некоторые полезные функции
# import re
# поиск по тем значениеям, после заданного слова
# print(re.findall(r'Isaac\d (?=Asimov)', 'Isaac1 Asimov, Isaac2 Newton'))
# print(re.findall(r'Isaac\d (?!Asimov)', 'Isaac1 Asimov, Isaac2 Newton'))

# print(re.findall(r'(?<=abc)def\d', 'abcdef1, absdef2'))
# print(re.findall(r'(?<!abc)def\d', 'abcdef1, absdef2'))

# import re
# text = '1   + 2222 * 888 / 1111 -  4444'
# print(re.split(r'[ +/*-]+', text))

# import re
# text = 'Косой косой косил волос на осине'
# print(re.findall(r'\b\w+ос\w+\b', text))

# def fu(*args, **kwargs):
#     print(args)   # позиционный аргумент
#     print(kwargs)   # именованный аргумент
#     res = 0
#     for x in args:
#         if type(x) == int:
#             res += x
#     for x in kwargs:
#         if type(kwargs[x]) == int:
#             res += kwargs[x]
#     return res
# print(fu(1, 2, 'abc', a = 3, b = 'def'))
# print(fu('1', '2', '3', x = '4', y = 5))

# def dec(fun):
#     def wra(*args, **kwargs):
#         val = fun(*args, **kwargs)
#         # декорируется возвращаемое значение функции
#         return val
#     return wra


# import time
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         print(start)
#         val = func(*args, **kwargs)
#         end = time.perf_counter()
#         print(end)
#         work_time = end - start
#         print(f'Время выполнения {func.__name__}: {round(work_time, 4)} сек.')
#         return val
#     return wrapper
# @timer   # декорирование первой функции
# def test(n): return sum([(i / 99) ** 2 for i in range(n)])
#
# @timer   # декорирование второй функции
# def sleep(n):
#     time.sleep(n)
#     return n * n
# # res1 = test(10000)
# # res2 = sleep(4)
# # print(f'Результат функции test = {res1}')
# # print(f'Результат функции sleep = {res2}')
#
# # print('Результат функции test', test(1000000))
# # print('Результат функции sleep', sleep(4))   # функция sleep никакого значения не возвращает, поэтому будет None
# # после добавлени return в функцию sleep, None поменяется на значение возвращения функции
# print('Результат функции sleep', sleep(4))

# Задание на склеивание переменных
# def dec(func):
#     def wra(*args):
#         res = ''
#         for i in args:
#             res += i
#         val = func(*args)
#         return res
#     return wra
# @dec
# def text(*args):
#     return
# print(text('xxx', 'yyy', 'zzz'))

# Задание
# Создание декоратора, который перед запуском:
# записывает функцию в файл, время старта, ее имя, слово Start
# после окончания функции записывает функцию в файл, врем я окончания, ее имя, слово Finish
# import time
# def dec(func):
#     def wra():
#         with open('File/log.txt', 'a') as f:
#             print(time.ctime(), func.__name__, 'Start', file=f)
#         func()
#         with open('File/log.txt', 'a') as f:
#             print(time.ctime(), func.__name__, 'Finish', file=f)
#         return
#     return wra
# @dec
# def function():
#     time.sleep(5)
# @dec
# def no_function():
#     time.sleep(8)
# function()
# no_function()
# print('Done')

# ООП в Python (Объектно-ориентированное программирование)
# совокупность объектов, каждый из которых является экземпляром определенного класса,
# а классы образуют иерархию наследования
# класс - тип данных из мотодов (функции для работы с полями) и полей (переменные элементарных типов)
# объект - экземпляр

# class Person:   # Класс
#     # метод
#     def __init__(self, name, money):   # почти каждый класс должен содержать данную конструкцию
#         # self обязателен (ссылка на сам объект) первый параметр
#         self.name = name
#         self.money = money
#     # метод 2, позволяющий вычислить сколько денег кто и кому дает
#     def give_money(self, other, x_money):   # self - кто дает, кому дает, сколько дает
#         if self.money >= x_money:   # проверка на то, есть ли что передавать или нет
#             self.money -= x_money   # self дает деньги и поэтому уменьшается на x
#             other.money += x_money   # other получает деньги, поэтому x увеличивается
#             print('ОК')
#         else:
#             print('Недостаточно средств')
#
# a = Person('Pete', 200)   # экземпляр класса
# b = Person('Nick', 300)   # еще один экземляр класса
# print(a.name, a.money, type(a.money))
# print(b.name, b.money, type(b.money))
# # a.money = 400   # изменение значения money
# # a.name = 'Piter'   # изменение значения name
# # print(a.name, a.money)
#
# a.give_money(b, 100)   # self.give_money(other, x)
# # Pete дает 100 Nick
# print(a.money, b.money)
#
# b.give_money(a, 120)
# # Nick возвращает деньги Pete
# print(a.money, b.money)
#
# a.give_money(a, 500)
# print(a.money)


# class Person:   # Класс
#     # метод
#     def __init__(self, name, money):   # почти каждый класс должен содержать данную конструкцию
#         # self обязателен (ссылка на сам объект) первый параметр
#         self.name = name
#         self.money = money
#     # метод 2, позволяющий вычислить сколько денег кто и кому дает
#     def give_money(self, other, x_money):   # self - кто дает, кому дает, сколько дает
#         if self.money >= x_money:   # проверка на то, есть ли что передавать или нет
#             self.money -= x_money   # self дает деньги и поэтому уменьшается на x
#             other.money += x_money   # other получает деньги, поэтому x увеличивается
#             print('Средства переданы. Транзакция успешна')
#         else:
#             print('Недостаточно средств')
#
#     # метод для вывода печати имени и количества денег у Person
#     def info(self):
#         print(f'{self.name} имеет {self.money} денежных единиц')
#     # метод выравнивания денег между Person
#     def rovn(self, other):
#         self.money = (self.money + other.money) / 2
#         other.money = self.money
#         self.info()
#         other.info()
#
# a = Person('Pete', 200)
# b = Person('Nick', 300)
# # a.info()
# # b.info()
# # a.give_money(b, 50)
# # a.info()
# # b.info()
# # a.height = 180   # присваивание нового атрибута экземляру класса
# # print(a.height)
# # # при печати b.height - будет ошибка
# # Person.height = 190   # присваивание нового атрибута всему классу
# # print(a.height, b.height)
# a.rovn(b)   # вызов метода выравнивания денежный средств


class Pet:
    def __init__(self, name, mass, level):
        self.name = name
        self.mass = mass
        self.level = level
    def info(self):
        print(f'{self.name}, {self.mass}, {self.level}')
    def hungry(self):
        if self.level < 5:
            return self.name, self.level, 'Голоден'
        elif self.level > 10:
            return self.name, self.level, 'Сыт'
        return self.name, self.level, 'Поел'
    def feed(self, eat):
        self.level += eat

a = Pet('Мухтар', 10, 3)
b = Pet('Тузик', 5, 5)
c = Pet('Шарпей', 7, 10)
print(a.hungry(), b.hungry(), c.hungry())
a.feed(5)
print(a.hungry(), b.hungry(), c.hungry())
a.feed(4)
c.feed()
print(a.hungry(), b.hungry(), c.hungry())
print(a.hungry(), b.hungry(), c.hungry())

