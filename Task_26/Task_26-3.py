class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age
    @property
    def name(self):
        return self.__name

    @age.setter
    def age(self, other_age):
        if 1 < other_age < 100:
            self.__age = other_age
        else:
            print('Недопустимый возраст.')

    @age.deleter
    def age(self):
        del self.__age
    @name.deleter
    def name(self):   # делитер свойства name
        del self.__name

pers = Person('Ivan', 10)
print(pers.name, pers.age)
pers.age = 35
print(pers.name, pers.age)
pers.age = 101

# del pers.age
# print(pers.age)
