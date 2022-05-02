from enum import Enum

# Looking into adding Enums to Contact objets. Work still in progress


class Channel(Enum):
    PHONE = (1, "phone")
    CHAT = (2, "chat")
    E_LETTER = (3, "e-letter")


class Type(Enum):
    COUNSELING = "counseling"
    NON_COUNSELING = "non-counseling"
    SILENT = "silent"
    NON_TARGET = "non-target group"


class Gender(Enum):
    GIRL = "girl"
    BOY = "boy"
    SOMETHING_ELSE = "something else"
    UNKNOWN = "unknown"


class Age(Enum):
    UNDER_9 = "under 9"
    FROM_9_TO_11 = "9-11"
    FROM_12_TO_14 = "12-14"
    FROM_15_TO_17 = "15-17"
    FROM_18_TO_21 = "18-21"
    FROM_22_TO_25 = "22-25"
    OVER_25 = "over 25"


class Contact:

    def __init__(self, datetime_as_str: str, channel, c_type, age, gender, content: str):
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
        self.marked = ""

    def is_valid(self):
        if not self.channel or not self.type:
            return (False, "Each contact must have a channel and a type.")
        counseling_is_valid = bool(self.age and self.gender and self.content)
        if self.type == self.contact_dict["type"][1] and not counseling_is_valid:
            return (False,
                    "Counseling contact must include age, gender and description on content.")
        return (True, "")
