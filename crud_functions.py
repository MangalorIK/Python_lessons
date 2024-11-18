import sqlite3

def initiate_db():
    connection = sqlite3.connect('not_telegram_4.db')
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
    connection.commit()
    connection.close()


def add_product(title, desc, price):
    connection = sqlite3.connect('not_telegram_4.db')
    cursor = connection.cursor()
    check_product = cursor.execute("SELECT * FROM Products where title = ?", (title,))

    if check_product.fetchone() is None:
        cursor.execute(f'''
    INSERT INTO Products (title, description, price) VALUES('{title}','{desc}','{price}')
    ''')
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('not_telegram_4.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    connection.close()
    return products



