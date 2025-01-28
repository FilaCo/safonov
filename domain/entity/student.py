from uuid import UUID


class Student:
    def __init__(self, id: "StudentId"):
        self.__id = id


class StudentId:
    pass