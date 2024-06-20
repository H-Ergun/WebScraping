from enum import Enum, auto

#2 kadın, 1 erkek, 3 belirtmek istemiyorum, 4 özel
class GenderEnum(Enum):
    ERKEK = auto()
    KADIN = auto()
    UNDIFENED = auto()
    PRIVACY=auto()