# xyz = 1,000,000
# print(xyz)
#
# # x y z = 1000 2000 3000
# # print(x y z)
#
# x, y, z = 1000, 2000, 3000
# print(x, y, z)
#
# x_y_z = 1_000_000
# print(x_y_z)
#
# lst = [1, 0, 2, 0, 'hi', '', [], [False]]
# res = list(filter(bool, lst))
# print(res)

# def fun1(par):
#     return par * 2
# def fun2(par):
#     return arg * 2
# arg = 100
# # print(fun1(arg), fun2(arg))
#
# x = 200
# print(fun1(x), fun2(x))


# from PyQt6.QtWidgets import QApplication, QWidget
# app = QApplication([])   # Приложение
# window = QWidget()   # класс, от которого унаследованы все виджеты
# window.show()   # окно по умолчанию открыто
# app.exec()   # запускаем цикл событий, которые обрабатывает приложение
# # Приложение не доберется сюда, пока вы не выйдете и цикл событий не остановится

# КНОПКА PUSH ME
# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
# app = QApplication([sys.argv])
# window = QPushButton('Push Me')
# window.show()
# app.exec()

# ОКНО
# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow
# app = QApplication(sys.argv)
# window = QMainWindow()
# window.show()   # запускаем цикл событий
# app.exec()


# Class QMainWimdow (добавили имя для окна
# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.setWindowTitle('Моё приложение')
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()   # запускаем цикл событий
# app.exec()

# Окно фиксированного размера с кнопкой
# from PyQt6.QtCore import QSize, Qt
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
# class MainWindow(QMainWindow):   # Под класс QMainWindow для настройки главного окна
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Моё приложение')
#         button = QPushButton('Press Me!')
#         self.setFixedSize(QSize(400, 300))
#         self.setCentralWidget(button)   # Установка центрального виджета Windows
# app = QApplication([])
# window = MainWindow()
# window.show()   # запускаем цикл событий
# app.exec()

# Нажатие кнопки (сигналы и слоты)
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
# class MainWindow(QMainWindow):   # Под класс QMainWindow для настройки главного окна
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Моё приложение')
#         self.button = QPushButton('Press Me!')
#         self.button.setCheckable(True)
#         self.button.clicked.connect(self.the_button_was_clicked)
#         self.setCentralWidget(self.button)   # Установка центрального виджета Windows
#     def the_button_was_clicked(self):
#         print('Нажата кнопка "Press Me!"')
# app = QApplication([])
# window = MainWindow()
# window.show()   # запускаем цикл событий
# app.exec()


# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
# class MainWindow(QMainWindow):   # Под класс QMainWindow для настройки главного окна
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Моё приложение')
#         self.count = 0
#         self.button = QPushButton('Press Me!')
#         self.button.clicked.connect(self.the_button_was_clicked)
#         self.setCentralWidget(self.button)   # Установка центрального виджета Windows
#     def the_button_was_clicked(self):
#         self.count += 1
#         print('Нажата кнопка "Press Me!"' + str(self.count))
#         self.setWindowTitle('Clicked')
#
# app = QApplication([])
# window = MainWindow()
# window.show()   # запускаем цикл событий
# app.exec()


# Одноразовая кнопка
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
# class MainWindow(QMainWindow):   # Под класс QMainWindow для настройки главного окна
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Моё приложение')
#         self.count = 0
#         self.button = QPushButton('Press Me!')
#         self.button.clicked.connect(self.the_button_was_clicked)
#         self.setCentralWidget(self.button)   # Установка центрального виджета Windows
#     def the_button_was_clicked(self):
#         self.button.setText('You already clicked me')
#         self.button.setEnabled(False)
#         # print('Нажата кнопка "Press Me!"' + str(self.count))
#         self.setWindowTitle('Clicked')
#
# app = QApplication([])
# window = MainWindow()
# window.show()   # запускаем цикл событий
# app.exec()

