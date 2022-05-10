import unittest
from entities.user import User, Role
from services.user_management import default_user_management
from repositories.user_repository import default_user_repository
from initialize_database import initialize_database


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.user_management = default_user_management
        self.db = initialize_database()
        self.repository = default_user_repository

    def test_user_set_admin_rights(self):
        self.user_management.handle_user_creation(
            "testuser1", "password", "password", 1)
        user1 = self.repository.fetch_selected_user("testuser1")
        user1_role = None
        if user1:
            user1_role = user1.role
        self.assertEqual(user1_role, Role.ADMIN)
