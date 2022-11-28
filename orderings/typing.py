from abc import abstractmethod
from builtins import isinstance as is_instance
from typing import TypeVar

from typing_extensions import Protocol

__all__ = (
    "Less",
    "Greater",
    "StrictOrdered",
    "LessOrEqual",
    "GreaterOrEqual",
    "LenientOrdered",
    "Ordered",
    "is_instance",
)

L = TypeVar("L", bound="Less")


class Less(Protocol):
    """Represents types that implement the *less* operation (`self < other`)
    where `other` is of type `Self`.
    """

    @abstractmethod
    def __lt__(self: L, other: L) -> bool:
        ...


G = TypeVar("G", bound="Greater")


class Greater(Protocol):
    """Represents types that implement the *greater* operation (`self > other`)
    where `other` is of type `Self`.
    """

    @abstractmethod
    def __gt__(self: G, other: G) -> bool:
        ...


class StrictOrdered(Less, Greater, Protocol):
    """Represents types that implement both [`Less`][orderings.typing.Less]
    and [`Greater`][orderings.typing.Greater] protocols.
    """


LE = TypeVar("LE", bound="LessOrEqual")


class LessOrEqual(Protocol):
    """Represents types that implement the *less-or-equal* operation (`self <= other`)
    where `other` is of type `Self`.
    """

    @abstractmethod
    def __le__(self: LE, other: LE) -> bool:
        ...


GE = TypeVar("GE", bound="GreaterOrEqual")


class GreaterOrEqual(Protocol):
    """Represents types that implement the *greater-or-equal* operation (`self >= other`)
    where `other` is of type `Self`.
    """

    @abstractmethod
    def __ge__(self: GE, other: GE) -> bool:
        ...


class LenientOrdered(LessOrEqual, GreaterOrEqual, Protocol):
    """Represents types that implement both [`LessOrEqual`][orderings.typing.LessOrEqual]
    and [`GreaterOrEqual`][orderings.typing.GreaterOrEqual] protocols.
    """


class Ordered(StrictOrdered, LenientOrdered, Protocol):
    """Represents types that implement both [`StrictOrdered`][orderings.typing.StrictOrdered]
    and [`LenientOrdered`][orderings.typing.LenientOrdered] protocols.
    """
