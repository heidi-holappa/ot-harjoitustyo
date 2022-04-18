import unittest
from services.contact_management import ContactManagement
from services.user_management import default_user_management
from entities.contact import Contact
from entities.user import User
from initialize_database import initialize_database


class TestContactManagement(unittest.TestCase):
    def setUp(self):
        self.contact_management = ContactManagement()
        self.contact_management._user_management = default_user_management
        self.contact_management._user_management.create_active_user("testuser", "password")
        self.db = initialize_database()

    def test_submit_contact(self):
        dict_1 = self.contact_management.fetch_all_contacts()
        len_1 = len(dict_1)
        self.contact_management.manage_new_contact_submission(1, 1, 1, 1, "lorem ipsum")
        dict_2 = self.contact_management.fetch_all_contacts()
        len_2 = len(dict_2)
        self.assertEqual(len_1 + 1, len_2)

    def test_fetch_all_contacts(self):
        n = 4
        for i in range(n):
            self.contact_management.manage_new_contact_submission(1, 1, 1, 1, "lorem ipsum")
        contact_count = len(self.contact_management.fetch_all_contacts())
        self.assertEqual(n, contact_count)

    def test_fetch_contacts_by_user(self):
        n = 2
        for i in range(n):
            self.contact_management.manage_new_contact_submission(1, 1, 1, 1, "lorem ipsum")
        self.contact_management._user_management.create_active_user("testuser2", "password")
        k = 3
        for i in range(k):
            self.contact_management.manage_new_contact_submission(1, 1, 1, 1, "lorem ipsum")
        testuser = User("testuser2", "password")
        contact_count = len(
            self.contact_management.fetch_contacts_by_user(testuser))
        self.assertEqual(k, contact_count)
