from dataclasses import dataclass
from typing import Dict, List, Union
from uuid import UUID

from domain.entity.student import Student


class CourseParticipants:
    def __init__(self, participants: Dict[UUID, Student]):
        self.__participants = participants

    async def handle(self, command: "Command") -> List["Event"]:
        match command:
            case "StartCheckin":
                self.__start_checkin(command)
            case "CheckinStudent":
                self.__checkin_student(command)
            case "FinishCheckin":
                self.__finish_checkin(command)
            case "ClaimManOfTheDay":
                self.__claim_man_of_the_day(command)

    async def __start_checkin(self, command: "StartCheckin") -> List["Event"]:
        event = CheckinStarted()

        return [event]

    async def __checkin_student(self, command: "CheckinStudent") -> List["Event"]:
        event = StudentCheckedIn()

        return [event]

    async def __finish_checkin(self, command: "FinishCheckin") -> List["Event"]:
        event = CheckinFinished()

        return [event]

    async def __claim_man_of_the_day(
        self, command: "ClaimManOfTheDay"
    ) -> List["Event"]:
        event = ManOfTheDayClaimed()

        return [event]


Event = Union[
    "CheckinStarted",
    "StudentCheckedIn",
    "CheckinFinished",
    "ManOfTheDayClaimed",
]

Command = Union[
    "StartCheckin",
    "CheckinStudent",
    "FinishCheckin",
    "ClaimManOfTheDay",
]

# Error = Union[]


# Events


@dataclass
class CheckinStarted:
    pass


@dataclass
class StudentCheckedIn:
    pass


@dataclass
class CheckinFinished:
    pass


@dataclass
class ManOfTheDayClaimed:
    pass


# Commands


@dataclass
class StartCheckin:
    pass


@dataclass
class CheckinStudent:
    pass


@dataclass
class FinishCheckin:
    pass


@dataclass
class ClaimManOfTheDay:
    pass


# Errors
