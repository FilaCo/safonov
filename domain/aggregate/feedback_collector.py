from dataclasses import dataclass
from typing import List, Union


class Safonov:
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
            case "CollectReport":
                self.__collect_report(command)
            case "CollectFeedback":
                self.__collect_feedback(command)

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

    async def __collect_report(self, command: "CollectReport") -> List["Event"]:
        event = ReportCollected()

        return [event]

    async def __collect_feedback(self, command: "CollectFeedback") -> List["Event"]:
        event = FeedbackCollected()

        return [event]


Event = Union[
    "GoodsPaid",
    "CheckinStarted",
    "StudentCheckedIn",
    "CheckinFinished",
    "ManOfTheDayClaimed",
    "ReportCollected",
    "FeedbackCollected",
]

Command = Union[
    "PayForTheGoods",
    "StartCheckin",
    "CheckinStudent",
    "FinishCheckin",
    "ClaimManOfTheDay",
    "CollectReport",
    "CollectFeedback",
]

# Error = Union[]


# Events


@dataclass
class GoodsPaid:
    pass


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


@dataclass
class ReportCollected:
    pass


@dataclass
class FeedbackCollected:
    pass


# Commands


@dataclass
class PayForTheGoods:
    pass


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


@dataclass
class CollectReport:
    pass


@dataclass
class CollectFeedback:
    pass


# Errors
