from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox, QMainWindow


class Login:
    def __init__(self):
        self.login = uic.loadUi("gui/login.ui")
        self.login.show()
