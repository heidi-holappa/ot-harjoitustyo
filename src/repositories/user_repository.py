from entities.user import User, Role
from database_connection import get_database_connection


class UserRepository:
    """A class for managing data queries related to user objects
    """

    def __init__(self, connection):
        """A constructor for the class.

        Args:
            connection (sqlite3 object): an initialized database connection
        """
        self._connection = connection

    def fetch_selected_user(self, username: str):
        """method to fetch a selected user

        Args:
            username (str): username used to fetch a row from database

        Returns:
            None: if now row is returned
            User: a user object created with the fetched information
        """
        cursor = self._connection.cursor()

        db_fetch = cursor.execute('''SELECT username, password, role
                                    FROM USERS WHERE username=?''', [username]).fetchone()
        if not db_fetch:
            return None
        fetched_user = User(db_fetch["username"], db_fetch["password"])
        fetched_user.role = Role(db_fetch["role"])
        return fetched_user

    def fetch_all_users(self):
        """method for fetching all user data.

        Returns:
            dict: returns a dictionary with usernames as keys and passwords and roles as items.
        """
        cursor = self._connection.cursor()

        cursor.execute("SELECT username, password, role FROM USERS")
        rows = cursor.fetchall()

        users = {}

        for row in rows:
            users[row["username"]] = (row["password"], row["role"])
        return users

    def add_user(self, new_user: User, password):
        """A method to add a new user

        Args:
            new_user (User): user object
            password (_type_): hashed password
        """
        cursor = self._connection.cursor()
        cursor.execute('''INSERT INTO USERS
                    (username, password, role) 
                    VALUES (?,?,?)''',
                       [new_user.username,
                        password,
                        new_user.role.value]
                       )
        self._connection.commit()

default_user_repository = UserRepository(get_database_connection())
