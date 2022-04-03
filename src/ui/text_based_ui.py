from services.console_io import ConsoleIO
from entities.user import User
import os

class TextBasedUi:

    def __init__(self):
        self._io = ConsoleIO()

    def start(self):
        StartScreen().start()
        
class StartScreen:

    def __init__(self):
        self._io = ConsoleIO()
        self.commands_start = {
            "X": "QUIT",
            "1": Login(),
            "2": CreateAccount()
        }
        self.guide = {
            "X": "QUIT",
            "1": "LOGIN",
            "2": "CREATE ACCOUNT"
        }

    def start(self):
        self._io.print_guide(self.guide)
        while True:
            command = self._io.read_command()
            if not command in self.commands_start:
                self._io.output("ERROR: INVALID COMMAND. TRY AGAIN.")
                continue
            if command == "X":
                break
            command_object = self.commands_start[command]
            command_object.start()


class Login:

    def __init__(self):
        self._io = ConsoleIO()
    
    def start(self):
        self._io.output("----")
        self._io.output("LOGIN (PRESS ENTER TO CANCEL)")
        self._io.output("ENTER USERNAME")
        username = self._io.read_command()
        if len(username) == 0:
            start_screen = StartScreen()
            start_screen.start()
        self._io.output("ENTER PASSWORD")
        password = self._io.read_command()
        self._user = User(username, password)

        if self._user.login():
            CounselorStart(self._user).start()
        else:
            print("LOGIN FAILED. CHECK USERNAME AND PASSWORD")
            self.start()
    
class CreateAccount:

    def __init__(self):
        self._io = ConsoleIO()
    
    def start(self):
        self._io.output("----")
        self._io.output("CREATE ACCOUNT (PRESS ENTER TO CANCEL)")
        self._io.output("ENTER USERNAME")
        username = self._io.read_command()
        if len(username) == 0:
            start_screen = StartScreen()
            start_screen.start()
        self._io.output("ENTER PASSWORD")
        password = self._io.read_command()
        self._io.output("RE-ENTER PASSWORD")
        password2 = self._io.read_command()

        if not bool(password == password2):
            self._io.output("----")
            self._io.output("ERROR: PASSWORDS DO NOT MATCH. START AGAIN.")
            self._io.output("----")
            self.start()
        new_user = User(username, password)
        if new_user.create_user():
            start_screen = StartScreen()
            start_screen.start()
        else:
            print("CREATING NEW ACCOUNT FAILED. TRY AGAIN")
            self.start()
            
            

class CounselorStart:

    def __init__(self, user: User):
        self._io = ConsoleIO()
        self.commands_counselor = {
            "X" : "LOGOUT",
            "1" : "SUBMIT DATA"
        }
        self._user = user

    def start(self):
        while True:
            commands = self.commands_counselor
            self._io.print_guide(commands)
            command = self._io.read_command()
            if command not in commands:
                self._io.output("ERROR. INVALID COMMAND. TRY AGAIN.")
            elif command == "X":
                exit()
            else:
                CounselorSubmit(self._user).start()

class CounselorSubmit:

    def __init__(self, user: User):      
        self._io = ConsoleIO()
        self._user = user
        self._data = {
            "channel": "",
            "type": "",
            "age": "",
            "gender": "",
            "content": "",

        }
        self.commands_channel = {
            "1": "phone",
            "2": "chat",
            "3": "e-letter",
            "X": "CANCEL SUBMISSION",
        }
        self.commands_type = {
            "1": "counseling",
            "2": "non-counseling",
            "3": "silent",
            "4": "non-target group",
            "X": "CANCEL SUBMISSION",
        }
        self.commands_age = {
            "1": "under 9",
            "2": "9-11 y",
            "3": "12-14 y",
            "4": "15-17 y",
            "5": "18-21 y",
            "6": "22-25 y",
            "7": "over 25",
            "B": "GO BACK",
            "X": "CANCEL SUBMISSION",
        }
        self.commands_gender  = {
            "1": "girl",
            "2": "boy",
            "3": "something else",
            "4": "unknown",
            "B": "GO BACK",
            "X": "CANCEL SUBMISSION",
        }


    def start(self):
        self._io.output("NOW SUBMITTING A NEW CONTACT")
        self.submit_channel()

        
    def submit_channel(self):
        self._io.output("")
        self._io.output("CHANNEL:")
        while True:
            commands = self.commands_channel
            self._io.print_guide(commands)
            command = self._io.read_command()
            if not command in commands:
                print("ERROR: INVALID COMMAND. TRY AGAIN")
            elif command == "X":
                CounselorStart(self._user).start()
            else:
                self._data["channel"] = commands[command]
                self.submit_type()

    def submit_type(self):
        self._io.output("")
        self._io.output("TYPE:")
        while True:
            commands = self.commands_type
            self._io.print_guide(commands)
            command = self._io.read_command()
            if not command in commands:
                print("ERROR: INVALID COMMAND. TRY AGAIN")
            elif command == "X":
                self.start()
            elif command == "B":
                self.submit_channel()
            else:
                self._data["type"] = commands[command]
                self.submit_age()
    
    def submit_age(self):
        self._io.output("")
        self._io.output("AGE:")
        while True:
            commands = self.commands_age
            self._io.print_guide(commands)
            command = self._io.read_command()
            if not command in commands:
                print("ERROR: INVALID COMMAND. TRY AGAIN")
            elif command == "X":
                self.start()
            elif command == "B":
                self.submit_type()
            else:
                self._data["age"] = commands[command]
                self.submit_gender()

    def submit_gender(self):
        self._io.output("")
        self._io.output("GENDER:")
        while True:
            commands = self.commands_gender
            self._io.print_guide(commands)
            command = self._io.read_command()
            if not command in commands:
                print("ERROR: INVALID COMMAND. TRY AGAIN")
            elif command == "X":
                self.start()
            elif command == "B":
                self.submit_age()
            else:
                self._data["gender"] = commands[command]
                self.submit_content()
    
    def submit_content(self):
        self._io.output("")
        self._io.output("WRITE A DESCRIPTION OF THE CONTACT:")
        content = self._io.read_command()
        if len(content) == 0:
            self._io.output("ERROR: CONTENT CANNOT BE EMPTY. TRY AGAIN")
            self._io.output("")
            self.submit_content
        else:
            self._data["content"] = content
            self.confirm_submit()

    def confirm_submit(self):
        self._io.output("")
        self._io.output("REVIEW SUBMITTED DATA: ")
        self._io.output("----")
        self._io.print_guide(self._data)
        self._io.output("----")
        self._io.output("1: CONFIRM DATA")
        self._io.output("2: CANCEL AND RESTART DATA SUBMISSION")
        while True:
            command = self._io.read_command()
            if command != "1" and command != "2":
                self._io.output("ERROR. INVALID COMMAND. TRY AGAIN.")
            elif command == "1":
                self.save_data()
                self._io.output("DATA SUCCESSFULLY STORED")
                self.clear_data()
                CounselorStart(self._user).start()
            else:
                self._io.output("CANCELLING. NO DATA STORED")
                self.clear_data()
                CounselorStart(self._user).start()

    def save_data(self):
        try:
            save_path = "src/repositories"
            file_name = "db_contacts.csv"
            path_and_file = os.path.join(save_path, file_name)
            with open(path_and_file, "a") as file:
                line = ""
                for key in self._data:
                    line += self._data[key] + ";"
                line += "\n"
                file.write(line)
                file.close()
        except IOError as exception:
            raise IOError("ERROR: WRITING DATA FAILED.")


    def clear_data(self):
        for key in self._data:
            self._data[key] = ""
