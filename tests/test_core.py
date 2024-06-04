from typing import Generic, TypeVar
from hypothesis import given, strategies
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


@given(strategies.integers(), strategies.integers())
def test_compare(left: int, right: int) -> None:
    assert (left < right) is (Wrap(left) < Wrap(right))
    assert (left > right) is (Wrap(left) > Wrap(right))
    assert (left <= right) is (Wrap(left) <= Wrap(right))
    assert (left >= right) is (Wrap(left) >= Wrap(right))
    assert (left == right) is (Wrap(left) == Wrap(right))
    assert (left != right) is (Wrap(left) != Wrap(right))


def test_is_compare() -> None:
    assert is_compare(Wrap(13))
    assert not is_compare(13)
