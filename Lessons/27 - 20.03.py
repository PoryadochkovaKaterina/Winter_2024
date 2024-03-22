# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __getattribute__(self, attr):
#         print(f'Возвращаю значение атрибута {attr}')
#         if attr in self.__dict__:
#             return object.__getattribute__(self, attr)
#         else:
#             raise AttributeError
#
#     def __getattr__(self, attr):
#         print(f'Возращаю значение атрибута {attr}')
#         return None
# # обращение к словарю __dict__ приведет к бесконечным рекурсивным
# # вызовам метода __getattribute__(), так как словарь __dict__ сам явзыется атрибутом.
#
# cat = Cat('Murka')
# print(cat.name)
# print(cat.age)


# class AnyClass:
#     def __init__(self, **kwargs):
#         for i in kwargs:
#             self.__dict__[i] = kwargs[i]
#     def __str__(self):
#         s = 'AnyClass('
#         lst = []
#         for i in self.__dict__:
#             lst.append(i + ' : ' + str(self.__dict__[i]))
#         return s + ', '.join(lst) + ')'
#
# a = AnyClass(attr1 = 1, attr2 = 22, attr3 = [3, 4, 5], attr4 = ('abc', 1))
# print(a)

# МЕТАКЛАССЫ
# xyz = type('ClassA', (), {})
# x = xyz
# print(type(x))
#
# strb = 'ClassB'
# zyx = type(strb, (), {})   # В строке нет слова ClassB!
# b = zyx()   # в этой тоже нет, но b - это экземпляр класса ClassB
# print(type(b))

# Простой способ
# class Singleton:
#     def __new__(cls):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super(Singleton,cls).__new__(cls)
#         return cls.instance
#
# s1 = Singleton()
# print(Singleton.instance)
# s2 = Singleton()
# print(s1 is s2)
# s1.x = 123
# print(s2.x)

# Прототип
# import copy
# class Person:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#     def __str__(self): return f'Person {self.name} from {self.address}'
#
# John = Person('John', ['Nevsky', 25])
# # print(John)
# # Jane = John
# Jane = copy.deepcopy(John)   # Глубокая копия
# # print(Jane)
# Jane.name = 'Jane'
# # print(Jane)
# Jane.address = ['Liteiny', 44]
# print(Jane)
# print(John)

