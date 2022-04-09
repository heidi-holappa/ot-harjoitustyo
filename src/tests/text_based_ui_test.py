import unittest
from ui.text_based_ui import CounselorSubmit, StartScreen
from services.console_io import ConsoleIO
from entities.user import User


class TestTextBasedUI(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_clear_data(self):
        user = User("testuser", "salasana")
        data_submit = CounselorSubmit(user)
        for key in data_submit._data:
            data_submit._data[key] = "test content"
        data_submit.clear_data()
        self.assertEqual(0, len(data_submit._data["channel"]))
