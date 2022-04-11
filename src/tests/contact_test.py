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
        self.testuser = User("testuser", "password")
        self.contact_management._user_management._logged_user = self.testuser
        self.t_contact = Contact(1, 1, 1, 1, "lorem ipsum")
        self.db = initialize_database()


    def test_submit_contact(self):
        dict_1 = self.contact_management.fetch_all_contacts()
        len_1 = len(dict_1)
        self.contact_management.submit_contact(self.t_contact)
        dict_2 = self.contact_management.fetch_all_contacts()
        len_2 = len(dict_2)
        self.assertEqual(len_1 + 1, len_2)
    
    def test_fetch_all_contacts(self):
        self.contact_management.submit_contact(self.t_contact)
        self.contact_management.submit_contact(self.t_contact)
        self.contact_management.submit_contact(self.t_contact)
        contact_count = len(self.contact_management.fetch_all_contacts())
        self.assertEqual(3, contact_count)
    
    def test_fetch_contacts_by_user(self):
        self.contact_management.submit_contact(self.t_contact)
        self.contact_management.submit_contact(self.t_contact)
        user2 = User("testuser2", "password")
        self.contact_management._user_management._logged_user = user2
        self.contact_management.submit_contact(self.t_contact)
        contact_count = len(self.contact_management.fetch_contacts_by_user(self.testuser))
        self.assertEqual(2, contact_count)
