from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox, QMainWindow
from data.user import UserData
from models.user import User
from gui.main import MainWindow


class Login:
    def __init__(self):
        self.login = uic.loadUi("gui/login.ui")
        self.initGUI()
        self.login.txterror.setText("")
        self.login.show()

    def ingresar(self):
        if self.login.txtUser.text() == "" or self.login.txtPassword.text() == "":
            self.login.txterror.setText("Por favor ingrese usuario y contraseña")
            self.login.txtUser.setFocus()
            self.login.txtPassword.setFocus()

        elif len(self.login.txtUser.text()) < 3:
            self.login.txterror.setText("Por favor ingrese un usuario válido")
            self.login.txtUser.setFocus()

        elif len(self.login.txtPassword.text()) < 8:
            self.login.txterror.setText("Por favor ingrese una contraseña válida")
            self.login.txtPassword.setFocus()
        else:
            self.login.txterror.setText("")
            user = User(
                name=self.login.txtUser.text(), password=self.login.txtPassword.text()
            )
            res = UserData().login(user)
            if res:
                # self.login.txterror.setText("OK")
                self.main = MainWindow()
                self.login.hide()
            else:
                self.login.txterror.setText("Usuario o contraseña incorrectos")

    def initGUI(self):
        self.login.btnLogin.clicked.connect(self.ingresar)
        self.login.show()

    def run(self):
        self.app.exec()
