import random
class Tasks:   # Класс для хранения тем обучения
    def __init__(self, spisok):
        self.spisok = spisok   # в виде списка


class Solution():
    def __init__(self, name):
        self.knowledge = []
        self.name = name
        self.work = 0
        self.k = 0

    def solution(self):
        for i in self.knowledge:
            # k = random.choice(['Решил', 'Не решил'])
            print(f'{self.name} решил {i}')
        return

    def solution_t(self, task):
        print(f'{self.name} правильно решил {self.knowledge[task-1]}')

    def solution_n(self, task):
        print(f'{self.name} не правильно решил {self.knowledge[task-1]}')

    def check(self, pupil, chec, task):
        if chec == 'Правильно': pupil.solution_t(task)
        else: pupil.solution_n(task)

class Teacher(Solution):   # класс учителей
    def __init__(self, name):
        super().__init__(name)

    def teach_individual(self, info, pupil):   # индивидуальное обучение
        pupil.take(info)   # вызов метода ученика получения информации
        self.work += 1

    def teach_group(self, info):   # групповое обучение
        for i in Pupil.group:   # цикл по списку учеников
            i.take(info)   # вызов метода ученика получения инфы
            self.work += 1

class Pupil(Solution):   # класс учеников
    group = []   # список учеников

    def __init__(self, name):
        super().__init__(name)
        Pupil.group.append(self)

    def take(self, info):   # метод получения информации
        self.knowledge.append(info)

    def info(self):   # метод печати, что ученик выучил
        print(self.name, end=f' получил задачи: ')
        for i in self.knowledge:
            print(i, end=', ')
            self.k += 1
        print()

Task = Tasks(['Task 1. Class',
              'Task 2. Object',
              'Task 3. Inheritance',
              'Task 4. Polymorphism',
              'Task 5. Encapsulation'])


Teach = Teacher('Ivan')
vasya = Pupil('Vasya')
petya = Pupil('Petya')
misha = Pupil('Misha')

Teach.teach_individual(Task.spisok[2], vasya)   # дать Васю задачу 3
Teach.teach_individual(Task.spisok[4], misha)   # дать Мише задачу 5
Teach.teach_group(Task.spisok[1])    # дать ученикам задачу 2

vasya.info()
petya.info()
misha.info()
print()
vasya.solution()
petya.solution()
misha.solution()
print()
Teach.check(vasya, 'Правильно', 1)
Teach.check(vasya, 'Правильно', 2)
Teach.check(petya, 'Не правильно', 1)
Teach.check(misha, 'Правильно', 2)
Teach.check(misha, 'Не правильно', 1)
print()
