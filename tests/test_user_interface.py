import unittest
from unittest.mock import patch
from user_interface import UserInterface

class TestUserInterface(unittest.TestCase):
    @patch("builtins.input", return_value="SELECT * FROM employees")
    def test_run(self, mock_input):
        ui = UserInterface()
        ui.run()
        # Add assertions for expected behavior

if __name__ == "__main__":
    unittest.main()
