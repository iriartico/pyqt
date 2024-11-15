from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox, QMainWindow


class MainWindow:
    def __init__(self):
        self.main = uic.loadUi("gui/main.ui")
        # self.initGUI()
        self.main.showMaximized()
