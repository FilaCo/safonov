from dataclasses import dataclass
from typing import Dict, List, Union
import uuid

from domain.entity.student import StudentId
from domain.vo.version import Version


class Checkin:
    def __init__(self):
        self.__id = None
        self.__version = Version.min()
        self.__checked_in = None
        self.__finished = None

    def apply_many(self, events: List["CheckinEvent"]):
        for event in events:
            match event:
                case _ if isinstance(event, CheckinStarted):
                    self.__checkin_started(event)
                case _ if isinstance(event, CheckinFinished):
                    self.__checkin_finished(event)
                case _ if isinstance(event, ParticipantCheckedIn):
                    self.__participant_checked_in(event)
                case _ if isinstance(event, AllParticipantsCheckedIn):
                    self.__all_participants_checked_in(event)

    def apply(self, event: "CheckinEvent"):
        self.apply_many([event])

    def handle_many(self, commands: List["CheckinCommand"]) -> List["CheckinEvent"]:
        events = []

        for command in commands:
            match command:
                case _ if isinstance(command, StartCheckin):
                    events.extend(self.__start_checkin(command))
                case _ if isinstance(command, FinishCheckin):
                    events.extend(self.__finish_checkin(command))
                case _ if isinstance(command, CheckinParticipant):
                    events.extend(self.__checkin_participant(command))

        return events

    def handle(self, command: "CheckinCommand") -> List["CheckinEvent"]:
        return self.handle_many([command])

    def __start_checkin(self, command: "StartCheckin") -> List["CheckinEvent"]:
        event = CheckinStarted(command.checked_in)

        self.apply(event)

        return [event]

    def __finish_checkin(self, _: "FinishCheckin") -> List["CheckinEvent"]:
        event = CheckinFinished()

        self.apply(event)

        return [event]

    def __checkin_participant(
        self, command: "CheckinParticipant"
    ) -> List["CheckinEvent"]:
        if self.__finished:
            raise CheckinAlreadyFinished()

        event = ParticipantCheckedIn(command.participant_id)

        self.apply(event)

        if not all(x is True for x in self.__participants.values()):
            return [event]

        events = [event, AllParticipantsCheckedIn(), CheckinFinished()]

        self.apply_many(events[1:])

        return events

    def __checkin_started(self, event: "CheckinStarted"):
        self.__id = event.checkin_id
        self.__checked_in = event.checked_in
        self.__finished = False

        self.__version.increment()

    def __checkin_finished(self, event: "CheckinFinished"):
        self.__finished = True

        self.__version.increment()

    def __participant_checked_in(self, event: "ParticipantCheckedIn"):
        self.__checked_in[event.participant_id] = True

        self.__version.increment()

    def __all_participants_checked_in(self, event: "AllParticipantsCheckedIn"):
        self.__version.increment()


class CheckinId:
    def __init__(self):
        # Bad generation, better to use v7
        # see https://discuss.python.org/t/rfc-4122-9562-uuid-version-7-and-8-implementation/56725/3
        self.__value = uuid.uuid4()

    def __str__(self) -> str:
        return f"{self.__value}"

    def __eq__(self, other: "CheckinId"):
        return self.__value == other.__value

    def __ne__(self, other: "CheckinId"):
        return not (self == other)


CheckinEvent = Union[
    "CheckinStarted",
    "CheckinFinished",
    "ParticipantCheckedIn",
    "AllParticipantsCheckedIn",
]

CheckinCommand = Union["StartCheckin", "FinishCheckin", "CheckinParticipant"]

CheckinError = Union["CheckinAlreadyFinished"]

# Events


@dataclass
class CheckinStarted:
    checkin_id: CheckinId
    checked_in: Dict[StudentId, bool]


@dataclass
class CheckinFinished:
    pass


@dataclass
class ParticipantCheckedIn:
    participant_id: StudentId


@dataclass
class AllParticipantsCheckedIn:
    pass


# Commands


@dataclass
class StartCheckin:
    checkin_id: CheckinId
    checked_in: Dict[StudentId, bool]


@dataclass
class FinishCheckin:
    pass


@dataclass
class CheckinParticipant:
    participant_id: StudentId


# Errors
@dataclass
class CheckinAlreadyFinished(Exception):
    def __str__(self):
        return "Checkin already finished"
