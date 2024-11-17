from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox, QMainWindow
from data.user import UserData
from models.user import User


class RegisterWindow:
    def __init__(self):
        self.window = uic.loadUi("gui/registerTransfer.ui")
        # self.initGUI()
        self.window.show()

    # def initGUI(self):
    #     self.window.btnRegistrarTransferencias.clicked.connect(self.registerTransfer)
