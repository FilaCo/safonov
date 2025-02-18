from unittest import TestCase

from domain.vo.version import Version


class TestVersion(TestCase):
    def test__init__InitialValueIsInvalid__ValueErrorRaised(self):
        # arrange
        raw_version = -3
        expected_str = f"version should be greater than 0, provided: {raw_version}"

        # act
        with self.assertRaises(ValueError) as actual:
            _ = Version(raw_version)

        # assert
        self.assertEqual(expected_str, str(actual.exception))

    def test__init__InitialValueisValid_VersionReturned(self):
        # arrange
        raw_version = 10
        expected = Version(10)

        # act
        actual = Version(raw_version)

        # assert
        self.assertEqual(expected, actual)

    def test__increment__IncrementedVersionReturned(self):
        # arrange
        version = Version(10)
        expected = Version(11)

        # act
        actual = version.increment()

        # assert
        self.assertEqual(expected, actual)

    def test__min__MinVersionReturned(self):
        # arrange
        expected = Version(0)

        # act
        actual = Version.min()

        # assert
        self.assertEqual(expected, actual)
