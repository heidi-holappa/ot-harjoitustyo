import unittest
from entities.user import User
from services.user_management import default_user_management


class TestUserManagement(unittest.TestCase):
    def setUp(self):
        self.user_management = default_user_management
        self.testuser = User("testuser", "salasana")
        print("Set up goes here")

    def test_create_user(self):
        # Incase testuser does not exist, create user account
        self.user_management.create_user(self.testuser)
        result = self.user_management.login(self.testuser)
        self.assertEqual(True, result)

    def test_set_admin(self):
        self.testuser.set_admin()
        role = self.testuser.role
        self.assertEqual("admin", role)


    def test_valid_password_false(self):
        password_1 = "password"
        password_2 = "passwoerd"
        result = self.user_management.password_is_valid(password_1, password_2)
        self.assertEqual(False, result)

    def test_valid_password_true(self):
        password_1 = "password"
        password_2 = "password"
        result = self.user_management.password_is_valid(password_1, password_2)
        self.assertEqual(True, result)

    def test_get_user(self):
        self.user_management.create_user(self.testuser)
        fetched_user = self.user_management.get_user(self.testuser.username)
        self.assertEqual(self.testuser.username, fetched_user.username)


        

