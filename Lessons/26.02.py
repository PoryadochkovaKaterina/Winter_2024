# Инкапсуляция, Наследование, Полиморфизм, Абстракция

# Имя класса всегда с большой буквы
# внутри класса могут быть свои переменные
# class ИМЯКЛАССА:
#     переменная = значение
#     def __init__(self, x = 1, y = 'abc'):
#
#     def ИМЯМЕТОДА(self, ...):
#         self.переменная = значение

# class Figure:
#     def __init__(self, perim, colour):   # конструктор
#         print('Inside Constructor')
#         self.perim = perim
#         self.colour = colour
#         print('Object initialized')
#     def show(self):
#         print('Figure', self.perim, self.colour)
#     def ger_perim(self):
#         return self.perim
#     def __del__(self):   # Деструктор
#         print('Inside destructor')
#         print('Object destroyed')
#
# abc = Figure(123, 'Красный')   # Создать объект
# abc.show()
# del abc   # удаление объекта
# # abc.__del__()
# abc.show()

# class Figure:
#     spisok = []   # список для создания списка объектов
#     def __init__(self, perim, colour, name):   # конструктор
#         # print('Inside Constructor')
#         self.perim = perim
#         self.colour = colour
#         self.name = name
#         Figure.spisok.append(self)   # добавление объекта в список
#         for i in Figure.spisok:
#             print(i. name, i.colour, i.perim)
#         # print('Object initialized')
#         print()
#     def show(self):
#         print('Figure', self.perim, self.colour)
#     def ger_perim(self):
#         return self.perim
#
# abc = Figure(123, 'Красный', 'Кругляш')   # Создать объект
# efg = Figure(456, 'Желтый', 'Квадрат')
# fgh = Figure(785, 'Зеленый', 'Овал')

# Для определения, к какому классу относится объект, можно вызвать внутренник атрибут объекта __class__
# Так же можно воспользоваться функцией isinstance()  (рекомендуется этот вариант)

# a = []
# type(a)
# b = 123.45
# print(isinstance(b, (int, float)))

# class Animal:
#     pass
# animal  = Animal()
# print(isinstance(animal, Animal))   # определить класс объекта
#
# print(animal.__class__)
#
# print(dir(animal))   #Поля объекта

# class Tree(object):   # РОдительский класс помещается в скобки после имени класса
#     def __init__(self, kind, height):
#         self.kind = kind
#         self.age = 0
#         self.height = height
#     def grow(self):
#         self.age += 1
#
# class FruitTree(Tree):   # Объект производного класса наследуюет все свойства родительского
#     def __init__(self, kind, height):
#         super().__init__(kind, height)   # вызывается конструктор родительсткого класса
#     def give_fruits(self):
#         print(f'Collected 20kg of {self.kind}')
#
# f_tree = FruitTree('Apple', 0.7)
# print(f_tree.kind, f_tree.age)
# f_tree.grow()
# print(f_tree.kind, f_tree.age)
# f_tree.give_fruits()
# f_tree2 = FruitTree('Orange', 0.8)
# f_tree2.give_fruits()
# f_tree3 = Tree('Oak', 3)
# # f_tree3.give_fruits()

# Какие параметры пришли, такие и передаем

# class Figure:
#     def __init__(self, perim, colour):   # конструктор
#         print('Inside Constructor')
#         self.perim = perim
#         self.colour = colour
#         print('Object initialized')
#     def show(self):
#         print('Figure', self.perim, self.colour)
#     def get_perim(self):
#         return f'Периметр фигуры {self.perim}'
    # def __del__(self):   # Деструктор
    #     print('Inside destructor')
    #     print('Object destroyed')

# class Triangle(Figure):
#     def set_perim(self):
#         self.perim = self.x + self.y + self.z
#         return self.perim
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.set_perim()
#
# class Rectangle(Figure):
#     def set_perim_R(self):
#         self.perim = (self.a + self.b) * 2
#         return self.perim
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         self.set_perim_R()
#     def get_perim(self):   # Используется этот get_perim, не наследуя метод из родительского класса (перезаписывается)
#         return f'Периметр прямоугольника = {self.perim}'
#
#
# abc = Triangle(3, 4, 6)
# print(abc.get_perim())
# print(abc.perim)
# bcd = Rectangle(4, 6)
# print(bcd.get_perim())
# print(bcd.perim)

# Множественное наследование

