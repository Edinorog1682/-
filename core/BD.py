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
            self.cursor.execute("INSERT INTO users(E_mail, username, password) VALUES(?,?,?)",(E_mail, username, password))
            self.conn.commit()
            print(f"Зареган акк {E_mail}, {username}, {password} спамит BD.py 31 строка")
            return "Успешно зарегистрирован"
        else:
            print("Занят или логин или майл")
            #Тут тебе срется ошибка из-за того, что ты пытаешься вызвать селф метод не у объекта класса
            #Register.login_auth()
            return "Пользователь уже существует"
        #Добавил ретерны, чтобы отслеживать что произошло при вызове этого def чтобы в Regiser потом поймать результат
        #и вызвать нужную функцию, дабы задоджить ошибку 46 строки


checker = UserChecker("PROMMETALL.db")
reg_checker = UserChecker("PROMMETALL.db")