# Задание. Название кнопки Hello world! меняется на Привет, мир! и наоборот
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
# class MainWindow(QMainWindow):   # Под класс QMainWindow для настройки главного окна
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Моё приложение')
#         self.count = 0
#         self.button = QPushButton('Hello world!')
#         self.button.clicked.connect(self.the_button_was_clicked)
#         self.setCentralWidget(self.button)   # Установка центрального виджета Windows
#     def the_button_was_clicked(self):
#
#         self.count += 1
#         if self.count % 2 != 0:
#             self.button.setText('Привет, мир! ' + str(self.count))
#         else: self.button.setText('Hello world! ' + str(self.count))
#         # self.button.setEnabled(False)
#         # print('Нажата кнопка "Press Me!"' + str(self.count))
#         # self.setWindowTitle('Clicked')
#
# app = QApplication([])
# window = MainWindow()
# window.show()   # запускаем цикл событий
# app.exec()

# Калькулятор
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QHBoxLayout,
                             QVBoxLayout, QWidget, QLineEdit, QTextEdit)
class MainWindow(QMainWindow):   # Под класс QMainWindow для настройки главного окна
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        w, h = 200, 25
        self.line1 = QLineEdit()
        self.line1.setFixedSize(QSize(w, h))

        self.line2 = QLineEdit()
        self.line2.setFixedSize(QSize(w, h))

        self.button_add = QPushButton('a + b')
        self.button_add.setFixedSize(QSize(w,h))
        self.button_add.clicked.connect(self.the_button_add)

        self.button_sub = QPushButton('a - b')
        self.button_sub.setFixedSize(QSize(w,h))
        self.button_sub.clicked.connect(self.the_button_sub)

        self.button_mul = QPushButton('a * b')
        self.button_mul.setFixedSize(QSize(w,h))
        self.button_mul.clicked.connect(self.the_button_mul)

        self.button_div = QPushButton('a / b')
        self.button_div.setFixedSize(QSize(w,h))
        self.button_div.clicked.connect(self.the_button_div)

        self.button_rem = QPushButton('a % b')
        self.button_rem.setFixedSize(QSize(w,h))
        self.button_rem.clicked.connect(self.the_button_rem)

        self.button_int_div = QPushButton('a // b')
        self.button_int_div.setFixedSize(QSize(w,h))
        self.button_int_div.clicked.connect(self.the_button_int_div)

        self.label = QLabel('= ')
        self.label.setFixedSize(QSize(w, h))
        font = self.label.font()
        font.setPointSize(15)
        self.label.setFont(font)

        self.qte = QTextEdit()
        self.qte.setFixedSize(QSize(200, 70))

        layout = QVBoxLayout()   # Расположение QHBoxLayout - горизонтальное расположение
        widgets = [self.line1, self.line2, self.label, self.button_add, self.button_sub,
                   self.button_mul, self.button_div, self.button_int_div, self.button_rem,
                   self.qte]
        for w in widgets:
            layout.addWidget(w)

        widgets = QWidget()
        widgets.setLayout(layout)
        self.setCentralWidget(widgets)
    def the_button_add(self):
        try:
            res = '= ' + str(eval(self.line1.text() + '+' + self.line2.text()))
        except:
            res = 'Mistake!'
        self.label.setText(res)
        self.qte.append(res)

    def the_button_sub(self):
        try:
            res = '= ' + str(eval(self.line1.text() + '-' + self.line2.text()))
        except:
            res = 'Mistake!'
        self.label.setText(res)
        self.qte.append(res)

    def the_button_mul(self):
        try:
            res = '= ' + str(eval(self.line1.text() + '*' + self.line2.text()))
        except:
            res = 'Mistake!'
        self.label.setText(res)
        self.qte.append(res)

    def the_button_div(self):
        try:
            res = '= ' + str(eval(self.line1.text() + '/' + self.line2.text()))
        except:
            res = 'Mistake!'
        self.label.setText(res)
        self.qte.append(res)

    def the_button_rem(self):
        try:
            res = '= ' + str(eval(self.line1.text() + '%' + self.line2.text()))
        except:
            res = 'Mistake!'
        self.label.setText(res)
        self.qte.append(res)

    def the_button_int_div(self):
        try:
            res = '= ' + str(eval(self.line1.text() + '//' + self.line2.text()))
        except:
            res = 'Mistake!'
        self.label.setText(res)
        self.qte.append(res)


app = QApplication([])
window = MainWindow()
window.show()   # запускаем цикл событий
app.exec()