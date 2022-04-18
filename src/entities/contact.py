
class Contact:

    def __init__(self, datetime_as_str, channel, c_type, age, gender, content):
        self.datetime_as_str = datetime_as_str
        self.channel = channel
        self.type = c_type
        self.age = age
        self.gender = gender
        self.content = content


    def is_valid(self):
        if not self.channel and not self.type:
            return (False, "Each contact must have a channel and a type.")
        counseling_is_valid = bool(self.age and self.gender and self.content)
        if self.type == 1 and not counseling_is_valid:
            return (False, "Counseling contact must include age, gender and description on content.")
        return (True , "")
            
            

