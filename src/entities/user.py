class User:

    def __init__(self, username: str,  password: str, role="counselor"):
        self.username = username
        self.password = password
        self.role = role
        self.logged = False

    def get_role(self):
        return self.role

    def set_admin(self):
        self.role = "admin"

    # def __str__(self):
    #     result = f"username: {self.username}, role: {self.role}"
    #     return result
