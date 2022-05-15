import unittest
from services.contact_management import ContactManagement
from services.user_management import default_user_management
from entities.user import User
from initialize_database import initialize_database


class TestContactManagement(unittest.TestCase):
    def setUp(self):
        self.contact_management = ContactManagement()
        self.dummy_user = User("testuser", "password")
        self.contact_management._user_management = default_user_management
        self.contact_management._user_management.set_active_user(
            self.dummy_user)
        self.db = initialize_database()

    def test_submit_contact(self):
        dict_1 = self.contact_management.fetch_all_contacts_as_tuples()
        len_1 = len(dict_1)
        self.contact_management.manage_new_contact_submission(
            1, 1, 1, 1, "lorem ipsum")
        dict_2 = self.contact_management.fetch_all_contacts_as_tuples()
        len_2 = len(dict_2)
        self.assertEqual(len_1 + 1, len_2)

    def test_fetch_all_contacts(self):
        n = 4
        for i in range(n):
            self.contact_management.manage_new_contact_submission(
                1, 1, 1, 1, "lorem ipsum")
        contact_count = len(
            self.contact_management.fetch_all_contacts_as_tuples())
        self.assertEqual(n, contact_count)

    def test_fetch_contacts_by_user(self):
        n = 2
        for i in range(n):
            self.contact_management.manage_new_contact_submission(
                1, 1, 1, 1, "lorem ipsum")
        testuser = User("testuser2", "password")
        self.contact_management._user_management.set_active_user(testuser)
        k = 3
        for i in range(k):
            self.contact_management.manage_new_contact_submission(
                1, 1, 1, 1, "lorem ipsum")
        contact_count = len(
            self.contact_management.fetch_contacts_by_user(testuser))
        self.assertEqual(k, contact_count)

    def test_validity_check_fails_when_counseling_contact_is_missing_age(self):
        result = self.contact_management.manage_new_contact_submission(
            1, 1, 0, 1, "lorem ipsum")
        self.assertEqual(result[0], False)

    def test_validity_check_fails_when_counseling_contact_is_missing_gender(self):
        result = self.contact_management.manage_new_contact_submission(
            1, 1, 1, 0, "lorem ipsum")
        self.assertEqual(result[0], False)

    def test_validity_check_fails_when_counseling_contact_is_missing_content(self):
        result = self.contact_management.manage_new_contact_submission(
            1, 1, 1, 1, "")
        self.assertEqual(result[0], False)

    def test_validity_check_fails_when_counseling_contact_is_missing_type(self):
        result = self.contact_management.manage_new_contact_submission(
            0, 1, 1, 1, "lorem ipsum")
        self.assertEqual(result[0], False)

    def test_validity_check_passes_when_counseling_has_age_gender_content(self):
        result = self.contact_management.manage_new_contact_submission(
            1, 1, 1, 1, "lorem ipsum")
        self.assertEqual(result[0], True)

    def test_contact_is_returned_as_a_tuple(self):
        self.contact_management.manage_new_contact_submission(
                1, 1, 1, 1, "lorem ipsum")
        all_contacts = self.contact_management.fetch_all_contacts_as_tuples()
        row_id = all_contacts[0][0]
        contact = self.contact_management.fetch_selected_contact(row_id)
        self.assertEqual(tuple, type(contact))

    def test_returned_contact_is_correct(self):
        self.contact_management.manage_new_contact_submission(
                1, 1, 1, 1, "lorem ipsum 1")
        all_contacts = self.contact_management.fetch_all_contacts_as_tuples()
        row_id = all_contacts[0][0]
        self.contact_management.manage_new_contact_submission(
                1, 1, 1, 1, "lorem ipsum 2")
        contact = self.contact_management.fetch_selected_contact(row_id)
        content = contact[7]
        self.assertEqual("lorem ipsum 1", content)
    
    def test_treeview_content_value_count_matches(self):
        self.contact_management.create_random_contacts(10)
        treeview_values = self.contact_management.fetch_treeview_contact_info()
        n_of_values = len(treeview_values[0])
        self.assertEqual(6, n_of_values)
    
    def test_contact_deletion_succeeds(self):
        n = 10
        self.contact_management.create_random_contacts(n)
        self.contact_management.delete_contact(1)
        n_after_deletion = len(self.contact_management.fetch_all_contacts_as_tuples())
        self.assertEqual(n-1, n_after_deletion)

    def test_deleting_all_data_is_successful(self):
        n = 10
        self.contact_management.create_random_contacts(n)
        n_before_deletion = len(self.contact_management.fetch_all_contacts_as_tuples())
        self.contact_management.delete_all_contacts()
        n_after_deletion = len(self.contact_management.fetch_all_contacts_as_tuples())
        self.assertEqual(n_before_deletion - n, n_after_deletion)

    def test_marking_contact_for_deletion_works(self):
        n = 10
        self.contact_management.create_random_contacts(n)
        self.contact_management.mark_contact_for_deletion(1, "TRUE")
        self.contact_management.delete_marked_contacts()
        n_after_deletion = len(self.contact_management.fetch_all_contacts_as_tuples())
        self.assertEqual(n-1, n_after_deletion)

    def test_remove_marking_from_contact_marked_for_deletion_works(self):
        n = 10
        self.contact_management.create_random_contacts(n)
        self.contact_management.mark_contact_for_deletion(1, "TRUE")
        self.contact_management.mark_contact_for_deletion(1, "")
        self.contact_management.delete_marked_contacts()
        n_after_deletion = len(self.contact_management.fetch_all_contacts_as_tuples())
        self.assertEqual(n, n_after_deletion)

    def test_gender_removed_from_non_counseling_contact(self):
        self.contact_management.manage_new_contact_submission(
                1, 2, 1, 1, "lorem ipsum 2")
        contact = self.contact_management.fetch_all_contacts_as_tuples()
        self.assertEqual("None", contact[0][5])
    
    def test_age_removed_from_non_counseling_contact(self):
        self.contact_management.manage_new_contact_submission(
                1, 2, 1, 1, "lorem ipsum 2")
        contact = self.contact_management.fetch_all_contacts_as_tuples()
        self.assertEqual("None", contact[0][6])
