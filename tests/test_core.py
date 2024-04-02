from typing import Generic, TypeVar

from typing_extensions import Self

from orderings.core import Compare, Ordering, is_compare
from orderings.typing import StrictOrdered

T = TypeVar("T", bound=StrictOrdered)


class Wrap(Compare, Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value

    @property
    def value(self) -> T:
        return self._value

    def compare(self, other: Self) -> Ordering:
        self_value = self.value
        other_value = other.value

        if self_value < other_value:
            return Ordering.LESS

        if self_value > other_value:
            return Ordering.GREATER

        return Ordering.EQUAL


def test_compare() -> None:
    assert Wrap(13) < Wrap(34)
    assert Wrap(69) > Wrap(42)

    assert Wrap(0) <= Wrap(0)
    assert Wrap(0) <= Wrap(1)

    assert Wrap(1) >= Wrap(1)
    assert Wrap(1) >= Wrap(0)

    assert Wrap(0) == Wrap(0)
    assert Wrap(1) != Wrap(0)


def test_is_compare() -> None:
    assert is_compare(Wrap(13))
    assert not is_compare(13)
