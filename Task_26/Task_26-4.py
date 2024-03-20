import sys
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QIcon, QAction, QPixmap
from PyQt6.QtWidgets import (
        QApplication, QMainWindow, QTextEdit,
        QToolBar, QLabel, QStatusBar,
        QVBoxLayout, QWidget, QPushButton)
from PyQt6.QtWebEngineWidgets import QWebEngineView

class Example(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()
        self.setWindowTitle('My app')

    def initUI(self):

        self.resize(300, 200)
        self.centralWidget = QLabel('Hello!')
        self.centralWidget.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.centralWidget)
        self.statusBar()

        self.newAction = QAction(QIcon('Icon/New.png'), '&New', self)
        self.newAction.setShortcut('Ctrl+N')
        self.newAction.setStatusTip('New aplication')
        self.newAction.triggered.connect(self.newFile)

        self.openAction = QAction(QIcon('Icon/Open.png'), '&Open', self)
        self.openAction.setShortcut('Ctrl+O')
        self.openAction.setStatusTip('Open aplication')
        self.openAction.triggered.connect(self.openFile)

        self.saveAction = QAction(QIcon('Icon/Save.png'), '&Save', self)
        self.saveAction.setShortcut('Ctrl+S')
        self.saveAction.setStatusTip('Save aplication')
        self.saveAction.triggered.connect(self.saveFile)

        self.exitAction = QAction(QIcon('Icon/Exit.png'), '&Exit', self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setStatusTip('Exit application')
        self.exitAction.triggered.connect(self.close)

        self.copyAction = QAction(QIcon('Icon/Copy.png'), '&Copy', self)
        self.copyAction.setShortcut('Ctrl+C')
        self.copyAction.setStatusTip('Copy aplication')
        self.copyAction.triggered.connect(self.copyFile)

        self.pasteAction = QAction(QIcon('Icon/Paste.png'), '&Paste', self)
        self.pasteAction.setShortcut('Ctrl+V')
        self.pasteAction.setStatusTip('Paste aplication')
        self.pasteAction.triggered.connect(self.pasteFile)

        self.cutAction = QAction(QIcon('Icon/Cut.png'), '&Cut', self)
        self.cutAction.setShortcut('Ctrl+Z')
        self.cutAction.setStatusTip('Cut aplication')
        self.cutAction.triggered.connect(self.cutFile)

        self.helpAction = QAction(QIcon('Icon/Help.png'), '&Help', self)
        self.helpAction.setStatusTip('Help aplication')
        self.helpAction.triggered.connect(self.helpFile)

        self.manualAction = QAction(QIcon('Icon/Manual.png'), '&Manual', self)
        self.manualAction.setStatusTip('Manual aplication')
        self.manualAction.triggered.connect(self.manualFile)

        self.aboutAction = QAction('&About', self)
        self.aboutAction.setStatusTip('About aplication')
        self.aboutAction.triggered.connect(self.aboutFile)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)

        editMenu = menubar.addMenu('&Edit')
        editMenu.addAction(self.copyAction)
        editMenu.addAction(self.pasteAction)
        editMenu.addAction(self.cutAction)

        manualMenu = menubar.addMenu('&Manual')
        manualMenu.addAction(self.manualAction)

        helpMenu = menubar.addMenu('&Help')
        helpMenu.addAction(self.helpAction)
        helpMenu.addAction(self.aboutAction)

        fileToolBar = self.addToolBar('File')
        fileToolBar.addAction(self.newAction)
        fileToolBar.addAction(self.openAction)
        fileToolBar.addAction(self.saveAction)

        editToolBar = QToolBar('Edit', self)
        self.addToolBar(editToolBar)
        editToolBar.addAction(self.copyAction)
        editToolBar.addAction(self.pasteAction)
        editToolBar.addAction(self.cutAction)



        # self.copyAction.setShortcut(QKeySequence.Copy)
        self.show()
    def newFile(self):
        self.centralWidget.setText('<b> File > New </b> clicked')
    def openFile(self):
        self.centralWidget.setText('<b> File > Open </b>  clicked')
    def saveFile(self):
        self.centralWidget.setText('<b> File > Save </b> clicked')
    def copyFile(self):
        self.centralWidget.setText('<b> File > Copy </b> clicked')
    def pasteFile(self):
        self.centralWidget.setText('<b> File > Paste </b> clicked')
    def cutFile(self):
        self.centralWidget.setText('<b> File > Cut </b> clicked')
    def manualFile(self):
        self.centralWidget.setText('https://pythonist.ru/')
    def helpFile(self):

        window = QWidget()
        layout = QVBoxLayout()
        view = QWebEngineView()
        layout.addWidget(view)
        view.setUrl(QUrl('https://www.pythontutorial.net/pyqt/'))
        window.setLayout(layout)
        window.show()
        self.centralWidget.setText('<b> File > Help </b> clicked')
    def aboutFile(self):
        self.centralWidget.setText('Мини приложение \n Создано 20 марта 2024г.')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())