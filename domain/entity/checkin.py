from enum import Enum


class Checkin:
    def __init__(self, state: "State"):
        self.__state = state


class State(Enum):
    Started = 0
    Finished = 1
