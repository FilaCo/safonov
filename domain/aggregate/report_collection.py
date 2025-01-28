from dataclasses import dataclass
from typing import List, Union

from domain.entity.student import Student


class ReportCollection:
    def __init__(self):
        pass

    async def handle(self, command: "Command") -> List["Event"]:
        match command:
            case _ if isinstance(command, "CollectReport"):
                self.__collect_report(command)

    async def __collect_report(self, command: "CollectReport") -> List["Event"]:
        pass


Command = Union["CollectReport"]
Event = Union["ReportCollected"]


@dataclass
class CollectReport:
    author: Student


@dataclass
class ReportCollected:
    pass
