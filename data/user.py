import connection as con
from models.user import User


class UserData:
    def __init__(self):
        self.db = con.con.connect()  # Conexión a la base de datos
        self.cursor = self.db.cursor()

    def close(self):
        """
        Cierra la conexión con la base de datos.
        """
        try:
            if self.cursor:
                self.cursor.close()
            if self.db:
                self.db.close()
        except Exception as exc:
            print(f"Error al cerrar la conexión: {exc}")

    def login(self, user: User):
        """
        Verifica si el usuario existe en la base de datos.
        Retorna una instancia del usuario si existe, de lo contrario None.
        """
        try:
            query = "SELECT * FROM users WHERE name = ? AND password = ?"
            self.cursor.execute(query, (user._name, user._password))
            res = self.cursor.fetchone()

            if res is None:
                return None
            else:
                # Crea un nuevo usuario con los datos obtenidos
                logged_user = User(name=res[1], email=res[2], password=res[3])
                return logged_user
        except Exception as exc:
            print(f"Error al intentar iniciar sesión: {exc}")
            return None
