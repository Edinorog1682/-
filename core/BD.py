import sqlite3
from flet import *
from core.style import *
from core.dicitionary_ru import *
from views.Register import *



class UserChecker():
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            № INTEGER PRIMARY KEY AUTOINCREMENT,
            E_mail TEXT,
            username TEXT,
            password TEXT
            )""")

    def check_user(self, login_username: str, login_password: str):
        self.cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?",
                            (login_username, login_password))
        user = self.cursor.fetchone()

        print(user)
        if user:
            print("True")



        else:
            print("False")

    def register_check(self, E_mail: str, username: str, password: str):
        self.cursor.execute("SELECT * FROM users WHERE E_mail = ? AND username = ?",
                            (E_mail, username))
        user = self.cursor.fetchone()
        if not user:
            print("можно регистрировать")
        else:
            print("Занят или логин или майл")
            Register.login_auth()


checker = UserChecker("PROMMETALL.db")
print(123)
reg_checker = UserChecker("PROMMETALL.db")
