# a = [1, 2]
# a += '345'
# a += {1: 11, 2: 22}
# print(a)
# # работает метод __iadd__.
# # К списку а прибавляет шинкуя str на отдельные символы, как и словари (по ключам) и т.д.

# a = [1, 2]
# a = a + '34'
# print(a)
# # работает метод __add__. Т.к. типы разные, то ошибка


# from PyQt6.QtCore import QSize, Qt
# from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QHBoxLayout,
#                              QVBoxLayout, QWidget, QLineEdit, QTextEdit)
# class MainWindow(QMainWindow):   # Под класс QMainWindow для настройки главного окна
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.setWindowTitle('My App')
#
#         widget = QLineEdit()
#         widget.setMaxLength(10)
#         widget.setPlaceholderText('Énter your text')
#
#         # widget.setReadOnly(True)   # раскомментируйте, чтобы сделать доступным только для чтения
#
#         widget.returnPressed.connect(self.return_pressed)
#         widget.selectionChanged.connect(self.selection_changed)
#         widget.textChanged.connect(self.text_changed)
#         widget.textEdited.connect(self.text_editer)
#
#         self.setCentralWidget(widget)
#
#     def return_pressed(self):
#         print('Return pressed!')
#
#     def selection_changed(self):
#         print('Selection changed')
#
#     def text_changed(self, s):
#         print('Text changed...')
#         print(s)
#
#     def text_editer(self, s):
#         print('Text editer!')
#         print(s)
#
# app = QApplication([])
# window = MainWindow()
# window.show()   # запускаем цикл событий
# app.exec()

# from PyQt6.QtCore import QSize, Qt
# from PyQt6.QtWidgets import (
#         QApplication, QMainWindow,
#         QSpinBox, QLabel, QComboBox,
#         QCheckBox, QDoubleSpinBox, QSlider,
#         QGridLayout, QPushButton, QWidget,
#         QLineEdit)
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.setWindowTitle('My App')
#
#         layout = QGridLayout()
#         button = QPushButton('Button')
#         le = QLineEdit('LineEdit')
#         label = QLabel('Label')
#         combo = QComboBox()
#
#         combo.addItems(['First', 'Second', 'Third'])
#         layout.addWidget(button, 0, 0)
#         layout.addWidget(le, 0, 1)
#         layout.addWidget(label, 1, 0)


