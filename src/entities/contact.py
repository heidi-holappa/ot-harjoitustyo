
class Contact:

    def __init__(self, datetime_as_str: str, channel: int, c_type: int, age: int, gender: int, content: str, marked = 0):
        self.contact_dict = {
            "channel": [None,
                        "phone",
                        "chat",
                        "e-letter"],
            "type": [None,
                     "counseling",
                     "non-counseling",
                     "silent",
                     "non-target group"],
            "gender": [None,
                       "girl",
                       "boy",
                       "something else",
                       "unknown"],
            "age": [None,
                    "under 9",
                    "9-11",
                    "12-14",
                    "15-17",
                    "18-21",
                    "22-25",
                    "over 25"]
        }

        self.datetime_as_str = datetime_as_str
        self.channel = self.contact_dict["channel"][channel]
        self.type = self.contact_dict["type"][c_type]
        self.age = self.contact_dict["age"][age]
        self.gender = self.contact_dict["gender"][gender]
        self.content = content
        self.marked = marked

    def is_valid(self):
        if not self.channel and not self.type:
            return (False, "Each contact must have a channel and a type.")
        counseling_is_valid = bool(self.age and self.gender and self.content)
        if self.type == 1 and not counseling_is_valid:
            return (False,
                    "Counseling contact must include age, gender and description on content.")
        return (True, "")

    def get_type(self):
        return self.type
    
    def get_age(self):
        return self.age
    
    def get_gender(self):
        return self.gender
    
    def get_channel(self):
        return self.channel
