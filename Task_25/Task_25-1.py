from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
class MainWindow(QMainWindow):   # Под класс QMainWindow для настройки главного окна
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Моё приложение')
        self.count = 0
        self.button = QPushButton('Hello world!')
        self.button.clicked.connect(self.the_button_was_clicked)
        self.setCentralWidget(self.button)   # Установка центрального виджета Windows
    def the_button_was_clicked(self):
        self.count += 1
        self.button.setText('Нажато: ' + str(self.count))

app = QApplication([])
window = MainWindow()
window.show()   # запускаем цикл событий
app.exec()