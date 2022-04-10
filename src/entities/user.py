from repositories.user_repository import UserRepository

class User:

    def __init__(self, username: str,  password: str):
        self.username = username
        self.password = password
        self.role = "counselor"
        self.logged = False

    def login(self):
        is_valid = False
        users = self.get_users()
        if self.username in users:
            if self.password == users[self.username][0]:
                self.role = users[self.username][0]
                self.logged = True
                is_valid = True
        return is_valid

    def set_admin(self):
        self.role = "admin"

    def get_users(self):
        users = UserRepository().fetch_all_users()
        if not users:
            return {}
        return users

    def create_user(self):
        users = self.get_users()
        if self.username in users:
            print("USERNAME ALREADY IN USE. ABORTING.")
            return False
        try:
            UserRepository().add_user(self)
        except Exception as ex:
            print("USER.PY.CREATE_USER(). CRITICAL DATABASE ERROR. NO USER CREATED")
            print("Error content: ", ex)
            return False

    # MAKE NEW METHOD FOR SQLITE AND GUI
    def __str__(self):
        users = self.get_users()
        result = ""
        result += "USERS AND ROLES:\n"
        result += "----------------\n"
        for account in users.items():
            result += "username: " + account[0] + ", role: " + account[1] + "\n"
        result += "----------------"
        return result

# CREATE DUMMY DATA
if __name__ == "__main__":
    user = User("pekka", "salasana")
    user.create_user()
    user2 = User("mauri", "salasana")
    user2.create_user()
    user3 = User("jorma", "salasana")
    user3.create_user()
    print(user)
