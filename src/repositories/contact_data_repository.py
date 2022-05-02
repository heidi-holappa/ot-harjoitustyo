from database_connection import get_database_connection
from entities.contact import Contact
from entities.user import User


class ContactDataRepository:
    """A class for managing database queries for Contact objects.

    Attributes:
        connection: database connection
        _all_data (): a variable for handling fetched data
    """

    def __init__(self, connection):
        """Constructor for the class. 

        Initializes database, initializes variable _all_data. 

        Args:
            connection (sqlite3 object): initialized database connection
        """
        self._connection = connection
        self._all_data = None

    def fetch_all_contacts(self):
        """A method to fetch all contacts stored in database

        Returns:
            Dictionary: returns a dictionary. Rowid's are key's, Strings of data are values. 
        """
        self._all_data = {}
        cursor = self._connection.cursor()

        cursor.execute('''SELECT ROWID, username, datetime, channel,
                type, gender, age, content FROM CONTACTS''')

        rows = cursor.fetchall()
        for row in rows:
            self._all_data[row["ROWID"]] = str(row["username"]) + ";" + \
                str(row["datetime"]) + ";" + \
                str(row["channel"]) + ";" + \
                str(row["type"]) + ";" + \
                str(row["gender"]) + \
                ";" + str(row["age"]) + \
                ";" + str(row["content"])
        return self._all_data

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

    def fetch_contacts_by_user(self, user: User):
        """Method to fetch all contacts from a selected user. 

        Not currently used. Will most likely be deleted. 

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
                        contact.channel,
                        contact.type,
                        contact.age,
                        contact.gender,
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

    # REMOVE THIS WHEN DELETE MARKED IS INTEGRATED TO APP
    def delete_contact(self, c_id):
        """An obsolete method to be deleted when it is certain it is not used anymore"""
        cursor = self._connection.cursor()
        cursor.execute('''DELETE FROM CONTACTS
                        WHERE ROWID = ?''', [c_id])
        self._connection.commit()


default_contact_repository = ContactDataRepository(get_database_connection())
