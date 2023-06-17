# -*- coding: cp1251 -*-
import sqlite3

"""try:
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

except sqlite3.DatabaseError:
    print("Произошла ошибка при подключении")

finally:
    connection.close()""" # Так делать не надо

class User:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender


def create_table(cursor):
    command = """
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            name TEXT,
            surname TEXT,
            gender TEXT);
            """
    cursor.execute(command)


def add_user(cursor, user):
    command = """
                INSERT INTO users (name, surname, gender) VALUES (?, ?, ?)
                """
    cursor.execute(command, (user.name, user.surname, user.gender))


def get_user_list(cursor):
    command = """
            SELECT * FROM users;
            """
    result = cursor.execute(command)
    users = result.fetchall()
    print(users)


def get_user(cursor, user_id):
    command = """
            SELECT * FROM users WHERE id = ?;
            """
    result = cursor.execute(command, (user_id,))
    users = result.fetchall()
    print(users)


def update_user_name(cursor, value, user_id):
    command = """
    UPDATE users SET name = ? WHERE id = ?
    """
    cursor.execute(command, (value, user_id))


def delete_users(cursor):
    command = """
    DELETE FROM users
    """
    cursor.execute(command)

if __name__ == "__main__":
    with sqlite3.connect("data.db") as cursor:
        create_table(cursor)
        delete_users(cursor)
        add_user(cursor, User(name="Alex", surname="Matveev", gender="male"))
        add_user(cursor, User(name="Alice", surname="Sokolova", gender="female"))
        add_user(cursor, User(name="Mikhail", surname="Kamenev", gender="male"))
        get_user_list(cursor)
        get_user(cursor, 2)
        update_user_name(cursor, "Kate", 2)
        get_user(cursor, 2)







# Домашняя работа


# 1 задание
import sqlite3

class User:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender


def create_table(cursor):
    command = """
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            name TEXT,
            surname TEXT,
            gender TEXT);
            """
    cursor.execute(command)


def add_user(cursor, user):
    command = """
                INSERT INTO users (name, surname, gender) VALUES (?, ?, ?)
                """
    cursor.execute(command, (user.name, user.surname, user.gender))


def get_user_list(cursor):
    command = """
            SELECT * FROM users;
            """
    result = cursor.execute(command)
    users = result.fetchall()
    print(users)


def get_user(cursor, user_id):
    command = """
            SELECT * FROM users WHERE id = ?;
            """
    result = cursor.execute(command, (user_id,))
    users = result.fetchall()
    print(users)


def update_user_name(cursor, value, user_id):
    command = """
    UPDATE users SET name = ? WHERE id = ?
    """
    cursor.execute(command, (value, user_id))


def delete_users(cursor):
    command = """
    DELETE FROM users
    """
    cursor.execute(command)

def delete_user(cursor, user_id):
    command = """
    DELETE FROM users WHERE id = ?;
    """
    result = cursor.execute(command, (user_id,))
    users = result.fetchall()
    print(users)

if __name__ == "__main__":
    with sqlite3.connect("data.db") as cursor:
        create_table(cursor)
        delete_users(cursor)
        add_user(cursor, User(name="Alex", surname="Matveev", gender="male"))
        add_user(cursor, User(name="Alice", surname="Sokolova", gender="female"))
        add_user(cursor, User(name="Mikhail", surname="Kamenev", gender="male"))
        get_user_list(cursor)
        get_user(cursor, 2)
        update_user_name(cursor, "Kate", 2)
        get_user(cursor, 2)
        delete_user(cursor, 3)
        get_user_list(cursor)






# 2 задание

import sqlite3

class User:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender


def create_table(cursor):
    command = """
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            name TEXT,
            surname TEXT,
            gender TEXT);
            """
    cursor.execute(command)


def add_user(cursor, user):
    command = """
                INSERT INTO users (name, surname, gender) VALUES (?, ?, ?)
                """
    cursor.execute(command, (user.name, user.surname, user.gender))


def get_user_list(cursor):
    command = """
            SELECT * FROM users;
            """
    result = cursor.execute(command)
    users = result.fetchall()
    print(users)


def get_user(cursor, user_id):
    command = """
            SELECT * FROM users WHERE id = ?;
            """
    result = cursor.execute(command, (user_id,))
    users = result.fetchall()
    print(users)


def get_users(cursor, gender_):
    command = """
            SELECT * FROM users WHERE gender = ?;
            """
    result = cursor.execute(command, (gender_,))
    users = result.fetchall()
    print(users)


def update_user_name(cursor, value, user_id):
    command = """
    UPDATE users SET name = ? WHERE id = ?
    """
    cursor.execute(command, (value, user_id))


def delete_users(cursor):
    command = """
    DELETE FROM users
    """
    cursor.execute(command)

def delete_user(cursor, user_id):
    command = """
    DELETE FROM users WHERE id = ?;
    """
    result = cursor.execute(command, (user_id,))
    users = result.fetchall()
    print(users)

if __name__ == "__main__":
    with sqlite3.connect("data.db") as cursor:
        create_table(cursor)
        delete_users(cursor)
        add_user(cursor, User(name="Alex", surname="Matveev", gender="male"))
        add_user(cursor, User(name="Alice", surname="Sokolova", gender="female"))
        add_user(cursor, User(name="Mikhail", surname="Kamenev", gender="male"))
        get_user_list(cursor)
        get_user(cursor, 2)
        update_user_name(cursor, "Kate", 2)
        get_user(cursor, 2)
        get_users(cursor, "male")