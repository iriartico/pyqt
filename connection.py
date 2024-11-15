import sqlite3


class Connection:
    def __init__(self):
        try:
            self.con = sqlite3.connect("banca.db")
            self.createTables()
        except Exception as exc:
            print(f"Error al conectar con la base de datos: {exc}")

    def createTables(self):
        try:
            sql_create_table1 = """CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT NOT NULL,
                password TEXT NOT NULL
            );"""
            cur = self.con.cursor()
            cur.execute(sql_create_table1)
        except Exception as exc:
            print(f"Error al crear la tabla: {exc}")
        finally:
            cur.close()
        self.createAdmin()

    def createAdmin(self):
        try:
            cur = self.con.cursor()
            cur.execute("SELECT * FROM users WHERE name = ?", ("admin",))
            if cur.fetchone() is None:  # Si no existe el admin
                sql_insert_admin = (
                    """INSERT INTO users (name, email, password) VALUES (?, ?, ?)"""
                )
                cur.execute(sql_insert_admin, ("admin", "admin@email.com", "admin123"))
                self.con.commit()
            cur.close()
        except Exception as exc:
            print(f"Error al verificar o crear el admin: {exc}")

    def connect(self):
        return self.con


# Crea una instancia de Connection
con = Connection()
