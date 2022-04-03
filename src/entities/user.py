

class User:

    def __init__(self, username: str,  password: str):
        self.username = username
        self.password =  password
        self.role = ""
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
    
    def get_users(self):
        try:
            with open("src/repositories/db_users.csv") as file:
                users = {}
                for row in file:
                    row = row.replace("\n", "")
                    parts = row.split(";")
                    users[parts[0]] = (parts[1], parts[2])            
                return users
        except:
            print("USER.PY.GET_USERS(). CRITICAL DATABASE ERROR. CAN NOT FETCH USERDATA")
            return {}

    def create_user(self):
        users = self.get_users()
        if self.username in users:
            print("USERNAME ALREADY IN USE. ABORTING.")
            return False
        else:
            try:
                with open("src/repositories/db_users.csv", "a") as file:
                    line = self.username + ";" + self.password + ";counselor\n"
                    file.write(line)
                    file.close
                return True
            except:
                print("USER.PY.CREATE_USER(). CRITICAL DATABASE ERROR. NO USER CREATED")
                return False


    def __str__(self):
        users = self.get_users()
        for user in users:
            print(user + ",role: " + users[user][1])
        return str(users)



if __name__ == "__main__":
    user = User("pekka", "salasana")
    user.create_user()
    user2 = User("mauri", "salasana")
    user2.create_user()
    user3 = User("jorma", "salasana")
    user3.create_user()
    print(user)