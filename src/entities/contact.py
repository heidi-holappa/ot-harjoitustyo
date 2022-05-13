from enum import Enum


class ContactChannel(Enum):
    """Enum constants for data values regarding selected channel
    in the data submission view.

    Args:
        Enum (int): integer values that match the IntVar attributes in GUI-radiobuttons.
    """
    NOVALUE = 0
    PHONE = 1
    CHAT = 2
    E_LETTER = 3


class ContactType(Enum):
    """Enum constants for data values regarding selected contact type
    in the data submission view

    Args:
        Enum (int): integer values that match the IntVar attributes in GUI-radiobuttons.
    """
    NOVALUE = 0
    COUNSELING = 1
    NON_COUNSELING = 2
    SILENT = 3
    NON_TARGET = 4


class Gender(Enum):
    """Enum constants for data values regarding selected gender in the data submisison view.

    Args:
        Enum (int): integer values that match the IntVar attributes in GUI-radiobuttons.
    """
    NOVALUE = 0
    GIRL = 1
    BOY = 2
    SOMETHING_ELSE = 3
    UNKNOWN = 4


class AgeGroup(Enum):
    """Enum constans for data values regarding selected Age in th edata submission view.

    Args:
        Enum (int): integer values that match the IntVar attributes in GUI-radiobuttons.
    """
    NOVALUE = 0
    UNDER_9 = 1
    FROM_9_TO_11 = 2
    FROM_12_TO_14 = 3
    FROM_15_TO_17 = 4
    FROM_18_TO_21 = 5
    FROM_22_TO_25 = 6
    OVER_25 = 7


class Contact:
    """Class for creating Contact objects

    Attributes:
        datetime_as_str: current date and time as String
        channel: selected channel for contact
        c_type: selected type for contact
        age: selected age
        gender: selected gender
        content: possible written content for the contact
    """

    def __init__(self,
                datetime_as_str: str,
                channel: int,
                c_type: int,
                age: int,
                gender: int,
                content: str):
        """Constructor for the class to create new contact objects.

        Args:
            datetime_as_str (str): current date and time
            channel (Enum): selected channel
            c_type (Enum): selected type
            age (Enum): selected age
            gender (Enum): selected gender
            content (str): content for the contact
            marked: "informs whether the contact is marked for deletion"
        """

        self.datetime_as_str = datetime_as_str
        self.channel = ContactChannel(channel)
        self.age = AgeGroup(age)
        self.type = ContactType(c_type)
        self.gender = Gender(gender)
        self.content = content
        self.marked = ""

    def is_valid(self):
        """Checks the validity of given data.

        Counseling contacts must have age, gender and written content.

        Returns:
            (False, String): if information is missing
            (True, String): if validation succeeds.
        """
        if not self.channel.value or not self.type.value:
            return False, "Each contact must have a channel and a type."
        counseling_is_valid = bool(
            self.age.value and self.gender.value and self.content)
        if self.type == ContactType.COUNSELING and not counseling_is_valid:
            return False, "Counseling contact must include age, gender and description on content."
        return True, ""
