import sqlite3

class Connection():
    def __init__(self):
        try:
            self.con = sqlite3.connect("banca.db")
            self.createTables()
        except Exception as exc:
            print(exc)

    def createTables(self):
        sql_create_table1 = """CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        );"""
        cur = self.con.cursor()
        cur.execute(sql_create_table1)
        cur.close()
        self.createAdmin()


    def createAdmin(self):
        try:            
            sql_create_table1 = """INSERT INTO users VALUES (null, '{}', '{}', '{}')""".format("admin", "admin@email.com",
                                                                                        "admin123")
            cur = self.con.cursor()
            cur.execute(sql_create_table1)
            self.con.commit()
            cur.close()
        except Exception as exc:
            print(exc)

con = Connection()