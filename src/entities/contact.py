from entities.user import User

class Contact:

    def __init__(self, user: User, channel, c_type, age, gender, content):
        self.user = user
        self.channel = channel
        self.type = c_type
        self.age = age
        self.gender = gender
        self.content = content
    