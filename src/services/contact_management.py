from random import randint
from datetime import datetime
from lorem_text import lorem
from entities.user import User
from entities.contact import Contact

from repositories.contact_data_repository import default_contact_repository
from repositories.user_repository import default_user_repository
from services.user_management import default_user_management


class ContactManagement:
    """A service class for managing contact-related functionalities

    Attributes:
        user_repository: a default repository for database queries
        contact_repository: a default repository for database queries
        user_management: default service class for user management
    """

    def __init__(self,
                 user_repository=default_user_repository,
                 contact_repository=default_contact_repository,
                 user_management=default_user_management
                 ):
        self._user_repository = user_repository
        self._contact_repository = contact_repository
        self._user_management = user_management

    def fetch_all_contacts_as_tuples(self):
        """Returns contact data as tuples for the treeview widget

        Returns:
            list: a list populated with tuples
        """
        return self._contact_repository.fetch_all_contacts_as_tuples()

    def fetch_selected_contact(self, rowid):
        """Returns the selected contact as a tuple

        Args:
            rowid (int): id of requested contact

        Returns:
            tuple: tuple of contact information
        """
        return self._contact_repository.fetch_selected_contact(rowid)

    def fetch_treeview_contact_info(self):
        """A method to query more compact data to populate the treeview widget

        Returns:
            list: list of tuples for the treeview
        """
        return self._contact_repository.fetch_treeview_contact_info()

    def fetch_contacts_by_user(self, user: User):
        """Queries contacts from a selected user.

        This method is not used. Will be deleted.

        Args:
            user (User): selected user

        Returns:
            dict: a dictionary of contacts
        """
        return self._contact_repository.fetch_contacts_by_user(user)

    def delete_contact(self, c_id):
        """A method to query a contact deletion.

        Note: not used by the application, but useful for automated tests.

        Args:
            c_id (_type_): An id to identify the contact to be deleted
        """
        self._contact_repository.delete_contact(c_id)

    def delete_all_contacts(self):
        """A method to query the deletion of all contact data
        """
        self._contact_repository.delete_all_data()

    def mark_contact_for_deletion(self, c_id, status):
        """Alters the deletion status of a contact.

        Args:
            c_id (int): an id to identify the selected contact
            status (str): given new status
        """
        if status == "TRUE":
            mark = "TRUE"
        else:
            mark = ""
        self._contact_repository.mark_for_deletion(c_id, mark)

    def _get_current_time_as_str(self):
        """A method for creating a string of the current date and time

        Returns:
            String: A string of date and time
        """
        time_of_submission = datetime.now()
        datetime_as_str = time_of_submission.strftime("%d.%m.%Y %H:%M")
        return datetime_as_str

    def delete_marked_contacts(self):
        """A method to query the deletion of of all contacts marked for deletion.
        """
        self._contact_repository.delete_marked()

    def manage_new_contact_submission(self,
                                      c_channel: int,
                                      c_type: int,
                                      c_age: int,
                                      c_gender: int,
                                      c_content: str):
        """A method to manage submission of a new contact.

        Calls methods to create a date and time String and to validate given data.

        Args:
            c_channel (int): selected channel
            c_type (int): selected type
            c_age (int): selected age
            c_gender (int): selected gender
            c_content (str): written content

        Returns:
            boolean, String: returns a boolean indicating whether submission succeeded
            and a string of possible status information
        """
        datetime_as_str = self._get_current_time_as_str()
        if c_type != 1:
            c_age = 0
            c_gender = 0
            c_content = ""
        contact = Contact(datetime_as_str, c_channel,
                          c_type, c_age, c_gender, c_content)
        result, status_msg = contact.is_valid()
        if result:
            self.submit_contact(contact)
        return result, status_msg

    def submit_contact(self, contact: Contact):
        """A method for submitting a contact

        Args:
            contact (Contact): New contact to be submitted

        Returns:
            False, String: If fails, returns False and a string of status information.
            method call: If succeeds, call a method to add contact to databse.
        """
        fetch_user = self._user_management.get_active_user()
        if not fetch_user:
            return False, "Error. No user logged in."
        username = fetch_user.username
        return self._contact_repository.add_contact(username, contact)

    def create_random_contact(self):
        """A method for creating dummy contact data. Method uses randint to
        select username and contact selected variables. If contact type is
        counseling, another method is called to create dummy content. The finished
        contact is passed to another method that handles contact submission.
        """
        rand_users = ["carol", "cynthia", "max", "alex", "murphy", "peter",
                      "jill", "jane", "rhonda", "whoopie", "keanu", "johnny", "fiona"]
        random_user = rand_users[randint(0, len(rand_users)-1)]
        c_channel = randint(1, 3)
        c_type = randint(1, 4)
        c_age = randint(1, 7)
        c_gender = randint(1, 4)
        if c_type == 1:
            contact = Contact("", c_channel, c_type, c_age, c_gender, "")
            content = self.create_dummy_content(contact)
        else:
            content = ""
        return self.manage_dummy_contact_submission(random_user,
                                                    c_channel, c_type, c_age, c_gender, content)

    def manage_dummy_contact_submission(self,
                                        user: str,
                                        c_channel: int,
                                        c_type: int,
                                        c_age: int,
                                        c_gender: int,
                                        c_content: str):
        """A method for managing dummy data creation

        Args:
            user (str): dummy username
            c_channel (int): dummy channel
            c_type (int): dummy type
            c_age (int): dummy age
            c_gender (int): dummy gender
            c_content (str): dummy content

        Returns:
            (True, String): If success, return True and an empty string
            (False, String): False if something fails and a String of status information
        """
        datetime_as_str = self._get_current_time_as_str()
        if c_type != 1:
            c_age = 0
            c_gender = 0
            c_content = "No content (only counseling contacts have age, gender and a description)."
        contact = Contact(datetime_as_str, c_channel,
                          c_type, c_age, c_gender, c_content)
        result, status_msg = contact.is_valid()
        if result:
            self._submit_dummy_contact(user, contact)
        return result, status_msg

    def _submit_dummy_contact(self, user: str, contact: Contact):
        """A method for submitting new dummy contact

        Args:
            user (str): a username
            contact (Contact): contact object
        """
        self._contact_repository.add_contact(user, contact)

    def create_random_contacts(self, given_n=10):
        """A method for creating multiple dummy contacts.

        Calls a method to create a dummy contact as many times as given as an argument.

        Args:
            given_n (int, optional): Number of contacts to create. Defaults to 10.
        """

        for _ in range(given_n):
            result, status_msg = self.create_random_contact()
            if not result:
                return False, status_msg
        return True, ""

    def create_dummy_content(self, contact: Contact):
        """A method for creating dummy content from dummy quantitative data and lorem ipsum.

        In selected topics referral information is also created.

        Args:
            contact (Contact): contact object

        Returns:
            String: returns created content.
        """
        c_channel = default_contact_repository.contact_dict[contact.channel]
        age = default_contact_repository.contact_dict[contact.age]
        randtopic = [
            "mental health",
            "phsyical health",
            "bullying",
            "family relationships",
            "child abuse",
            "sexuality",
            "puberty",
            "peer relationships",
            "school",
        ]
        intro = f"A child/youth aged {age} contacted the helpline's {c_channel} service. "
        topic_id = randint(0, len(randtopic)-1)
        topics = f"They wanted to talk about {randtopic[topic_id]}. "
        topics += "A summary of the discussion: \n\n"
        dummytext = lorem.paragraph()
        content = intro + topics + dummytext
        if topic_id < 5:
            content += "\n\nI referred the child to appropriate services"
            content += f" that provide more help with {randtopic[topic_id]}"
        return content
