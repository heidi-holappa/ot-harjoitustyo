from entities.user import User
from entities.contact import Contact

from repositories.contact_data_repository import default_contact_repository
from repositories.user_repository import UserRepository as default_user_repository
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

    def submit_contact(self, contact: Contact):
        print("Now in ContactManagement. Contact content: ", contact.content, contact, self._user_management)        
        fetch_user = self._user_management.get_logged_user()
        print("user: ", fetch_user, "contact: ", contact)
        self._contact_repository.add_contact(fetch_user, contact)

    def fetch_all_contacts(self):
        return self._contact_repository.fetch_all_contacts()

    def fetch_contacts_by_user(self, user: User):
        return self._contact_repository.fetch_contacts_by_user()
