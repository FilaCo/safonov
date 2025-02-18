from enum import Enum
import uuid
from domain.entity.student import StudentId


class Report:
    def __init__(self, id: "ReportId", author_id: StudentId):
        self.__id = id
        self.__author_id = author_id


class ReportId:
    def __init__(self):
        # Bad generation, better to use v7
        # see https://discuss.python.org/t/rfc-4122-9562-uuid-version-7-and-8-implementation/56725/3
        self.__value = uuid.uuid4()

    def __str__(self) -> str:
        return f"{self.__value}"

    def __eq__(self, other: "ReportId"):
        return self.__value == other.__value

    def __ne__(self, other: "ReportId"):
        return not (self == other)


class PracticeKind(Enum):
    BASIC = 0
    ASYNC = 1
    INTERACTION_PROTOCOLS = 2
    SPEED_AND_RELIABLITY = 3
    CHAT_BOTS = 4
    SYSTEM_DESIGN_CASE = 5
    FINAL = 6
