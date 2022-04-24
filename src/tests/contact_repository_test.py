import unittest
from services.contact_management import ContactManagement
from repositories.contact_data_repository import default_contact_repository
from services.user_management import default_user_management
from entities.user import User
from initialize_database import initialize_database


class TestContactRepository(unittest.TestCase):

    def setUp(self):
        self.contact_management = ContactManagement()
        self.contact_management._user_management = default_user_management
        self.contact_management._user_management.create_active_user(
            "testuser", "password")
        self.db = initialize_database()
        self.contact_repository = default_contact_repository

    def test_fetch_treeview_info_returns_list(self):
        self.contact_management.create_random_contacts(10)
        results = self.contact_repository.fetch_treeview_contact_info()
        self.assertEqual(type(results), list)

    def test_fetch_treeview_info_contains_tuples(self):
        self.contact_management.create_random_contacts(10)
        results = self.contact_repository.fetch_treeview_contact_info()
        self.assertEqual(type(results[0]), tuple)

    def test_fetch_one_contact(self):
        self.contact_management.create_random_contacts(10)
        result = self.contact_repository.fetch_selected_contact(1)
        self.assertEqual(type(result), tuple)

    # Is this a sensible test? Ask in workshop
    def test_fetch_one_contact_has_nine_variables(self):
        self.contact_management.create_random_contacts(10)
        result = self.contact_repository.fetch_selected_contact(1)
        self.assertEqual(len(result), 9)

    def test_delete_contact(self):
        self.contact_management.create_random_contacts(10)
        n_of_contacts_before_deletion = len(
            self.contact_repository.fetch_all_contacts_as_tuples())
        self.contact_repository.delete_contact(1)
        n_of_contacts_after_deletion = len(
            self.contact_repository.fetch_all_contacts_as_tuples())
        self.assertEqual(n_of_contacts_before_deletion,
                         n_of_contacts_after_deletion + 1)

    def test_mark_for_deletion_is_by_default_an_empty_string(self):
        self.contact_management.create_random_contacts(10)
        contact_before_being_marked = self.contact_repository.fetch_selected_contact(
            1)
        mark = contact_before_being_marked[-1]
        self.assertEqual(mark, "")

    def test_value_in_column_marked_altered(self):
        self.contact_management.create_random_contacts(10)
        self.contact_repository.mark_for_deletion(1, "TRUE")
        contact_after_being_marked = self.contact_repository.fetch_selected_contact(
            1)
        mark = contact_after_being_marked[-1]
        self.assertEqual(mark, "TRUE")

    def test_mark_for_deletion_changes_status(self):
        self.contact_management.create_random_contacts(10)
        contact_before_being_marked = self.contact_repository.fetch_selected_contact(
            1)
        marked_before_change = contact_before_being_marked[-1]
        self.contact_repository.mark_for_deletion(1, "TRUE")
        contact_after_being_marked = self.contact_repository.fetch_selected_contact(
            1)
        marked_after_change = contact_after_being_marked[-1]
        self.assertNotEqual(marked_before_change, marked_after_change)

    def test_marked_contact_is_deleted(self):
        self.contact_management.create_random_contacts(10)
        self.contact_repository.mark_for_deletion(1, "TRUE")
        self.contact_repository.delete_marked()
        n_of_contacts_after_deletion = len(
            self.contact_repository.fetch_all_contacts_as_tuples())
        self.assertEqual(n_of_contacts_after_deletion, 9)

    def test_delete_all_data_deletes_all_data(self):
        self.contact_management.create_random_contacts(10)
        self.contact_repository.delete_all_data()
        n_of_contacts_after_deletion = len(
            self.contact_repository.fetch_all_contacts())
        self.assertEqual(n_of_contacts_after_deletion, 0)
