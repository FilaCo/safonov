import uuid


class Student:
    def __init__(self, id: "StudentId"):
        self.__id = id

    @property
    def id(self) -> "StudentId":
        self.__id


class StudentId:
    def __init__(self):
        # Bad generation, better to use v7
        # see https://discuss.python.org/t/rfc-4122-9562-uuid-version-7-and-8-implementation/56725/3
        self.__value = uuid.uuid4()

    def __str__(self) -> str:
        return f"{self.__value}"

    def __eq__(self, other: "StudentId"):
        return self.__value == other.__value

    def __ne__(self, other: "StudentId"):
        return not (self == other)
