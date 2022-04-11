import unittest
from entities.user import User
from services.user_management import default_user_management
from initialize_database import initialize_database


class TestUserManagement(unittest.TestCase):
    def setUp(self):
        self.user_management = default_user_management
        self.testuser = User("testuser1", "salasana")
        self.db = initialize_database()

    def test_create_user(self):
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
    
    def test_create_multiple_users(self):
        self.user_management.add_user(User("user1", "password"))
        self.user_management.add_user(User("user2", "password"))
        self.user_management.add_user(User("user3", "password"))
        user_count = len(self.user_management.get_all_users())
        self.assertEqual(3, user_count)

    def test_try_to_add_username_already_in_use(self):
        self.user_management.add_user(User("user1", "password"))
        result = self.user_management.add_user(User("user1", "password"))
        self.assertEqual(False, result)
    
    def test_try_to_create_username_already_in_use(self):
        self.user_management.add_user(User("user1", "password"))
        result = self.user_management.create_user(User("user1", "password"))
        self.assertEqual(False, result)
    





        

