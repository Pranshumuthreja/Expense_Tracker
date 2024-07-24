import sqlite3

def connect_db():
    return sqlite3.connect('expenses.db')

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY,
                        amount REAL,
                        description TEXT,
                        category TEXT,
                        date TEXT)''')
    conn.commit()
    conn.close()

def add_expense(amount, description, category, date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO expenses (amount, description, category, date) VALUES (?, ?, ?, ?)',
                   (amount, description, category, date))
    conn.commit()
    conn.close()

def fetch_expenses():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM expenses')
    rows = cursor.fetchall()
    conn.close()
    return rows