# class Horse:
#     isHorse = True   # атрибут класса
# class Donkey:
#     isDonkey = True   # атрибут класса
# class Mule(Horse, Donkey):   # наследование сразу двух классов, последовательно как в скобках (можно менять)
#     pass
# mule = Mule()
# print(mule.isHorse)
# print(mule.isDonkey)

#  Сложение разных классов
# class X(str):
#     def __init__(self, s):
#         self.s = s
#     def __abs__(self, other):
#         return other.s.lower() + self.s.upper()
#
# class Y(int):
#     def __init__(self, s):
#         self.s = s
#     def __add__(self, other):
#         return self.s * other.s
#     def __mul__(self, other):
#         return self.s + other.s
#
# x = X('aAa')
# y = X('bbb')
# z = Y(11)
# u = Y(12)
# print(x + y)
# print(z * u)   # берет метод __mul__
# print(z + u)   # берет метод __add__


# class Car:
#     def __init__(self, model, color, vin):
#         self.model = model
#         self.color = color
#         self.VIN = vin
#
#     def __str__(self):
#         return f'Модель {self.model}'   # неформальный, человеческий метод печати (user-friendly)
#
#     def __repr__(self):
#         return f'VIN номер: {self.VIN}, цвет: {self.color}'    # более формальный, машинный метод печати
#
# car = Car('Kia Venga', 'silver', 'WB4561567861864B456BD456')
# print(car)
# print(str(car))
# # print(repr(Car))

# class SomeClass():
#     def __init__(self):
#         self.__param = 42   # приватный атрибут
#     def get_param(self):
#         return self.__param
#
# obj = SomeClass()
# # obj.__param   # AttributeError: 'SomeClass' object has no attribure '__param'
# print(obj.get_param())
# print(obj._SomeClass__param)   # обходной способ с указанием класса


# class Person:
#     def __init__(self, name):
#         self.__name = name   # устанавливаем имя
#         self.__age = 1   # устанавливаем возраст
#
#     def set_age(self, age):
#         if 1 < age < 100: self.__age = age
#         else: print('Недопустимый возраст')
#
#     def get_age(self):
#         return self.__age
#
#     def get_name(self):
#         return self.__name
#
#     def display_info(self):
#         print(f'Имя: {self.__name}. Возраст: {self.__age}')
#
#     def __str__(self):   # подготавливает для оператора print, если str нет, то будет repr, если и str, и repr, то хватает str
#         s = []
#         for k, v in self.__dict__.items():
#             s.append(str(k) + ':' + str(v))
#         return ', '.join(s)
#
#
# Tom = Person('Tom')
# # Tom.display_info()   # Имя: Том. Возраст: 1
# Tom.set_age(25)
# # Tom.display_info()   # Имя: Том. Возраст: 25
# # Tom.__name   # Ошибка, т.к. нет атрибута
# # Tom.__age
#
# # print(Tom.__dict__)   # Словарь со всем атрибутами, свойствами и их значениями
# # for k, v in Tom.__dict__.items():
# #     print(k, v)
#
# print(Tom)   # вывод из метода __str__, возвращаем пару ключ атрибута и его значение

# Учебный процесс
class Data:
    def __init__(self, spisok):
        self.spisok = spisok

class Teacher:
    def __init__(self):
        self.work = 0
    def teach_individual(self, info, pupil):   # info - элемент обучения, тут односторонний обмен
        pupil.take(info)   # pupil сам забирает эту инфу, надо еще 2 метода от учителя - ученику и обратно
        self.work += 1
    def teach_group(self, info):
        for i in Pupil.group:
            i.take(info)
            self.work += 1

class Pupil:
    group = []
    def __init__(self, name):
        self.knowladge = []
        self.name = name
        Pupil.group.append(self)
    def take(self, info):
        self.knowladge.append(info)   # внимательно
    def info(self):
        print(self.name, end=':')
        for i in self.knowladge:
            print(i, end=', ')
        print()

lesson = Data()


# Домашняя работа
# Учитель, ученик (можно Персон и потом уже дочерние Учитель, ученик)
# Можно задать список задач
# От учителя - ученику - в виде списка
# От ученика - учителю - в виде словаря
# Если одна, то просто статус
# Ученик тоже вызывает метод решения
# Учитель дает задачу, ученик меняет статус на решение, учитель смотрит как решено и возвращает обратно
# Учитывать, кто инициатор