# Калькулятор, расположение кнопок
# from PyQt6.QtCore import QSize, Qt
# from PyQt6.QtWidgets import (
#     QApplication, QMainWindow, QPushButton,
#     QLabel, QHBoxLayout, QVBoxLayout, QWidget,
#     QLineEdit, QTextEdit, QSpinBox, QComboBox,
#     QCheckBox, QDoubleSpinBox, QSlider,
#     QGridLayout)
# class MainWindow(QMainWindow):   # Под класс QMainWindow для настройки главного окна
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Calculator')
#         w, h = 200, 25
#         self.line1 = QLineEdit()
#         self.line1.setFixedSize(QSize(w, h))
#
#         self.line2 = QLineEdit()
#         self.line2.setFixedSize(QSize(w, h))
#
#         self.button_add = QPushButton('a + b')
#         self.button_add.setFixedSize(QSize(w,h))
#         self.button_add.clicked.connect(self.the_button_add)
#
#         self.button_sub = QPushButton('a - b')
#         self.button_sub.setFixedSize(QSize(w,h))
#         self.button_sub.clicked.connect(self.the_button_sub)
#
#         self.button_mul = QPushButton('a * b')
#         self.button_mul.setFixedSize(QSize(w,h))
#         self.button_mul.clicked.connect(self.the_button_mul)
#
#         self.button_div = QPushButton('a / b')
#         self.button_div.setFixedSize(QSize(w,h))
#         self.button_div.clicked.connect(self.the_button_div)
#
#         self.button_rem = QPushButton('a % b')
#         self.button_rem.setFixedSize(QSize(w,h))
#         self.button_rem.clicked.connect(self.the_button_rem)
#
#         self.button_int_div = QPushButton('a // b')
#         self.button_int_div.setFixedSize(QSize(w,h))
#         self.button_int_div.clicked.connect(self.the_button_int_div)
#
#         self.label = QLabel('= ')
#         self.label.setFixedSize(QSize(w, h))
#         font = self.label.font()
#         font.setPointSize(15)
#         self.label.setFont(font)
#
#         self.qte = QTextEdit()
#         self.qte.setFixedSize(QSize(200, 70))
#
#         layout = QGridLayout()   # Расположение QHBoxLayout - горизонтальное расположение
#         widgets = [self.line1, self.line2, self.label, self.button_add, self.button_sub,
#                    self.button_mul, self.button_div, self.button_int_div, self.button_rem,
#                    self.qte]
#         # for w in widgets:
#         #     layout.addWidget(w)
#         #  Расположение кнопок по желанию
#         layout.addWidget(self.line1, 0, 0)
#         layout.addWidget(self.line2, 0, 1)
#         layout.addWidget(self.label, 1, 0)
#         layout.addWidget(self.button_add, 2, 0)
#         layout.addWidget(self.button_sub, 2, 1)
#         layout.addWidget(self.button_mul, 3, 0)
#         layout.addWidget(self.button_div, 3, 1)
#         layout.addWidget(self.button_rem, 4, 0)
#         layout.addWidget(self.button_int_div, 4, 1)
#         layout.addWidget(self.qte, 5, 0-1)
#
#         widgets = QWidget()
#         widgets.setLayout(layout)
#         self.setCentralWidget(widgets)
#     def the_button_add(self):
#         try:
#             res = '= ' + str(eval(self.line1.text() + '+' + self.line2.text()))
#         except:
#             res = 'Mistake!'
#         self.label.setText(res)
#         self.qte.append(res)
#
#     def the_button_sub(self):
#         try:
#             res = '= ' + str(eval(self.line1.text() + '-' + self.line2.text()))
#         except:
#             res = 'Mistake!'
#         self.label.setText(res)
#         self.qte.append(res)
#
#     def the_button_mul(self):
#         try:
#             res = '= ' + str(eval(self.line1.text() + '*' + self.line2.text()))
#         except:
#             res = 'Mistake!'
#         self.label.setText(res)
#         self.qte.append(res)
#
#     def the_button_div(self):
#         try:
#             res = '= ' + str(eval(self.line1.text() + '/' + self.line2.text()))
#         except:
#             res = 'Mistake!'
#         self.label.setText(res)
#         self.qte.append(res)
#
#     def the_button_rem(self):
#         try:
#             res = '= ' + str(eval(self.line1.text() + '%' + self.line2.text()))
#         except:
#             res = 'Mistake!'
#         self.label.setText(res)
#         self.qte.append(res)
#
#     def the_button_int_div(self):
#         try:
#             res = '= ' + str(eval(self.line1.text() + '//' + self.line2.text()))
#         except:
#             res = 'Mistake!'
#         self.label.setText(res)
#         self.qte.append(res)
#
#
# app = QApplication([])
# window = MainWindow()
# window.show()   # запускаем цикл событий
# app.exec()


# МЕНЮ, ТУЛБАР
# import sys
# from PyQt6.QtGui import QIcon, QAction
# from PyQt6.QtWidgets import (
#         QApplication, QMainWindow, QTextEdit)
#
# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#     def initUI(self):
#         textEdit = QTextEdit()
#         self.setCentralWidget(textEdit)
#
#         exitAction = QAction(QIcon('File/t1.png'), 'Exit', self)
#         exitAction.setShortcut('Ctrl + Q')
#         exitAction.setStatusTip('Exit application')
#         exitAction.triggered.connect(self.close)
#
#         self.statusBar()
#
#         menubar = self.menuBar()
#         fileMenu = menubar.addMenu('&File')
#         fileMenu.addAction(exitAction)
#
#         fileMenu2 = menubar.addMenu('&Edit')
#         fileMenu2.addAction(exitAction)
#
#         toolbar = self.addToolBar('Exit')
#         toolbar.addAction(exitAction)
#
#         self.setGeometry(300, 300, 350, 250)
#         self.setWindowTitle('Main Window')
#         self.show()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec())


# MOUSE - движение и действие мыши
# from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.label = QLabel('Click in the window')
#         self.setCentralWidget(self.label)
#
#     def mouseMoveEvent(self, e):
#         self.label.setText('mouseMoveEvent')
#
#     def mousePressEvent(self, e):
#         self.label.setText('mousePressEvent')
#
#     def mouseReleaseEvent(self, e):
#         self.label.setText('mouseReleaseEvent')
#
#     def mouseDoubleClickEvent(self, e):
#         self.label.setText('mouseDoubleClickEvent')
#
# app = QApplication([])
# window = MainWindow()
# window.show()   # запускаем цикл событий
# app.exec()

