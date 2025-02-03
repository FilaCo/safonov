from enum import Enum
from domain.entity.student import Student


class Report:
    def __init__(self, id: "ReportId", author: Student):
        self.__id = id
        self.__author = author


class ReportId:
    pass


class PracticeKind(Enum):
    BASIC = 0
    ASYNC = 1
    INTERACTION_PROTOCOLS = 2
    SPEED_AND_RELIABLITY = 3
    CHAT_BOTS = 4
    SYSTEM_DESIGN_CASE = 5
    FINAL = 6
