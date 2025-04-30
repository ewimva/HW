import sqlite3

class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    amount REAL NOT NULL
                )
            ''')
            conn.commit()

    def add_expenses(self, title, amount):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute(
            """INSERT INTO expenses (title, amount) VALUES (?, ?)""", (title, amount))
            conn.commit()

    def all_(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM expenses")
            return cursor.fetchall()

    def get_total(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT SUM(amount) FROM expenses")
            result = cursor.fetchone()[0]
            return int(result) if result else 0
        
    def delete_expense(self, expense_id: int):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
            conn.commit()

    def update_expense(self, expense_id: int, new_name: str, new_amount: float):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE expenses SET title = ?, amount = ? WHERE id = ?", (new_name, new_amount, expense_id))
            conn.commit()

