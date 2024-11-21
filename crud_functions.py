import sqlite3


def initiate_db():
    connection = sqlite3.connect('not_telegram_5.db')
    cursor = connection.cursor()
    # Создание таблицы
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')
    connection.commit()
    connection.close()


def add_user(username, email, age):
    connection = sqlite3.connect('not_telegram_5.db')
    cursor = connection.cursor()

    if not is_included(username):
        cursor.execute(f'''
        INSERT INTO Users (username, email, age, balance) VALUES('{username}','{email}','{age}', 1000)
        ''')
    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect('not_telegram_5.db')
    cursor = connection.cursor()
    check_user = cursor.execute("SELECT * FROM Users where username = ?", (username,))
    check = check_user.fetchone()
    connection.close()
    if check is None:
        return False
    else:
        return True


def add_product(title, desc, price):
    connection = sqlite3.connect('not_telegram_5.db')
    cursor = connection.cursor()
    check_product = cursor.execute("SELECT * FROM Products where title = ?", (title,))

    if check_product.fetchone() is None:
        cursor.execute(f'''
    INSERT INTO Products (title, description, price) VALUES('{title}','{desc}','{price}')
    ''')
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('not_telegram_5.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    connection.close()
    return products
