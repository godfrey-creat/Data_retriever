import unittest
from database import Database

class TestDatabase(unittest.TestCase):
    def test_execute_query(self):
        db = Database()
        query = "SELECT * FROM employees"
        result = db.execute_query(query)
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()
