import sqlite3

connection = sqlite3.connect('../not_telegram_2.db')
cursor = connection.cursor()

# Создание таблицы
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER,
username TEXT NOT NULL,
firstname TEXT,
block INT
)
''')


def add_user(user_id, username, first_name):
    check_user = cursor.execute("SELECT * FROM Users where id = ?", (user_id,))
    if check_user.fetchone() is None:
        cursor.execute(f'''
    INSERT INTO Users VALUES('{user_id}','{username}','{first_name}',0)
    ''')
    connection.commit()


connection.commit()
connection.close()
