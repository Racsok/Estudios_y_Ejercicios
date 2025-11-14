import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def open_connection(self):
        if self.connection is None:
            try:
                self.connection = sqlite3.connect(self.db_name)
            except sqlite3.Error as e:
                print(f"Error connecting to database: {e}")
                raise

    def close_connection(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def execute_query(self, query, params=()):
        if self.connection is not None:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            return cursor

    def fetch_all(self, query, params=()):
        self.open_connection()
        if self.connection is not None:
            cursor = self.execute_query(query, params)
            return cursor.fetchall() # type: ignore

    def fetch_one(self, query, params=()):
        self.open_connection  
        if self.connection is not None:  
            cursor = self.execute_query(query, params)
            return cursor.fetchone() # type: ignore