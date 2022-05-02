from enum import Enum
from werkzeug.security import check_password_hash, generate_password_hash

class Role(Enum):
    COUNSELOR = "counselor"
    ADMIN = "admin"


class User:

    def __init__(self, username: str, password: str, role=Role.COUNSELOR):
        self.username = username
        self.password = password
        self.role = role
        self.logged = False

    def get_role(self):
        return self.role.value

    def set_admin(self):
        self.role = Role.ADMIN

    def username_is_valid(self):
        status = ""
        is_valid = bool(len(self.username) > 4)
        if not is_valid:
            status += "Error: Username must have atleast four characters."
            return (False, status)
        return (True, status)

    def password_is_valid(self, password1: str, password2: str):
        # Password validation can be expanded easily
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
        return generate_password_hash(self.password)

    def password_hash_valid(self, retrieved_password):
        return check_password_hash(retrieved_password, self.password)
