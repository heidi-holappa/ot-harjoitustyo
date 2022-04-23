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

        cursor.execute('''SELECT ROWID, username, datetime, channel,
                type, gender, age, content FROM CONTACTS''')

        rows = cursor.fetchall()
        for row in rows:
            self._all_data[row["ROWID"]] = str(row["username"]) + ";" + str(row["datetime"]) + ";" + \
                str(row["channel"]) + ";" + str(row["type"]) + ";" + str(row["gender"]) + ";" + str(row["age"]) + \
                ";" + str(row["content"])
        return self._all_data

    def fetch_all_contacts_as_tuples(self):
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
        self._all_data = {}
        cursor = self._connection.cursor()

        cursor.execute('''SELECT ROWID, username, datetime, channel,
                type, gender, age, content FROM CONTACTS
                WHERE username=?''', [user.username])

        rows = cursor.fetchall()
        for row in rows:
            self._all_data[row["ROWID"]] = str(row["username"]) + ";" + str(row["datetime"]) + ";" + \
                str(row["channel"]) + ";" + str(row["type"]) + ";" + str(row["gender"]) + ";" + str(row["age"]) + \
                ";" + str(row["content"])
        return self._all_data

    def add_contact(self, user: User, contact: Contact):
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
                       [user.username,
                        contact.datetime_as_str,
                        contact.channel,
                        contact.type,
                        contact.age,
                        contact.gender,
                        contact.content,
                        contact.marked]
                       )
        self._connection.commit()

    # REMOVE THIS WHEN DELETE MARKED IS INTEGRATED TO APP
    def delete_contact(self, c_id):
        cursor = self._connection.cursor()
        cursor.execute('''DELETE FROM CONTACTS
                        WHERE ROWID = ?''', [c_id])
        self._connection.commit()

    def mark_for_deletion(self, c_id):
        cursor = self._connection.cursor()
        cursor.execute(''' UPDATE CONTACTS
                            SET marked = 1
                            WHERE ROWID = ?''', [c_id])
        self._connection.commit()

    def delete_marked(self):
        cursor = self._connection.cursor()
        cursor.execute('''DELETE FROM CONTACTS
                        WHERE MARKED = 1''')
        self._connection.commit()


default_contact_repository = ContactDataRepository(get_database_connection())
