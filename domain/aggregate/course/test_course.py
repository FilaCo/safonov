from unittest import TestCase

from domain.aggregate.course import (
    Course,
    StartCourse,
    CourseStarted,
    FinishCourse,
    CourseFinished,
)


class TestCourse(TestCase):
    def test__handle__StartCourseCommand__CourseStartedEventReturned(self):
        # arrange
        course = Course()
        command = StartCourse(None, {}, {})
        expected = [CourseStarted(None, {}, {})]

        # act
        actual = course.handle(command)

        # assert
        self.assertEqual(expected, actual)

    def test__handle__FinishCourseCommand__CourseFinishedEventReturned(self):
        # arrange
        course = Course()
        command = FinishCourse(None)
        expected = [CourseFinished(None)]

        # act
        actual = course.handle(command)

        # assert
        self.assertEqual(expected, actual)

    def test__handle__RegisterParticipantCommand__ParticipantRegisteredEventReturned(
        self,
    ):
        # arrange
        course = Course()
        command = FinishCourse(None)
        expected = [CourseFinished(None)]

        # act
        actual = course.handle(command)

        # assert
        self.assertEqual(expected, actual)
