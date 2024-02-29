class Person:
    def __init__(self, surname, name, fathername):
        self.surname = surname
        self.name = name
        self.fathername = fathername

    def info(self):
        print(f'{self.surname} {self.name} {self.fathername}')
        print(f'{self.surname}{self.name}{self.fathername}'[::-1])

person = Person('Иванов', 'Михаил', 'Федорович')
person.info()