

class ConsoleIO:

    def __init__(self):
        self.attribute = ""

    def print_guide(self, content: dict):
        for key, value in content.items():
            print(f"{key}: {value}")

    def read_command(self):
        return input("> ")
    
    def output(self, printout):
        print(printout)
