from database_connection import get_database_connection
from entities.contact import Contact
from entities.user import User


class ContactDataRepository:

    def __init__(self, connection):
        self._connection = connection
        self._all_data = None

    def fetch_all_contacts(self):
        self._all_data = {}
        cursor = self._connection.cursor()

        cursor.execute('''SELECT ROWID, username, channel,
                type, gender, age, content FROM CONTACTS''')

        rows = cursor.fetchall()
        for row in rows:
            self._all_data[row["ROWID"]] = row["username"] + ";" + \
                row["channel"] + ";" + row["type"] + ";" + row["gender"] + ";" + row["age"] + \
                ";" + row["content"]
        return self._all_data

    def fetch_contacts_by_user(self, user: User):
        self._all_data = {}
        cursor = self._connection.cursor()

        cursor.execute('''SELECT ROWID, username, channel,
                type, gender, age, content FROM CONTACTS
                WHERE username=?''', [user.username])

        rows = cursor.fetchall()
        for row in rows:
            self._all_data[row["ROWID"]] = row["username"] + ";" + \
                row["channel"] + ";" + row["type"] + ";" + row["gender"] + ";" + row["age"] + \
                ";" + row["content"]
        return self._all_data

    def add_contact(self, user: User, contact: Contact):
        cursor = self._connection.cursor()
        cursor.execute('''INSERT INTO CONTACTS
                (username, datetime, channel, type, age, gender, content) VALUES (?,?,?,?,?,?,?)''',
                       [user.username,
                        contact.datetime_as_str,
                        contact.channel,
                        contact.type,
                        contact.age,
                        contact.gender,
                        contact.content]
                       )
        self._connection.commit()

    def delete_contact(self, id):
        cursor = self._connection.cursor()
        cursor.execute('''DELETE FROM CONTACTS
                        WHERE ROWID = ?''', [id])
        self._connection.commit()


default_contact_repository = ContactDataRepository(get_database_connection())
