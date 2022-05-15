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
        user = User("testuser", "password")
        self.user_management.set_active_user(user)
        self.user_management.make_admin()
        role = self.user_management.get_active_user_role()
        self.assertEqual(Role.ADMIN, role)

    def test_username_is_valid(self):
        self.dummy_user = User("testuser", "password")
        is_valid, status_msg = self.dummy_user.username_is_valid()
        self.assertEqual(True, is_valid)

    def test_username_is_not_valid(self):
        self.dummy_user = User("abc", "password")
        is_valid, status_msg = self.dummy_user.username_is_valid()
        self.assertEqual(False, is_valid)

    def test_handle_user_creation_returns_false_when_username_not_valid(self):
        is_valid, status_msg = self.user_management.handle_user_creation("abc", "password", "password", False)
        self.assertEqual(False, is_valid)

    def test_handle_user_creation_returns_false_when_password_not_valid(self):
        is_valid, status_msg = self.user_management.handle_user_creation("username", "pass", "pass", False)
        self.assertEqual(False, is_valid)
        
    def test_valid_password_false(self):
        password_1 = "password"
        password_2 = "passwoerd"
        result, status_msg = self.dummy_user.password_is_valid(password_1, password_2)
        self.assertEqual(False, result)

    def test_passwords_do_not_match_error_msg(self):
        password_1 = "password"
        password_2 = "passwoerd"
        result, status_msg = self.dummy_user.password_is_valid(password_1, password_2)
        self.assertEqual("Error: Passwords do not match. ", status_msg)

    def test_password_not_long_enough_error_msg(self):
        password_1 = "pass"
        password_2 = "pass"
        result, status_msg = self.dummy_user.password_is_valid(password_1, password_2)
        self.assertEqual("Error: Password must have 6 characters", status_msg)

    def test_valid_password_true(self):
        password_1 = "password"
        password_2 = "password"
        result, status_msg = self.dummy_user.password_is_valid(password_1, password_2)
        self.assertEqual(True, result)

    def test_login_fails_with_incorrect_credentials(self):
        user = User("testuser", "password")
        self.user_management.set_active_user(user)
        self.user_management.create_user()
        result, status_msg = self.user_management.login("testuser", "passcode")
        self.assertEqual(False, result)

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
        result, status_msg = self.user_management.handle_user_creation(
            username, password1, password2, is_admin)
        self.assertEqual(False, result)
    
    def test_when_no_active_user_return_none_for_get_active_user(self):
        self.user_management._active_user = None
        result = self.user_management.get_active_user()
        self.assertEqual(None, result)

    def test_when_no_active_user_return_none_for_active_user_role(self):
        self.user_management._active_user = None
        result = self.user_management.get_active_user_role()
        self.assertEqual(None, result)

    def test_logout_clears_active_user(self):
        self.user_management.logout()
        user = self.user_management.get_active_user()
        self.assertEqual(None, user)

    def test_create_user_method_returns_false_if_no_active_user(self):
        self.user_management._active_user = None
        result, status_msg = self.user_management.create_user()
        self.assertEqual(False, result)
