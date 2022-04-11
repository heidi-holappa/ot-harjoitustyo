from repositories.user_repository import default_user_repository
from entities.user import User


class UserManagement:
    def __init__(self,
                 user_repository=default_user_repository):
        self._user_repository = user_repository
        self._logged_user = None

    def password_is_valid(self, password1: str, password2: str):
        # Password validation can be expanded easily
        return password1 == password2

    def get_user(self, username: str):
        return self._user_repository.fetch_selected_user(username)

    def get_all_users(self):
        return self._user_repository.fetch_all_users()

    def add_user(self, user: User):
        result = self._user_repository.add_user(user)
        if result:
            return True
        return False

    def create_user(self, user: User):
        users = self.get_all_users()
        if user.username in users:
            print("USERNAME ALREADY IN USE. ABORTING.")
            return False
        try:
            self._user_repository.add_user(user)
        except Exception as ex:
            print("USER.PY.CREATE_USER(). CRITICAL DATABASE ERROR. NO USER CREATED")
            print("Error content: ", ex)
            return False
        return True

    def login(self, user: User):
        is_valid = False
        users = self.get_all_users()
        if user.username in users:
            if user.password == users[user.username][0]:
                user.role = users[user.username][1]
                user.logged = True
                is_valid = True
        self._logged_user = user
        print("logged: ", self._logged_user, self)
        return is_valid

    def get_logged_user(self):
        return self._logged_user


default_user_management = UserManagement()
