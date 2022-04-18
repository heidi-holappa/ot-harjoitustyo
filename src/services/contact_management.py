from entities.user import User
from entities.contact import Contact
from datetime import datetime

from repositories.contact_data_repository import default_contact_repository
from repositories.user_repository import default_user_repository
from services.user_management import default_user_management


class ContactManagement:

    def __init__(self,
                 user_repository=default_user_repository,
                 contact_repository=default_contact_repository,
                 user_management=default_user_management
                 ):
        self._user_repository = user_repository
        self._contact_repository = contact_repository
        self._user_management = user_management

    def fetch_all_contacts(self):
        return self._contact_repository.fetch_all_contacts()

    def fetch_contacts_by_user(self, user: User):
        return self._contact_repository.fetch_contacts_by_user(user)

    def delete_contact(self, id):
        self._contact_repository.delete_contact(id)

    def manage_new_contact_submission(self, c_channel, c_type, c_age, c_gender, c_content):
        time_of_submission = datetime.now()
        datetime_as_str = time_of_submission.strftime("%d.%m.%Y %H:%M")
        contact = Contact(datetime_as_str, c_channel, c_type, c_age, c_gender, c_content)
        result = contact.is_valid()
        if result[0]:
            self.submit_contact(contact)
        return result

    def submit_contact(self, contact: Contact):
        fetch_user = self._user_management.get_active_user()
        if not fetch_user:
            return (False, "Error. No user logged in.")
        return self._contact_repository.add_contact(fetch_user, contact)

