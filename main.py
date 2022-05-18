from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtWidgets import QPushButton, QApplication, QMainWindow, QLabel, QStackedWidget, QHBoxLayout, QVBoxLayout, \
    QWidget, QListWidget, QStackedLayout
import sys

from src.pages.config import IVWindow
from src.pages.start import StartWin
from src.pages.home import Main
from src.lang.language import Language

class GUI(QMainWindow):
    def __init__(self, parent=None):
        super(GUI, self).__init__(parent)
        self.language = Language("fr")

        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap('src/image/maths.png'), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.setWindowIcon(self.icon)

        QtGui.QFontDatabase.addApplicationFont('./src/font/simplicity.ttf')

        self.uiMainWindow = Main()
        self.ui_start = StartWin()
        self.ui_conf = IVWindow()
        self.startMainWindow()

    def startMainWindow(self):
        self.uiMainWindow.lang = self.language.get_lang()
        self.uiMainWindow.setupUI(self)
        # Connect buttons to the page (ivPage, ipPage ...)
        self.uiMainWindow.start_bt.clicked.connect(self.load_start)
        self.uiMainWindow.conf_bt.clicked.connect(self.load_config)
        self.uiMainWindow.language.clicked.connect(self.change_language)
        self.show()

    def load_start(self):
        self.ui_start.lang = self.language.get_lang()
        self.ui_start.setupUI(self)
        self.ui_start.homeBt.clicked.connect(self.startMainWindow)
        self.ui_start.language.clicked.connect(self.change_language)
        self.show()

    def load_config(self):
        self.ui_conf.setupUI(self)
        self.ui_conf.homeBt.clicked.connect(self.startMainWindow)
        self.show()

    def change_language(self):

        try:
            if self.uiMainWindow.lang["language"] == "fr":
                self.language = Language("en")
            if self.uiMainWindow.lang["language"] == "en":
                self.language = Language("fr")
            self.startMainWindow()
        except:
            pass

        try:
            if self.ui_start.lang["language"] == "fr":
                self.language = Language("en")
            if self.ui_start.lang["language"] == "en":
                self.language = Language("fr")
            self.load_start()
        except:
            pass






if __name__ == '__main__':
    font = QFont('aero')
    app = QApplication(sys.argv)
    app.setStyle('Window')
    app.setStyleSheet(open('src/css/main.qss').read())
    window = GUI()
    sys.exit(app.exec_())
