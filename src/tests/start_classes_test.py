import unittest
from services.contact_management import ContactManagement
import dummy_data
from initialize_database import initialize_database

class TestStartClasses(unittest.TestCase):
    
    def setUp(self):
        self.contact_management = ContactManagement()
        self.db = initialize_database()

    
    def test_contact_management_object_created(self):
        is_contact_management = bool(type(dummy_data.contact_management == ContactManagement))
        self.assertEqual(is_contact_management, True)

    def test_create_dummy_data_with_poetry_command(self):
        contact_n = dummy_data.contact_n
        n_of_data_at_beginning = len(self.contact_management.fetch_all_contacts_as_tuples())
        dummy_data.contact_management.create_dummy_content(contact_n)
        n_of_data_after_dummy_data_creation = len(self.contact_management.fetch_all_contacts_as_tuples())
        self.assertEqual(n_of_data_after_dummy_data_creation, n_of_data_at_beginning + contact_n)



    
    def test_init_database(self):
        pass



    
    ## Tests to be written
    # Initialize database
    # Create dummy data
    # Create service_class objects
    # Launch app