class Version:
    """
    A value object represents an entity or an aggregate version.

    >>> version = Version.min()
    >>> print(version)
    1
    >>> version.increment()
    >>> print(version)
    2
    """

    __MIN_VERSION = 1
    """
    A constant for minimal possible version value.
    """

    def __init__(self, value: int):
        """
        Instantiate a new Version.

        Raises a ValueError exception if version value is invalid (less than minimal)

        >>> version = Version(0)
        Traceback (most recent call last):
        ...
        ValueError: version should be greater than 1, provided: 0
        """
        if value < Version.__MIN_VERSION:
            raise ValueError(
                f"version should be greater than {Version.__MIN_VERSION}, provided: {value}"
            )

        self.__value = value

    @classmethod
    def min(cls) -> "Version":
        """
        Instantiate a new version with minimal possible value.
        """
        return cls(cls.__MIN_VERSION)

    def increment(self) -> "Version":
        """
        Increment version.
        NOTE: no protection from overflow is used.
        """
        self.__value += 1

        return self

    def __str__(self) -> str:
        return f"{self.__value}"

    def __eq__(self, other: "Version"):
        return self.__value == other.__value

    def __ne__(self, other: "Version"):
        return not (self == other)

    def __gt__(self, other: "Version"):
        return self.__value > other.__value

    def __le__(self, other: "Version"):
        return not (self > other)

    def __lt__(self, other: "Version"):
        return self.__value < other.__value

    def __ge__(self, other: "Version"):
        return not (self < other)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
