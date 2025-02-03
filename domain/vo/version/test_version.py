from unittest import TestCase

from domain.vo.version import Version


class TestVersion(TestCase):
    def test_init_initialValueIsInvalid_ValueErrorRaised(self):
        # arrange
        raw_version = -3
        expected_str = f"version should be greater than 1, provided: {raw_version}"

        # act
        with self.assertRaises(ValueError) as actual:
            _ = Version(raw_version)

        # assert
        self.assertEqual(expected_str, str(actual.exception))

    def test_init_initialValueisValid_VersionReturned(self):
        # arrange
        raw_version = 10
        expected = Version(10)

        # act
        actual = Version(raw_version)

        # assert
        self.assertEqual(expected, actual)

    def test_increment_IncrementedVersionReturned(self):
        # arrange
        version = Version(10)
        expected = Version(11)

        # act
        actual = version.increment()

        # assert
        self.assertEqual(expected, actual)

    def test_min_MinVersionReturned(self):
        # arrange
        expected = Version(1)

        # act
        actual = Version.min()

        # assert
        self.assertEqual(expected, actual)
