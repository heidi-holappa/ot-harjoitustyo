from repositories.user_repository import default_user_repository
from entities.user import User


class UserManagement:
    def __init__(self,
                 user_repository=default_user_repository):
        self._user_repository = user_repository
        self._active_user = None

    def get_user(self, username: str):
        return self._user_repository.fetch_selected_user(username)

    def get_active_user_role(self):
        if self._active_user:
            return self._active_user.get_role()
        return None

    def get_all_users(self):
        return self._user_repository.fetch_all_users()

    def add_user(self, user: User):
        result = self._user_repository.add_user(user)
        if result:
            return True
        return False

    def login(self, username, password):
        user = User(username, password)
        self.set_active_user(user)
        user_found = self.get_user(user.username)
        if user_found and user.password_hash_valid(user_found.password):
            user.logged = True
            self._active_user = user
            return (True, user.role)
        return (False, None)

    def get_active_user(self):
        return self._active_user

    def set_active_user(self, user: User):
        self._active_user = user

    def handle_user_creation(self,
                             username: str,
                             password1: str,
                             password2: str,
                             is_admin: int):
        new_user = User(username, password1)
        valid_username = new_user.username_is_valid()
        if not valid_username[0]:
            return valid_username
        valid_password = new_user.password_is_valid(password1, password2)
        if not valid_password[0]:
            return valid_password
        self.set_active_user(new_user)
        if is_admin and self._active_user:
            self._active_user.set_admin()
        return self.create_user()

    def create_user(self):
        if not self._active_user:
            return (False, "No active user created.")
        username_found = self.get_user(self._active_user.username)
        if username_found:
            return (False, "Username already in use")
        hashed_password = self._active_user.get_hashed_password()
        self._user_repository.add_user(self.get_active_user(), hashed_password)
        return (True, "")

    def make_admin(self):
        if self._active_user:
            self._active_user.set_admin()

    def logout(self):
        self._active_user = None


default_user_management = UserManagement()
