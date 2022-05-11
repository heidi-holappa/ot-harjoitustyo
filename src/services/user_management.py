from repositories.user_repository import default_user_repository
from entities.user import User, Role


class UserManagement:
    """A class for managing user related functionalities

    Attributes:
        user_repository: default repository for database queries
        _active_user: current logged in user (if any)
    """

    def __init__(self,
                 user_repository=default_user_repository):
        """A constructor for the class

        Args:
            user_repository (_type_, optional): Defaults to default_user_repository.
        """
        self._user_repository = user_repository
        self._active_user = None

    def get_user(self, username: str):
        """A method to query fetching of selected user

        Args:
            username (str): username to query for

        Returns:
            None: if no user is found
            User: user object of information found with the username
        """
        return self._user_repository.fetch_selected_user(username)

    def get_active_user_role(self):
        """A method to retrieve the role of the logged in user

        Returns:
            String: returns the value of the enum from class Role
        """
        if self._active_user:
            return self._active_user.role
        return None

    # DELETE IF NOT USED
    def get_all_users(self):
        """A method for querying all user data.

        Might not be used anymore. Make sure and delete if not in use.

        Returns:
            dict: Returns a dictionary of all users
        """
        return self._user_repository.fetch_all_users()

    def add_user(self, user: User):
        """Calls a repository method to add a new user

        Args:
            user (User): User object to be added

        Returns:
            True: if all succeeds
            False: if something fails
        """
        result = self._user_repository.add_user(user)
        if result:
            return True
        return False

    def login(self, username, password):
        """A method for attempting to login with the information provided

        Args:
            username (str): username submitted
            password (str): password submitted

        Returns:
            (False, None): If validation fails, return False and no role
            (True, String): if succeeds, return True and the role for the user
        """
        user = User(username, password)
        self.set_active_user(user)
        user_found = self.get_user(user.username)
        if user_found and user.password_hash_valid(user_found.password):
            user = user_found
            user.logged = True
            self._active_user = user
            return True, user.role
        return False, None

    def get_active_user(self):
        """Gets the attribute self._active_user

        Returns:
            None: If no user is currently logged in
            User: If a user is logged in.
        """
        return self._active_user

    def set_active_user(self, user: User):
        """Sets a user object as the active user

        Args:
            user (User): a user object of current logged in user
        """
        self._active_user = user

    def handle_user_creation(self,
                             username: str,
                             password1: str,
                             password2: str,
                             is_admin: int):
        """A method for handling account creation.

        Validates given information and calls for user creation if data is valid.

        Args:
            username (str): given username
            password1 (str): given password
            password2 (str): given re-typed password
            is_admin (int): boolean to indicate whether an admin account is to be created

        Returns:
            (False, String): If validation fails, returns False and a status as a String.
            method call: calls method self.create_user() which return a tuple
        """
        new_user = User(username, password1)
        valid_username, username_status_msg = new_user.username_is_valid()
        if not valid_username:
            return valid_username, username_status_msg
        valid_password, pw_status_msg = new_user.password_is_valid(
            password1, password2)
        if not valid_password:
            return valid_password, pw_status_msg
        self.set_active_user(new_user)
        if is_admin and self._active_user:
            self._active_user.set_admin()
        return self.create_user()

    def create_user(self):
        """A method for creating a new user.

        Handles repository queries, checks that username does not exist.

        Returns:
            (True, String): If success, return True
            (False, String): If fails, return False and a status notification as a String.
        """
        if not self._active_user:
            return (False, "No active user created.")
        username_found = self.get_user(self._active_user.username)
        if username_found:
            return (False, "Username already in use")
        hashed_password = self._active_user.get_hashed_password()
        self._user_repository.add_user(self.get_active_user(), hashed_password)
        return (True, "")

    def make_admin(self):
        """Set current user role to Role.ADMIN
        """
        if self._active_user:
            self._active_user.set_admin()

    def logout(self):
        """Clear active user.
        """
        self._active_user = None


default_user_management = UserManagement()
