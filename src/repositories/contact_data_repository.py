from entities.contact import Contact
from entities.user import User

class ContactDataRepository:

    def __init__(self, connection):
        self._connection = connection
        self._all_data = None


    def fetch_all_contacts(self):
        self._all_data = {}
        cursor = self._connection.cursor()

        cursor.execute('''SELECT ROWID, username, datetime, channel,
                type, gender, age, content FROM CONTACTS''')

        rows = cursor.fetchall()
        for row in rows:
            # Perhaps create a contact object and populate it's attributes?
            self._all_data[row["ROWID"]] = row["username"] + ";" + row["datetime"] + ";" + \
                row["channel"] + ";" + row["type"] + ";" + row["gender"] + ";" + row["age"] + \
                    ";" + row["content"]
        return self._all_data


    def add_contact(self, user: User, contact: Contact):
        try:
            cursor = self._connection.cursor()
            cursor.execute('''INSERT INTO CONTACTS
                    (username, channel, type, age, gender, content) VALUES (?,?,?,?,?)''', \
                [user.username,
                contact.channel,
                contact.type,
                contact.age,
                contact.gender,
                contact.content]
                )
            cursor.commit()
        except Exception as ex:
            print("An error occured. Message: ", ex)
