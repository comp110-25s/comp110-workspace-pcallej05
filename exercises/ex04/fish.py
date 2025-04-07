"""File to define Fish class."""

__author__ = "730658315"


class Fish:
    age: int

    def __init__(self) -> None:
        self.age = 0
        return None

    def one_day(self) -> None:
        self.age += 1
        return None
