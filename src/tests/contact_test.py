import unittest
from services.contact_management import ContactManagement
from services.user_management import default_user_management
from entities.contact import Contact
from entities.user import User


class TestContactManagement(unittest.TestCase):
    def setUp(self):
        self.contact_management = ContactManagement()
        self.contact_management._user_management = default_user_management
        self.contact_management._user_management._logged_user = User("testuser", "salasana")
        self.t_contact = Contact(1, 1, 1, 1, "lorem ipsum")


    def test_submit_contact(self):
        dict_1 = self.contact_management.fetch_all_contacts()
        len_1 = len(dict_1)
        self.contact_management.submit_contact(self.t_contact)
        dict_2 = self.contact_management.fetch_all_contacts()
        len_2 = len(dict_2)
        self.assertEqual(len_1 + 1, len_2)
