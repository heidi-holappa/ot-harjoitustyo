from random import randint
from datetime import datetime
from lorem_text import lorem
from entities.user import User
from entities.contact import Contact

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

    # DELETE THIS WHEN NOT NEEDED ANY MORE
    def fetch_all_contacts(self):
        return self._contact_repository.fetch_all_contacts()

    def fetch_all_contacts_as_tuples(self):
        return self._contact_repository.fetch_all_contacts_as_tuples()

    def fetch_selected_contact(self, rowid):
        return self._contact_repository.fetch_selected_contact(rowid)

    def fetch_treeview_contact_info(self):
        return self._contact_repository.fetch_treeview_contact_info()

    def fetch_contacts_by_user(self, user: User):
        return self._contact_repository.fetch_contacts_by_user(user)

    def delete_contact(self, c_id):
        self._contact_repository.delete_contact(c_id)

    def mark_contact_for_deletion(self, c_id):
        self._contact_repository.mark_for_deletion(c_id)

    def delete_marked_contacts(self):
        self._contact_repository.delete_marked()

    def manage_new_contact_submission(self, c_channel, c_type, c_age, c_gender, c_content):
        time_of_submission = datetime.now()
        datetime_as_str = time_of_submission.strftime("%d.%m.%Y %H:%M")
        if c_type != 1:
            c_age = 0
            c_gender = 0
            c_content = None
        contact = Contact(datetime_as_str, c_channel,
                          c_type, c_age, c_gender, c_content)
        result = contact.is_valid()
        if result[0]:
            self.submit_contact(contact)
        return result

    def submit_contact(self, contact: Contact):
        fetch_user = self._user_management.get_active_user()
        if not fetch_user:
            return (False, "Error. No user logged in.")
        return self._contact_repository.add_contact(fetch_user, contact)

    def create_random_contact(self):
        rand_users = ["carol", "cynthia", "max", "alex", "murphy", "peter",
                      "jill", "jane", "rhonda", "whoopie", "keanu", "johnny", "fiona"]
        self._user_management.create_active_user(
            rand_users[randint(0, len(rand_users)-1)], "password")
        c_channel = randint(1, 3)
        c_type = randint(1, 4)
        c_age = randint(1, 7)
        c_gender = randint(1, 4)
        if c_type == 1:
            contact = Contact("", c_channel, c_type, c_age, c_gender, "")
            content = self.create_dummy_content(contact)
        else:
            content = ""
        self.manage_new_contact_submission(
            c_channel, c_type, c_age, c_gender, content)

    def create_random_contacts(self, given_n=10):
        for _ in range(given_n):
            self.create_random_contact()

    def create_dummy_content(self, contact):
        c_channel = contact.get_channel()
        age = contact.get_age()
        gender = contact.get_gender()
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
        intro = f"A child/youth aged {age} contacted the helpline's {c_channel} service."
        topic_id = randint(0, len(randtopic)-1)
        topics = f"They wanted to talk about {randtopic[topic_id]}. A summary of the discussion: \n\n"
        dummytext = lorem.paragraph()
        content = intro + topics + dummytext
        if topic_id < 5:
            content += f"\n\nI referred the child to appropriate services that provide more help with {randtopic[topic_id]}"
        return content
