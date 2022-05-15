from database_connection import get_database_connection
from entities.contact import Contact
from entities.contact import ContactChannel, ContactType, Gender, AgeGroup
from entities.user import User


class ContactDataRepository:
    """A class for managing database queries for Contact objects.

    Attributes:
        connection: database connection
        _all_data (): a variable for handling fetched data
        _contact_dict = values for data types used in data submission form
    """

    def __init__(self, connection):
        """Constructor for the class.

        Initializes database, initializes variable _all_data.

        Args:
            connection (sqlite3 object): initialized database connection
        """
        self._connection = connection
        self._all_data = None

        self.contact_dict = {
            ContactChannel.PHONE: "phone",
            ContactChannel.CHAT: "chat",
            ContactChannel.E_LETTER: "e-letter",
            ContactType.COUNSELING: "counseling",
            ContactType.NON_COUNSELING: "non-counseling",
            ContactType.SILENT: "silent",
            ContactType.NON_TARGET: "non-target group",
            Gender.NOVALUE: None,
            Gender.GIRL: "girl",
            Gender.BOY: "boy",
            Gender.SOMETHING_ELSE: "something else",
            Gender.UNKNOWN: "unknown",
            AgeGroup.NOVALUE: None,
            AgeGroup.UNDER_9: "under 9",
            AgeGroup.FROM_9_TO_11: "9-11",
            AgeGroup.FROM_12_TO_14: "12-14",
            AgeGroup.FROM_15_TO_17: "15-17",
            AgeGroup.FROM_18_TO_21: "18-21",
            AgeGroup.FROM_22_TO_25: "22-25",
            AgeGroup.OVER_25: "over 25"
        }

    def fetch_all_contacts_as_tuples(self):
        """Method to return all contacts as tuples for the Treeview widget.

        Returns:
            list: returns a list with tuples.
        """
        self._all_data = []
        cursor = self._connection.cursor()

        cursor.execute('''SELECT ROWID, username, datetime, channel,
                type, gender, age, content, marked FROM CONTACTS''')

        rows = cursor.fetchall()
        for row in rows:
            self._all_data.append((
                str(row["ROWID"]),
                str(row["username"]),
                str(row["datetime"]),
                str(row["channel"]),
                str(row["type"]),
                str(row["gender"]),
                str(row["age"]),
                str(row["content"]),
                str(row["marked"])
            ))
        return self._all_data

    def fetch_treeview_contact_info(self):
        """Database query to fetch items shown in Treeview widget

        Returns:
            list: returns a list of tuples.
        """
        self._all_data = []
        cursor = self._connection.cursor()

        cursor.execute('''SELECT ROWID, username, datetime, channel,
                type, marked FROM CONTACTS''')

        rows = cursor.fetchall()
        for row in rows:
            self._all_data.append((
                str(row["ROWID"]),
                str(row["username"]),
                str(row["datetime"]),
                str(row["channel"]),
                str(row["type"]),
                str(row["marked"]),
            ))
        return self._all_data

    def fetch_selected_contact(self, rowid):
        """method to fetch a selected contact

        Args:
            rowid (int): rowid identifies the selected contact

        Returns:
            tuple: returns the selected information as a tuple.
        """
        cursor = self._connection.cursor()

        db_result = cursor.execute('''SELECT ROWID,
                                username, 
                                datetime, 
                                channel,
                                type,
                                gender,
                                age,
                                content,
                                marked FROM CONTACTS
                                WHERE ROWID=?
                                ''', [rowid]).fetchone()

        result = (
            db_result["ROWID"],
            db_result["username"],
            db_result["datetime"],
            db_result["channel"],
            db_result["type"],
            db_result["gender"],
            db_result["age"],
            db_result["content"],
            db_result["marked"],
        )
        return result

    def add_contact(self, username, contact: Contact):
        """Add's a new contact to the database

        Args:
            username (str): Username of the logged in user
            contact (Contact): contact object
        """
        cursor = self._connection.cursor()
        cursor.execute('''INSERT INTO CONTACTS
                        (username, 
                        datetime, 
                        channel, 
                        type, 
                        age, 
                        gender, 
                        content, 
                        marked) 
                        VALUES (?,?,?,?,?,?,?,?)''',
                       [username,
                        contact.datetime_as_str,
                        self.contact_dict[contact.channel],
                        self.contact_dict[contact.type],
                        self.contact_dict[contact.age],
                        self.contact_dict[contact.gender],
                        contact.content,
                        contact.marked]
                       )
        self._connection.commit()

    def mark_for_deletion(self, c_id, status):
        """Change the deletion status of a selected contact

        Args:
            c_id (int): rowid of the contact
            status (String): new status
        """
        cursor = self._connection.cursor()
        cursor.execute(''' UPDATE CONTACTS
                            SET marked = ?
                            WHERE ROWID = ?''', [status, c_id])
        self._connection.commit()

    def delete_marked(self):
        """Deletes all rows where value in column MARKED is TRUE.
        """
        cursor = self._connection.cursor()
        cursor.execute('''DELETE FROM CONTACTS
                        WHERE MARKED = "TRUE"''')
        self._connection.commit()

    def delete_all_data(self):
        """Deletes all data from table contact.

        This functionality is meant only for the demo product for testing convenience.
        """
        cursor = self._connection.cursor()
        cursor.execute('''DELETE FROM CONTACTS''')
        self._connection.commit()

    def delete_contact(self, c_id):
        """A method used in automated tests to test database management"""
        cursor = self._connection.cursor()
        cursor.execute('''DELETE FROM CONTACTS
                        WHERE ROWID = ?''', [c_id])
        self._connection.commit()

    def fetch_contacts_by_user(self, user: User):
        """Method to fetch all contacts from a selected user.

        Not currently used. As the feature to browse contacts by user
        is on future development list, I will leave this as ground work
        for future development.

        Args:
            user (User): user who's contacts are to be fetched.

        Returns:
            dict: returns a dictionary of contacts
        """
        self._all_data = {}
        cursor = self._connection.cursor()

        cursor.execute('''SELECT ROWID, username, datetime, channel,
                type, gender, age, content FROM CONTACTS
                WHERE username=?''', [user.username])

        rows = cursor.fetchall()
        for row in rows:
            self._all_data[row["ROWID"]] = str(row["username"]) + ";" + \
                str(row["datetime"]) + ";" + \
                str(row["channel"]) + ";" + \
                str(row["type"]) + ";" + \
                str(row["gender"]) + ";" + \
                str(row["age"]) + ";" + \
                str(row["content"])
        return self._all_data


default_contact_repository = ContactDataRepository(get_database_connection())
