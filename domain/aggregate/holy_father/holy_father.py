from dataclasses import dataclass
from typing import List, Union

from domain.entity.feedback import Feedback
from domain.vo.version import Version


class HolyFather:
    def __init__(self):
        self.__version = Version.min()
        self.__feedbacks = {}

    def apply_many(self, events: List["HolyFatherEvent"]):
        for event in events:
            match event:
                case _ if isinstance(event, FeedbackCollected):
                    self.__apply_feedback_collected(event)

    def apply(self, event: "HolyFatherEvent"):
        self.apply_many([event])

    def handle_many(
        self, commands: List["HolyFatherCommand"]
    ) -> List["HolyFatherEvent"]:
        events = []

        for command in commands:
            match command:
                case _ if isinstance(command, CollectFeedback):
                    events.extend(self.__collect_feedback(command))

        return events

    def handle(self, command: "HolyFatherCommand") -> List["HolyFatherEvent"]:
        return self.handle_many([command])

    def __collect_feedback(self, command: "CollectFeedback") -> List["HolyFatherEvent"]:
        event = FeedbackCollected(command.feedback)

        self.__apply_feedback_collected(event)

        return [event]

    def __apply_feedback_collected(self, event: "FeedbackCollected"):
        self.__feedbacks[event.feedback.id] = event.feedback

        self.__version.increment()


HolyFatherEvent = Union["FeedbackCollected"]

HolyFatherCommand = Union["CollectFeedback"]

# HolyFatherError = Union[]

# Events


@dataclass
class FeedbackCollected:
    feedback: Feedback


# Commands


@dataclass
class CollectFeedback:
    feedback: Feedback


# Errors
