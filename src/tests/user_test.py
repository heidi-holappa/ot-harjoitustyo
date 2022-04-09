import unittest
from ui.text_based_ui import CounselorSubmit, StartScreen
from services.console_io import ConsoleIO
from entities.user import User


class TestTextBasedUI(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_create_user(self):
        user = User("testuser", "password")
        # Incase testuser does not exist, create user account
        user.create_user()
        result = user.login()
        self.assertEqual(True, result)
