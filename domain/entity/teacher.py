import uuid

from domain.vo.version import Version


class Teacher:
    def __init__(self, id: "TeacherId"):
        self.__id = id
        self.__version = Version()

    @property
    def id(self) -> "TeacherId":
        return self.__id


class TeacherId:
    def __init__(self):
        # Bad generation, better to use v7
        # see https://discuss.python.org/t/rfc-4122-9562-uuid-version-7-and-8-implementation/56725/3
        self.__value = uuid.uuid4()

    def __str__(self) -> str:
        return f"{self.__value}"

    def __eq__(self, other: "TeacherId"):
        return self.__value == other.__value

    def __ne__(self, other: "TeacherId"):
        return not (self == other)
