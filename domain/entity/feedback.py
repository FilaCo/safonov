from domain.entity.student import Student


class Feedback:
    def __init__(self, author: Student):
        self.__author = author

