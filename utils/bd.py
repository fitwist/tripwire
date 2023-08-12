import sqlite3
from datetime import datetime
from core import settings
import uuid


class Database():
    def __init__(self):
        self.con = None
        self.bd = settings.DATABASE 

    def __del__(self):
        self.close()

    def open(self):
        if self.con is None:
            self.con = sqlite3.connect(self.bd, isolation_level=None)
            self.con.row_factory = sqlite3.Row
            self.cur = self.con.cursor()

    def close(self):
        self.con.close()
        self.cur = None
        self.con = None

    def execute(self, sql, args=()):
        cursor = self.con.execute(sql, args)
        return cursor

    def first(self, sql, args=()):
        cursor = self.execute(sql, args)
        if cursor is None:
            return None
        return cursor.fetchone()

    def get(self, sql, args):
        row = self.first(sql, args)
        if row is None:
            return None
        return row[0]


db = Database()
time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
db.open()

# Создает базу данных при первом запуске
def create_db():
    # Проверим по tg_id, есть ли пользователь в базе users
    db.open()  # Подключимся к БД
    # запрос в БД
    db.cur.execute(f'''CREATE TABLE users(
        "tg_id" INT UNIQUE PRIMARY KEY,
        "uuid" VARCHAR(50),
        "phone" VARCHAR(30),
        "name" VARCHAR(60),
        "count" INT NULL DEFAULT 2,
        "finish" BOOLEAN NULL,
        "branch" VARCHAR(255),
        "result_time" TIMESTAMP,
        "is_login" VARCHAR(30),
        "is_uid" VARCHAR(11)
    )''')
    res = False
    if db.cur.fetchone():  # Извлечем данные
        res = True
    db.close()  # Закроем соединение
    return res

def check_user(tg_id):
    # Проверим по tg_id, есть ли пользователь в базе users
    db.open()  # Подключимся к БД
    # запрос в БД
    db.cur.execute(f"SELECT * FROM users WHERE tg_id = '{tg_id}'")
    res = False
    if db.cur.fetchone():  # Извлечем данные
        res = True
    db.close()  # Закроем соединение
    return res


def registration(tg_id, phone, name):
    # Присвоим пользователю уникальный идентификатор
    uniq_id = str(uuid.uuid4())

    db.open()
    db.cur.execute(f"INSERT INTO users (tg_id, phone, name, uuid)\
                     VALUES ({tg_id}, {phone}, '{name}', '{uniq_id}')")
    db.con.commit()
    db.close()
    return user_by_uuid(uniq_id)


def finish(tg_id, finish):
    # Сделаем запись об успешном прохождении опроса
    db.open()
    db.cur.execute(f"UPDATE users SET finish='{finish}',\
                     result_time='{time_now}'\
                     WHERE tg_id={tg_id}")
    db.con.commit()
    db.close()
    return True


def update_one_var(tg_id, row, var):
    # Запишем / обновим одну переменную для tg_id в базе users
    db.open()
    db.cur.execute(f"UPDATE users SET {row}='{var}' WHERE tg_id={tg_id}")
    db.con.commit()
    db.close()
    return True


# def read_one_var(tg_id, row):
#     # Прочитаем одну переменную для tg_id в базе users
#     db.open()
#     db.cur.execute(f"SELECT {row} FROM users WHERE tg_id={tg_id}")
#     data = db.cur.fetchone()
#     if data:
#         db.close()
#         return data[0]
#     db.close()
#     return False


def result(tg_id):
    # Выведем список победителей для каждой ветки
    db.open()
    db.cur.execute(f"SELECT name, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, question13, question14, question15, question16, question17, question18 FROM users WHERE (finish='True' AND tg_id='{tg_id}')")
    data = db.cur.fetchall()
    res = []
    # Занесем результаты в список
    for row in data:
        res.append(str(row[0]))
        res.append(str(row[1]))
        res.append(str(row[2]))
        res.append(str(row[3]))
        res.append(str(row[4]))
        res.append(str(row[5]))
        res.append(str(row[6]))
        res.append(str(row[7]))
        res.append(str(row[8]))
        res.append(str(row[9]))
        res.append(str(row[10]))
        res.append(str(row[11]))
        res.append(str(row[12]))
        res.append(str(row[13]))
        res.append(str(row[14]))
        res.append(str(row[15]))
        res.append(str(row[16]))
        res.append(str(row[17]))
        res.append(str(row[18]))
        
    db.close()
    return res


def user_by_uuid(uuid):
    db.open()
    sql = "SELECT * FROM users WHERE uuid=?"
    user_data = db.first(sql, (uuid,))
    if user_data is None:
        return None
    db.close()
    return dict(user_data)

