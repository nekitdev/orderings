from typing import Protocol, TypeVar, runtime_checkable

from typing_aliases import required
from typing_extensions import Self

__all__ = (
    # partial
    "PartialLess",
    "PartialGreater",
    "PartialStrictOrdered",
    "PartialLessOrEqual",
    "PartialGreaterOrEqual",
    "PartialLenientOrdered",
    "PartialOrdered",
    # total
    "Less",
    "Greater",
    "StrictOrdered",
    "LessOrEqual",
    "GreaterOrEqual",
    "LenientOrdered",
    "Ordered",
)

T = TypeVar("T", contravariant=True)


@runtime_checkable
class PartialLess(Protocol[T]):
    """Represents types that implement the *less* operation (`self < other`)
    where `other` is of type `T`.
    """

    @required
    def __lt__(self, __other: T) -> bool: ...


@runtime_checkable
class Less(Protocol):
    """Represents types that implement the *less* operation (`self < other`)
    where `other` is of type `Self`.
    """

    @required
    def __lt__(self, __other: Self) -> bool: ...


@runtime_checkable
class PartialGreater(Protocol[T]):
    """Represents types that implement the *greater* operation (`self > other`)
    where `other` is of type `T`.
    """

    @required
    def __gt__(self, __other: T) -> bool: ...


@runtime_checkable
class Greater(Protocol):
    """Represents types that implement the *greater* operation (`self > other`)
    where `other` is of type `Self`.
    """

    @required
    def __gt__(self, __other: Self) -> bool: ...


@runtime_checkable
class PartialStrictOrdered(PartialLess[T], PartialGreater[T], Protocol[T]):
    """Represents types that implement both [`PartialLess[T]`][orderings.typing.PartialLess]
    and [`PartialGreater[T]`][orderings.typing.PartialGreater] protocols.
    """


@runtime_checkable
class StrictOrdered(Less, Greater, Protocol):
    """Represents types that implement both [`Less`][orderings.typing.Less]
    and [`Greater`][orderings.typing.Greater] protocols.
    """


@runtime_checkable
class PartialLessOrEqual(Protocol[T]):
    """Represents types that implement the *less-or-equal* operation (`self <= other`)
    where `other` is of type `T`.
    """

    @required
    def __le__(self, __other: T) -> bool: ...


@runtime_checkable
class LessOrEqual(Protocol):
    """Represents types that implement the *less-or-equal* operation (`self <= other`)
    where `other` is of type `Self`.
    """

    @required
    def __le__(self, __other: Self) -> bool: ...


@runtime_checkable
class PartialGreaterOrEqual(Protocol[T]):
    """Represents types that implement the *greater-or-equal* operation (`self >= other`)
    where `other` is of type `T`.
    """

    @required
    def __ge__(self, __other: T) -> bool: ...


@runtime_checkable
class GreaterOrEqual(Protocol):
    """Represents types that implement the *greater-or-equal* operation (`self >= other`)
    where `other` is of type `Self`.
    """

    @required
    def __ge__(self, __other: Self) -> bool: ...


@runtime_checkable
class PartialLenientOrdered(PartialLessOrEqual[T], PartialGreaterOrEqual[T], Protocol[T]):
    """Represents types that implement both
    [`PartialLessOrEqual[T]`][orderings.typing.PartialLessOrEqual] and
    [`PartialGreaterOrEqual[T]`][orderings.typing.PartialGreaterOrEqual] protocols.
    """


@runtime_checkable
class LenientOrdered(LessOrEqual, GreaterOrEqual, Protocol):
    """Represents types that implement both [`LessOrEqual`][orderings.typing.LessOrEqual]
    and [`GreaterOrEqual`][orderings.typing.GreaterOrEqual] protocols.
    """


@runtime_checkable
class PartialOrdered(PartialStrictOrdered[T], PartialLenientOrdered[T], Protocol[T]):
    """Represents types that implement both
    [`PartialStrictOrdered[T]`][orderings.typing.PartialStrictOrdered] and
    [`PartialLenientOrdered[T]`][orderings.typing.PartialLenientOrdered] protocols.
    """


@runtime_checkable
class Ordered(StrictOrdered, LenientOrdered, Protocol):
    """Represents types that implement both [`StrictOrdered`][orderings.typing.StrictOrdered]
    and [`LenientOrdered`][orderings.typing.LenientOrdered] protocols.
    """
