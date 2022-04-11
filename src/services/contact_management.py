from entities.user import User
from entities.contact import Contact

from repositories.contact_data_repository import ContactDataRepository as default_contact_repository
from repositories.user_repository import UserRepository as default_user_repository


class ContactManagement:

    def __init__(self,
                 user_repository=default_user_repository,
                 contact_repository=default_contact_repository
                 ):
        self._user_repository = user_repository
        self._contact_repository = contact_repository
