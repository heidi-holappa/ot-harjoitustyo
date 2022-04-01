from services.console_io import ConsoleIO


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
        self._io.output("ENTER USERNAME")
        username = self._io.read_command()
        self._io.output("ENTER PASSWORD")
        password = self._io.read_command()

        # VALIDATE LOGIN HERE

        CounselorStart().start()
    

class CreateAccount:

    def __init__(self):
        self._io = ConsoleIO()
    
    def start(self):
        self._io.output("ENTER USERNAME")
        username = self._io.read_command()
        self._io.output("ENTER PASSWORD")
        password = self._io.read_command()
        self._io.output("RE-ENTER PASSWORD")
        password2 = self._io.read_command

        if not bool(password == password2):
            self._io.output("ERROR: PASSWORDS DO NOT MATCH. START AGAIN.")
            self.start()
        else:
            self._io.output("SUCCESS. YOU CAN NOW LOGIN.")
            StartScreen().start()
            
            

class CounselorStart:

    def __init__(self):
        self._io = ConsoleIO()
        self.commands_counselor = {
            "X" : "LOGOUT",
            "1" : "SUBMIT DATA"
        }

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
                CounselorSubmit().start()

class CounselorSubmit:

    def __init__(self):      
        self._io = ConsoleIO()
        self._data = {
            "channel": "",
            "type": "",
            "age": "",
            "gender": "",
            "content": "",

        }
        self.commands_channel = {
            "X": "CANCEL SUBMISSION",
            "1": "PHONE",
            "2": "CHAT",
            "3": "E-LETTER",
        }
        self.commands_type = {
            "X": "CANCEL SUBMISSION",
            "1": "COUNSELING",
            "2": "NON-COUNSELING",
            "3": "SILENT",
            "4": "NON-TARGET GROUP",
        }
        self.commands_age = {
            "X": "CANCEL SUBMISSION",
            "B": "GO BACK",
            "1": "UNDER 9",
            "2": "9-11 Y",
            "3": "12-14 Y",
            "4": "15-17 Y",
            "5": "18-21 Y",
            "6": "22-25 Y",
            "7": "OVER 25"
        }
        self.commands_gender  = {
            "X": "CANCEL SUBMISSION",
            "B": "GO BACK",
            "1": "GIRL",
            "2": "BOY",
            "3": "SOMETHING ELSE",
            "3": "UNKNOWN"
        }
        self.commands_confirm = {
            "X": "CANCEL SUBMISSION",
            "Y": "SUBMIT",
            "B": "GO BACK"
        }

    def start(self):
        self._io.output("SUBMIT NEW CONTACT")
        self.submit_channel()

        
    def submit_channel(self):
        while True:
            commands = self.commands_channel
            self._io.print_guide(commands)
            command = self._io.read_command()
            if not command in commands:
                print("ERROR: INVALID COMMAND. TRY AGAIN")
            elif command == "X":
                CounselorStart().start()
            else:
                self._data["channel"] = commands[command]
                self.submit_type()

    def submit_type(self):
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
        while True:
            self._io.output("INPUT CONTENT")
            content = self._io.read_command()
            if len(content) == 0:
                print("ERROR: CONTENT CANNOT BE EMPTY. TRY AGAIN")
            else:
                self._data["content"] = content
                self.confirm_submit()

    def confirm_submit(self):
        self._io.print_guide(self._data)
        self._io.output("")
        self._io.output("1: CONFIRM DATA")
        self._io.output("2: CANCEL AND RESTART DATA SUBMISSION")
        while True:
            command = self._io.read_command()
            if command != "1" and command != "2":
                self._io.output("ERROR. INVALID COMMAND. TRY AGAIN.")
            elif command == 1:
                # SAVE DATA TO REPOSITORY
                self._io.output("DATA SUCCESSFULLY STORED")
                self.clear_data()
                CounselorStart().start()
            else:
                # DO SAVE DATA
                self._io.output("DATA SUCCESSFULLY STORED")
                self.clear_data()
                CounselorStart().start()

    def clear_data(self):
        for key in self._data:
            self._data[key] = ""
