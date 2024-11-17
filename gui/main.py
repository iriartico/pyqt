from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox, QMainWindow
from gui.registerTransfer import RegisterWindow


class MainWindow:
    def __init__(self):
        self.main = uic.loadUi("gui/main.ui")
        self.initGUI()
        self.main.showMaximized()

    def initGUI(self):
        self.main.btnRegistrarTransferencias.triggered.connect(
            self.openRegisterTransfer
        )

    def openRegisterTransfer(self):
        self.registerTransfer = RegisterWindow()
        # self.main.hide()
        # self.main.()
