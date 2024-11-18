import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# Создание таблицы
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# Заполнение таблицы
for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES(?,?,?,?)",
                   (f'User{i}', f"example{i}@gmail.com", 10 * i, 1000))

# Украли у каждого второго 500, пропустив первого (Директора лучше не грабить)
cursor.execute("UPDATE Users SET balance = ? WHERE (id+1)%2 == 0 ", (500,))

# Сокращение в команде, Директора снова обойдём
cursor.execute("DELETE FROM Users where (id+2)%3 == 0")

# Вывели список кто скидывается на ДР 60-ти летнему
cursor.execute("SELECT * FROM Users WHERE age != 60")
users = cursor.fetchall()

for user in users:
    print(f"Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}")

connection.commit()
connection.close()
