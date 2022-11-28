from abc import abstractmethod
from enum import Enum
from typing import Any, TypeVar

from typing_extensions import Protocol

from orderings.typing import Ordered, is_instance

__all__ = ("Compare", "Ordering")


class Ordering(Enum):
    """Represents ordering."""

    LESS = -1
    """The left item is *less* than the right item."""
    EQUAL = 0
    """The left item is *equal* to the right item."""
    GREATER = 1
    """The left item is *greater* than the right item."""

    def is_less(self) -> bool:
        """Checks if the ordering is [`LESS`][orderings.core.Ordering.LESS].

        Returns:
            Whether the ordering is [`LESS`][orderings.core.Ordering.LESS].
        """
        return self is type(self).LESS

    def is_equal(self) -> bool:
        """Checks if the ordering is [`EQUAL`][orderings.core.Ordering.EQUAL].

        Returns:
            Whether the ordering is [`EQUAL`][orderings.core.Ordering.EQUAL].
        """
        return self is type(self).EQUAL

    def is_greater(self) -> bool:
        """Checks if the ordering is [`GREATER`][orderings.core.Ordering.GREATER].

        Returns:
            Whether the ordering is [`GREATER`][orderings.core.Ordering.GREATER].
        """
        return self is type(self).GREATER

    def is_less_or_equal(self) -> bool:
        """Checks if the ordering is [`LESS`][orderings.core.Ordering.LESS] or
        [`EQUAL`][orderings.core.Ordering.EQUAL].
        This is equivalent to:

        ```python
        ordering.is_less() or ordering.is_equal()
        ```

        Returns:
            Whether the ordering is [`LESS`][orderings.core.Ordering.LESS]
                or [`EQUAL`][orderings.core.Ordering.EQUAL].
        """
        return self.is_less() or self.is_equal()

    def is_not_equal(self) -> bool:
        """Checks if the ordering is not [`EQUAL`][orderings.core.Ordering.EQUAL].
        This is equivalent to:

        ```python
        not ordering.is_equal()
        ```

        Returns:
            Whether the ordering is not [`EQUAL`][orderings.core.Ordering.EQUAL].
        """
        return not self.is_equal()

    def is_greater_or_equal(self) -> bool:
        """Checks if the ordering is [`GREATER`][orderings.core.Ordering.GREATER] or
        [`EQUAL`][orderings.core.Ordering.EQUAL].
        This is equivalent to:

        ```python
        ordering.is_greater() or ordering.is_equal()
        ```

        Returns:
            Whether the ordering is [`GREATER`][orderings.core.Ordering.GREATER]
                or [`EQUAL`][orderings.core.Ordering.EQUAL].
        """
        return self.is_greater() or self.is_equal()


C = TypeVar("C", bound="Compare")


class Compare(Ordered, Protocol):
    """Implements total ordering via delegation to the
    [`compare`][orderings.core.Compare.compare] method.
    """

    @abstractmethod
    def compare(self: C, other: C) -> Ordering:
        """Defines ordering via the [`Ordering`][orderings.core.Ordering] enumeration."""
        ...

    def __lt__(self: C, other: C) -> bool:
        return self.compare(other).is_less()

    def __gt__(self: C, other: C) -> bool:
        return self.compare(other).is_greater()

    def __le__(self: C, other: C) -> bool:
        return self.compare(other).is_less_or_equal()

    def __ge__(self: C, other: C) -> bool:
        return self.compare(other).is_greater_or_equal()

    def __eq__(self, other: Any) -> bool:
        return is_instance(other, type(self)) and self.compare(other).is_equal()

    def __ne__(self, other: Any) -> bool:
        return not is_instance(other, type(self)) or self.compare(other).is_not_equal()
