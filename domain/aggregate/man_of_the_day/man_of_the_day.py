from dataclasses import dataclass
import random
from typing import List, Union
from domain.entity.student import StudentId
from domain.vo.version import Version


class ManOfTheDay:
    def __init__(self):
        self.__version = Version.min()

    def apply_many(self, events: List["ManOfTheDayEvent"]):
        for event in events:
            match event:
                case _ if isinstance(event, ManOfTheDayClaimed):
                    self.__man_of_the_day_claimed(event)

    def apply(self, event: "ManOfTheDayEvent"):
        self.apply_many([event])

    def handle_many(
        self, commands: List["ManOfTheDayCommand"]
    ) -> List["ManOfTheDayEvent"]:
        events = []

        for command in commands:
            match command:
                case _ if isinstance(command, ClaimManOfTheDay):
                    events.extend(self.__claim_man_of_the_day(command))

        return events

    def handle(self, command: "ManOfTheDayCommand") -> List["ManOfTheDayEvent"]:
        return self.handle_many([command])

    def __claim_man_of_the_day(
        self, command: "ClaimManOfTheDay"
    ) -> List["ManOfTheDayEvent"]:
        # TODO: Change to random.org usage
        motd = random.choice(command.candidates)

        event = ManOfTheDayClaimed(motd)

        self.apply(event)

        return [event]

    def __man_of_the_day_claimed(self, _: "ManOfTheDayClaimed"):
        self.__version.increment()


ManOfTheDayEvent = Union["ManOfTheDayClaimed"]

ManOfTheDayCommand = Union["ClaimManOfTheDay"]

# ManOfTheDayError = Union[]

# Events


@dataclass
class ManOfTheDayClaimed:
    motd: StudentId


# Commands


@dataclass
class ClaimManOfTheDay:
    candidates: List[StudentId]


# Errors
