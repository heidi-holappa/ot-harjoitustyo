from enum import Enum
from werkzeug.security import check_password_hash, generate_password_hash

class Role(Enum):
    COUNSELOR = "counselor"
    ADMIN = "admin"


class User:

    """Class to create user objects

    Attributes:
        username: username chosen for the account
        password: password chosen for the account
        role: user's role (defaults to Role.COUNSELOR)
    """

    def __init__(self, username: str, password: str, role=Role.COUNSELOR):
        """Constructor to create a new User object

        Args:
            username (str): chosen username
            password (str): submitted password
            role (_type_, optional): chosen user role. Defaults to Role.COUNSELOR.
        """
        self.username = username
        self.password = password
        self.role = role
        self.logged = False

    def get_role(self):
        """method to get the attribute role of the user object

        Returns:
            value of enum Role
        """
        return self.role.value

    def set_admin(self):
        """Sets user's role to admin
        """
        self.role = Role.ADMIN

    def username_is_valid(self):
        """Validates given username. Used in account creation.

        Returns:
           (False, String): if password validation fails
           (True, String): if validation is success
        """
        
        status = ""
        is_valid = bool(len(self.username) > 4)
        if not is_valid:
            status += "Error: Username must have atleast four characters."
            return (False, status)
        return (True, status)

    def password_is_valid(self, password1: str, password2: str):
        """Validates given password. Used in account creation.

        Checks passwords match and password length is atleast one character

        Args:
            password1 (str): given password
            password2 (str): given re-typed password

        Returns:
            (False, String): if password validation fails
            (True, String): if validatoin succeeds.
        """
        pw_match = bool(password1 == password2)
        pw_long_enough = bool(len(password1) > 0)
        if pw_match and pw_long_enough:
            return (True, "")
        error = "Error: "
        if not pw_match:
            error += "Passwords do not match. "
        if not pw_long_enough:
            error += "Password must have 6 characters"
        return (False, error)

    def get_hashed_password(self):
        """Returns a generated hash for the password

        Returns:
            String: creates a hashed password
        """
        return generate_password_hash(self.password)

    def password_hash_valid(self, retrieved_password: str):
        """Checks whether given password matches the hashed password in database

        Args:
            retrieved_password (str): password stored in database

        Returns:
            True: if passwords match
            False: if passwords do not match
        """
        return check_password_hash(retrieved_password, self.password)
