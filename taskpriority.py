from enum import Enum

class TaskPriority(Enum):
    HIGH = 1
    MEDIUM_HIGH = 2
    MEDIUM = 3
    MEDIUM_LOW = 4
    LOW = 5
    EXTENDED = 6

    #TODO: Document the method
    def __lt__(self, other):
        return self.value > other.value

    def __le__(self, other):
        return self.value >= other.value

