from dataclasses import dataclass
from typing import List, Union
from domain.entity.report import Report
from domain.vo.version import Version


class ReportCollector:
    def __init__(self):
        self.__version = Version.min()
        self.__reports = {}

    def apply_many(self, events: List["ReportCollectorEvent"]):
        for event in events:
            match event:
                case _ if isinstance(event, ReportCollected):
                    self.__report_collected(event)
                case _ if isinstance(event, ReportEvaluated):
                    self.__report_evaluated(event)

    def apply(self, event: "ReportCollectorEvent"):
        self.apply_many([event])

    def handle_many(
        self, commands: List["ReportCollectorCommand"]
    ) -> List["ReportCollectorEvent"]:
        events = []

        for command in commands:
            match command:
                case _ if isinstance(command, CollectReport):
                    events.extend(self.__collect_report(command))
                case _ if isinstance(command, EvaluateReport):
                    events.extend(self.__evaluate_report(command))

        return events

    def handle(self, command: "ReportCollectorCommand") -> List["ReportCollectorEvent"]:
        return self.handle_many([command])

    def __collect_report(
        self, command: "CollectReport"
    ) -> List["ReportCollectorEvent"]:
        event = ReportCollected(command.report)

        self.apply(event)

        return [event]

    def __evaluate_report(self, _: "EvaluateReport") -> List["ReportCollectorEvent"]:
        event = ReportEvaluated()

        self.apply(event)

        return [event]

    def __report_collected(self, event: "ReportCollected"):
        self.__reports[event.report.id] = event.report

        self.__version.increment()

    def __report_evaluated(self, _: "ReportEvaluated"):
        self.__version.increment()


ReportCollectorEvent = Union["ReportCollected", "ReportEvaluated"]

ReportCollectorCommand = Union["CollectReport", "EvaluateReport"]

# HolyFatherError = Union[]

# Events


@dataclass
class ReportCollected:
    report: Report


@dataclass
class ReportEvaluated:
    pass


# Commands


@dataclass
class CollectReport:
    report: Report


@dataclass
class EvaluateReport:
    pass


# Errors
