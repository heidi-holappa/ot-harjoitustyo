import unittest
from entities.user import User, Role
from services.user_management import default_user_management
from initialize_database import initialize_database


class TestUserManagement(unittest.TestCase):
    def setUp(self):
        self.user_management = default_user_management
        self.dummy_user = User("testuser", "password")
        self.db = initialize_database()

    def test_create_user(self):
        self.user_management.set_active_user(self.dummy_user)
        self.testuser = self.user_management.get_active_user()
        self.user_management.create_user()
        result = self.user_management.login(
            self.dummy_user.username, self.dummy_user.password)
        self.assertEqual(True, result[0])

    def test_set_admin(self):
        self.user_management.make_admin()
        role = self.user_management.get_active_user_role()
        self.assertEqual(Role.ADMIN, role)

    def test_valid_password_false(self):
        password_1 = "password"
        password_2 = "passwoerd"
        result = self.dummy_user.password_is_valid(password_1, password_2)
        self.assertEqual(False, result[0])

    def test_valid_password_true(self):
        password_1 = "password"
        password_2 = "password"
        result = self.dummy_user.password_is_valid(password_1, password_2)
        self.assertEqual(True, result[0])

    def test_get_user(self):
        username = "testuser2"
        password1 = "password"
        password2 = "password"
        is_admin = False
        self.user_management.handle_user_creation(
            username, password1, password2, is_admin)
        fetched_user = self.user_management.get_user(username)
        self.assertEqual(username, fetched_user.username)

    def test_create_multiple_users(self):
        username1 = "user1"
        username2 = "user2"
        username3 = "user3"
        password1 = "password"
        password2 = "password"
        is_admin = False
        self.user_management.handle_user_creation(
            username1, password1, password2, is_admin)
        self.user_management.handle_user_creation(
            username2, password1, password2, is_admin)
        self.user_management.handle_user_creation(
            username3, password1, password2, is_admin)
        user_count = len(self.user_management.get_all_users())
        self.assertEqual(3, user_count)

    def test_try_to_create_username_already_in_use(self):
        username = "testuser2"
        password1 = "password"
        password2 = "password"
        is_admin = False
        self.user_management.handle_user_creation(
            username, password1, password2, is_admin)
        result = self.user_management.handle_user_creation(
            username, password1, password2, is_admin)
        self.assertEqual(False, result[0])
