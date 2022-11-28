from typing import TypeVar

from orderings import Compare, Ordering

I = TypeVar("I", bound="Int")


class Int(Compare):
    def __init__(self, value: int) -> None:
        self._value = value

    @property
    def value(self) -> int:
        return self._value

    def compare(self: I, other: I) -> Ordering:
        self_value = self.value
        other_value = other.value

        if self_value < other_value:
            return Ordering.LESS

        if self_value > other_value:
            return Ordering.GREATER

        return Ordering.EQUAL


def test_compare() -> None:
    assert Int(13) < Int(34)
    assert Int(69) > Int(42)

    assert Int(0) <= Int(0)
    assert Int(0) <= Int(1)

    assert Int(1) >= Int(1)
    assert Int(1) >= Int(0)

    assert Int(0) == Int(0)
    assert Int(1) != Int(-1)
