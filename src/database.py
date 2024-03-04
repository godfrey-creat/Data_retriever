import psycopg2
from config import database_config

class Database:
    def __init__(self):
        self.connection = psycopg2.connect(**database_config)

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results
