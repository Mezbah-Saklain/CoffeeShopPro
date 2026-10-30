import sqlite3

class Database:
    def __init__(self, path: str = ":memory:"):
        self.conn = sqlite3.connect(path)
        self._init_schema()
    def _init_schema(self):
        self.conn.executescript("""
            CREATE TABLE IF NOT EXISTS menu (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                category TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT,
                total REAL
            );
        """)
        self.conn.commit()
    def add_menu_item(self, name, price, category):
        self.conn.execute(
            "INSERT INTO menu (name, price, category) VALUES (?, ?, ?)",
            (name, price, category))
        self.conn.commit()
    def get_menu(self):
        return self.conn.execute(
            "SELECT name, price, category FROM menu").fetchall()
    def save_order(self, description, total):
        self.conn.execute(
            "INSERT INTO orders (description, total) VALUES (?, ?)",
            (description, total))
        self.conn.commit()
    def get_orders(self):
        return self.conn.execute(
            "SELECT description, total FROM orders").fetchall()