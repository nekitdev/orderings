from typing import Protocol, runtime_checkable

from typing_aliases import required
from typing_extensions import Self

__all__ = (
    "Less",
    "Greater",
    "StrictOrdered",
    "LessOrEqual",
    "GreaterOrEqual",
    "LenientOrdered",
    "Ordered",
)


@runtime_checkable
class Less(Protocol):
    """Represents types that implement the *less* operation (`self < other`)
    where `other` is of type `Self`.
    """

    @required
    def __lt__(self, __other: Self) -> bool: ...


@runtime_checkable
class Greater(Protocol):
    """Represents types that implement the *greater* operation (`self > other`)
    where `other` is of type `Self`.
    """

    @required
    def __gt__(self, __other: Self) -> bool: ...


@runtime_checkable
class StrictOrdered(Less, Greater, Protocol):
    """Represents types that implement both [`Less`][orderings.typing.Less]
    and [`Greater`][orderings.typing.Greater] protocols.
    """


@runtime_checkable
class LessOrEqual(Protocol):
    """Represents types that implement the *less-or-equal* operation (`self <= other`)
    where `other` is of type `Self`.
    """

    @required
    def __le__(self, __other: Self) -> bool: ...


@runtime_checkable
class GreaterOrEqual(Protocol):
    """Represents types that implement the *greater-or-equal* operation (`self >= other`)
    where `other` is of type `Self`.
    """

    @required
    def __ge__(self, __other: Self) -> bool: ...


@runtime_checkable
class LenientOrdered(LessOrEqual, GreaterOrEqual, Protocol):
    """Represents types that implement both [`LessOrEqual`][orderings.typing.LessOrEqual]
    and [`GreaterOrEqual`][orderings.typing.GreaterOrEqual] protocols.
    """


@runtime_checkable
class Ordered(StrictOrdered, LenientOrdered, Protocol):
    """Represents types that implement both [`StrictOrdered`][orderings.typing.StrictOrdered]
    and [`LenientOrdered`][orderings.typing.LenientOrdered] protocols.
    """
