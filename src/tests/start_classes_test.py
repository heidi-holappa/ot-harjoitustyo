import unittest
from services.contact_management import ContactManagement
import dummy_data
from initialize_database import initialize_database


class TestStartClasses(unittest.TestCase):

    def setUp(self):
        self.contact_management = ContactManagement()
        self.db = initialize_database()

    def test_contact_management_object_created(self):
        is_contact_management = bool(
            type(dummy_data.contact_management == ContactManagement))
        self.assertEqual(is_contact_management, True)

    def test_create_dummy_data(self):
        contact_n = dummy_data.CONTACT_N
        n_of_data_at_beginning = len(
            self.contact_management.fetch_all_contacts_as_tuples())
        dummy_data.contact_management.create_random_contacts(contact_n)
        n_of_data_after_dummy_data_creation = len(
            self.contact_management.fetch_all_contacts_as_tuples())
        self.assertEqual(n_of_data_after_dummy_data_creation,
                         n_of_data_at_beginning + contact_n)

    def test_init_database(self):
        n_of_data_at_beginning = len(
            self.contact_management.fetch_all_contacts_as_tuples())
        self.contact_management.create_random_contacts(30)
        self.db = initialize_database()
        n_of_data_at_end = len(
            self.contact_management.fetch_all_contacts_as_tuples())
        self.assertEqual(n_of_data_at_beginning, n_of_data_at_end)