# ООП - работа с атрибутами
# class AnyClass:
#     def __init__(self):
#         self.a = 'Public'
#         self._b = 'Protected'
#         self.__c = 'Private'
# inst = AnyClass()
# print(inst.a)
# print(inst._b)   # как бы защищенный, но лучше не использовать
# # print(inst.__c)   # не использовать дандер (два нижний поддеркивания) в начале переменной
# # print(inst.__dict__)   # все атрибуты
# print(inst._AnyClass__c)

# ДОСТУП К АТРИБУТАМ
# class Person:
#     def __init__(self, name):
#         self.__name = name   # установление имени
#         self.__age = 1   # установление возраста
#
#     def set_age(self, age):
#         if 1 < age < 110:
#             self.__age = age
#         else:
#             print('Недопустимый возраст')
#
#     def get_age(self):
#         return self.__age
#
#     def get_name(self):
#         return self.__name
#
#     def display_info(self):
#         print(f'Имя: {self.__name}\tВозраст: {self.__age}')
#
# tom = Person('Tom')
# tom.display_info()   # Имя: Tom Возраст: 1
# tom.set_age(25)
# tom.display_info()   # Имя: Tom Возраст: 25
# # tom.__name
# # tom._Person__name
# # set - установить, get - получить

# Декоратор @property
# class Cat:
#     def __init__(self, name, age):
#         self.__name = name   # имя кошки
#         self.__age = age
#
#     @property
#     def name(self):   # геттер свойства name
#         return self.__name
#     @property
#     def age(self):
#         return self.__age
#
#     @name.setter
#     def name(self, other_name):   # сеттер свойства name
#         if (isinstance(other_name, str)
#             and other_name.isalpha()
#             and other_name == other_name.title()
#             and self.__name == self.__name.title()):
#             self.__name = other_name
#         else:
#             print('Некорректное имя')
#     @age.setter
#     def age(self, other_age):
#         if other_age < 15:
#             self.__age = other_age
#         else:
#             print('Некорректный возраст')
#
#     @name.deleter
#     def name(self):   # делитер свойства name
#         del self.__name
#     @age.deleter
#     def age(self):
#         del self.__age
#
#     # def __getattribute__(self, attr):   # проходит всеи то, чего нет, и то, что есть
#         # if attr in self.__dict__:
#             # return self.name.upper()
#
#     def __getattr__(self, attr):   # работает для тех атрибутов, которых нет в классе
#         if attr == 'color':
#             return 'Black'
#         elif attr == 'weight':
#             return 10
#
# # c = Cat('Persik', 10)   # Присвоение имени котику
# # print(c.name, c.age, c.color, c.weight)
# # c.name = 'Kotik'   # Переименование имени котика
# # print(c.name, c.age)
# # c.age = 11   # Изменение возраста котика
# # print(c.name, c.age)
# # del c.name   # Удаление имени котика
# # print(c.name)
# c = Cat('Persik', 5)
# print(c.name)

# @property декоратор может быть использован для определения методов в классе,
# которые действуют как атрибуты
# В этих методах можно реализовать разнообразные полезные функции


# МЕТОД __satattr__
# class SomeClass():
#     age = 42
#     def __setattr__(self, name, value):
#         print(name, value)
#         self.__dict__[name] = value
#         # self.age = value   #рекурсия
#
# obj = SomeClass()
# print(obj.age)
# obj.age = 100
# print(obj.age)   # Вызовет метод __steattr__


# УДАЛЕНИЕ АТРИБУТА __delattr__
# class SomeClass():
#     def __init__(self):
#         self.speed = 100
#     def __delattr__(self, item):
#         self.speed = 42
#
# # Создаем объект
# porsche = SomeClass()
# print(porsche.speed)
# delattr(porsche, 'speed')   # удаление атрибута у объекта
# print(porsche.speed)

# Класс - объект
# type() - МЕТАКЛАССЫ

# class Foo():
#     bar = True
# f = Foo()
# Foo = type('Foo', (), {'bar': True})   # Тоже самое
# # Имя класса, от кого наследуется и чем станет (словарь)
# # print(Foo)
# # print(f)
#
# class FooChild(Foo):
#     pass
# FooChild = type('Foochild', (Foo,), {})
# # print(FooChild)
#
# def echo_bar(self):
#     print(self.bar)
# FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})   # можно определить метод
#
# my_foo = FooChild()
# my_foo.echo_bar()


#  Задание
def show(self):
    print(self.age)
    print(self.name)

def __init__(self, name):
    self.name = name

Type = type('Type', (), {'age': 50, 'show': show, '__init__': __init__})
t = Type('Ivan')

t.show()
