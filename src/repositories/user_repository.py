from entities.user import User
from database_connection import get_database_connection


class UserRepository:

    def __init__(self, connection):
        self._connection = connection

    def fetch_selected_user(self, username: str):
        cursor = self._connection.cursor()

        db_fetch = cursor.execute('''SELECT username, password, role
                                    FROM USERS WHERE username=?''', [username]).fetchone()
        fetched_user = User(db_fetch["username"], db_fetch["password"])
        if db_fetch["role"] == "admin":
            fetched_user.set_admin()
        return fetched_user

    def fetch_all_users(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT username, password, role FROM USERS")
        rows = cursor.fetchall()

        users = {}

        for row in rows:
            users[row["username"]] = (row["password"], row["role"])
        return users

    def add_user(self, new_user: User, password):
        cursor = self._connection.cursor()
        cursor.execute('''INSERT INTO USERS
                    (username, password, role) 
                    VALUES (?,?,?)''',
                       [new_user.username,
                        password,
                        new_user.role]
                       )
        self._connection.commit()


default_user_repository = UserRepository(get_database_connection())
