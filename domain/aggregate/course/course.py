from dataclasses import dataclass
from typing import Dict, List, Union
import uuid
from domain.entity.student import Student, StudentId
from domain.entity.teacher import Teacher, TeacherId
from domain.vo.version import Version


class Course:
    def __init__(self):
        self.__id = None
        self.__version = Version.min()

        self.__teachers = None
        self.__participants = None
        self.__finished = None

    def apply_many(self, events: List["CourseEvent"]):
        for event in events:
            match event:
                case _ if isinstance(event, CourseStarted):
                    self.__course_started(event)
                case _ if isinstance(event, CourseFinished):
                    self.__course_finished(event)
                case _ if isinstance(event, ParticipantRegistered):
                    self.__participant_registered(event)

    def apply(self, event: "CourseEvent"):
        self.apply_many([event])

    def handle_many(self, commands: List["CourseCommand"]) -> List["CourseEvent"]:
        events = []

        for command in commands:
            match command:
                case _ if isinstance(command, StartCourse):
                    events.extend(self.__start_course(command))
                case _ if isinstance(command, FinishCourse):
                    events.extend(self.__finish_course(command))
                case _ if isinstance(command, RegisterParticipant):
                    events.extend(self.__register_participant(command))

        return events

    def handle(self, command: "CourseCommand") -> List["CourseEvent"]:
        return self.handle_many([command])

    def __start_course(self, command: "StartCourse") -> List["CourseEvent"]:
        event = CourseStarted(
            command.course_id,
            command.teachers,
            command.participants,
        )

        self.apply(event)

        return [event]

    def __finish_course(self, command: "FinishCourse") -> List["CourseEvent"]:
        event = CourseFinished(course_id=command.course_id)

        self.apply(event)

        return [event]

    def __register_participant(
        self, command: "RegisterParticipant"
    ) -> List["CourseEvent"]:
        if self.__finished:
            raise CourseAlreadyFinished()

        if command.participant.id in self.__participants:
            raise ParticipantAlreadyRegistered()

        event = ParticipantRegistered(command.participant)

        self.apply(event)

        return [event]

    def __course_started(self, event: "CourseStarted"):
        self.__id = event.course_id
        self.__teachers = event.teachers
        self.__participants = event.participants
        self.__finished = False

        self.__version.increment()

    def __course_finished(self, event: "CourseFinished"):
        self.__finished = True

        self.__version.increment()

    def __participant_registered(self, event: "ParticipantRegistered"):
        self.__participants[event.participant.id] = event.participant

        self.__version.increment()


class CourseId:
    def __init__(self):
        # Bad generation, better to use v7
        # see https://discuss.python.org/t/rfc-4122-9562-uuid-version-7-and-8-implementation/56725/3
        self.__value = uuid.uuid4()

    def __str__(self) -> str:
        return f"{self.__value}"

    def __eq__(self, other: "CourseId"):
        return self.__value == other.__value

    def __ne__(self, other: "CourseId"):
        return not (self == other)


CourseEvent = Union[
    "CourseStarted",
    "CourseFinished",
    "ParticipantRegistered",
]

CourseCommand = Union[
    "StartCourse",
    "FinishCourse",
    "RegisterParticipant",
]

CourseError = Union["CourseAlreadyFinished", "ParticipantAlreadyRegistered"]

# Events


@dataclass
class CourseStarted:
    course_id: CourseId
    teachers: Dict[TeacherId, Teacher]
    participants: Dict[StudentId, Student]


@dataclass
class CourseFinished:
    course_id: CourseId


@dataclass
class ParticipantRegistered:
    participant: Student


# Commands


@dataclass
class StartCourse:
    course_id: CourseId
    teachers: Dict[TeacherId, Teacher]
    participants: Dict[StudentId, Student]


@dataclass
class FinishCourse:
    course_id: CourseId


@dataclass
class RegisterParticipant:
    participant: Student


# Errors
@dataclass
class CourseAlreadyFinished(Exception):
    def __str__(self):
        return "Course already finished"


@dataclass
class ParticipantAlreadyRegistered(Exception):
    def __str__(self):
        return "Participant already registered"
