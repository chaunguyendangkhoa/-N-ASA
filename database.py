import sqlite3
from config import DATABASE_NAME


class Database:

    def __init__(self):

        self.conn = sqlite3.connect(
            DATABASE_NAME,
            check_same_thread=False
        )

        self.cursor = self.conn.cursor()

        self.create_table()

    def create_table(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS history(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            question TEXT,

            answer TEXT,

            created_at DATETIME DEFAULT CURRENT_TIMESTAMP

        )
        """)

        self.conn.commit()

    def save(self, question, answer):

        self.cursor.execute("""
        INSERT INTO history(question, answer)
        VALUES(?, ?)
        """, (question, answer))

        self.conn.commit()

    def get_all(self):

        self.cursor.execute("""
        SELECT *
        FROM history
        ORDER BY id DESC
        """)

        return self.cursor.fetchall()

    def delete_all(self):

        self.cursor.execute("""
        DELETE FROM history
        """)

        self.conn.commit()

    def get_count(self):

        self.cursor.execute("""
        SELECT COUNT(*)
        FROM history
        """)

        return self.cursor.fetchone()[0]