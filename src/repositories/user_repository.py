from entities.user import User
from database_connection import get_database_connection


class UserRepository:

    def __init__(self, connection):
        self._connection = connection

    def fetch_selected_user(self, username: str):
        cursor = self._connection.cursor()

        db_fetch = cursor.execute('''SELECT username, password, role
                                    FROM USERS WHERE username=?''', [username]).fetchone()
        fetched_used = User(db_fetch["username"], db_fetch["password"])
        if db_fetch["role"] == 1:
            fetched_used.set_admin()
        return fetched_used

    def fetch_all_users(self):
        # Try/except will be refactored
        try:
            cursor = self._connection.cursor()

            cursor.execute("SELECT username, password, role FROM USERS")
            rows = cursor.fetchall()

            users = {}

            for row in rows:
                users[row["username"]] = (row["password"], row["role"])
            return users
        except Exception as ex:
            print("Method fetch_all_users failed. Error-message: ", ex)
            return None

    def add_user(self, new_user: User, password):
        # Try/except will be refactored
        try:
            cursor = self._connection.cursor()
            cursor.execute('''INSERT INTO USERS
                        (username, password, role) 
                        VALUES (?,?,?)''',
                           [new_user.username,
                            password,
                            new_user.role]
                           )
            self._connection.commit()
            return True
        except Exception as ex:
            print("An error occured. Message: ", ex)
            return False


default_user_repository = UserRepository(get_database_connection())
