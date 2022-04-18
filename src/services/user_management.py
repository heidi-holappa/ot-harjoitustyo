from repositories.user_repository import default_user_repository
from entities.user import User
from werkzeug.security import check_password_hash, generate_password_hash


class UserManagement:
    def __init__(self,
                 user_repository=default_user_repository):
        self._user_repository = user_repository
        self._active_user = None

    def password_is_valid(self, password1: str, password2: str):
        # Password validation can be expanded easily

        return password1 == password2

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

    def login(self):
        if not self._active_user:
            return (False, None)
        user = self._active_user
        users = self.get_all_users()
        print("Given password: ", user.password, "\n ,db: ", users[user.username][0], "check validity: ", check_password_hash(user.password,users[user.username][0]))

        if user.username in users and check_password_hash(users[user.username][0], user.password):
            user.role = users[user.username][1]
            user.logged = True
            self._active_user = user
            return (True, user.role)
        return (False, None)

    def get_active_user(self):
        return self._active_user

    def create_active_user(self, username, password):
        self._active_user = User(username, password)

    def handle_user_creation(self, username, password1, password2, is_admin):
        valid_password = self.password_is_valid(password1, password2)
        if not valid_password:
            return (False, "Passwords do not match. Try again.")
        self.create_active_user(username, password1)
        if is_admin and self._active_user:
            self._active_user.set_admin()
        return self.create_user()
        
    
    def create_user(self):
        if not self._active_user:
            return (False, "No active user created.")
        users = self.get_all_users()
        if self._active_user.username in users:
            return (False, "Username already in use")
        try:
            hashed_password = hashed_password = generate_password_hash(self._active_user.password)
            self._user_repository.add_user(self._active_user, hashed_password)
        except Exception as ex:
            return (False, ex)
        return (True, "")
    
    def make_admin(self):
        if self._active_user:
            self._active_user.set_admin()

    def logout(self):
        self._active_user = None


default_user_management = UserManagement()
