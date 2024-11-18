import random
import sqlite3

connection = sqlite3.connect('not_telegram_2.db')
cursor = connection.cursor()

# Создание таблицы
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

# Заполнение таблицы
# for i in range(1, 31):
#     cursor.execute("INSERT INTO Users (username, email, age) VALUES(?,?,?)",
#                    (f'User{i}', f"example{i}@gmail.com", random.randint(25, 60)))

# Удалили пользователя под id = 6
cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

cursor.execute("SELECT COUNT(*),SUM(balance),AVG(balance) FROM Users")
result = cursor.fetchone()
all_balance = result[1]
total_users = result[0]

print(f"{all_balance/total_users} ({result[2]})")

connection.commit()
connection.close()