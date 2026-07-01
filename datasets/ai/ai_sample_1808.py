import sqlite3

class SQLReader():

    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(dB_name)

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def close_connection(self):
        self.connection.close()