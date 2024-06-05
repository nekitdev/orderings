from typing import Generic, TypeVar
from hypothesis import given, strategies
from typing_extensions import Self

from orderings.core import Compare, Ordering, compare, is_compare
from orderings.typing import Ordered

T = TypeVar("T", bound=Ordered)


class Wrap(Compare, Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value

    @property
    def value(self) -> T:
        return self._value

    def compare(self, other: Self) -> Ordering:
        return compare(self.value, other.value)


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
