from enum import Enum
from typing import Any, Protocol, TypeVar, runtime_checkable

from typing_aliases import is_instance, is_same_or_sub_type, required
from typing_extensions import Self, TypeIs

from orderings.typing import Ordered, PartialOrdered

__all__ = ("Ordering", "PartialCompare", "Compare", "compare", "is_compare")


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


T = TypeVar("T", contravariant=True)


@runtime_checkable
class PartialCompare(PartialOrdered[T], Protocol[T]):
    """Implements partial ordering via delegation to the
    [`partial_compare`][orderings.core.PartialCompare.partial_compare] method.

    Note:
        Please note that this protocol does not implement equality methods.
    """

    @required
    def partial_compare(self, value: T) -> Ordering:
        """Defines partial ordering via the [`Ordering`][orderings.core.Ordering] enumeration."""
        ...

    def __lt__(self, value: T) -> bool:
        return self.partial_compare(value).is_less()

    def __gt__(self, value: T) -> bool:
        return self.partial_compare(value).is_greater()

    def __le__(self, value: T) -> bool:
        return self.partial_compare(value).is_less_or_equal()

    def __ge__(self, value: T) -> bool:
        return self.partial_compare(value).is_greater_or_equal()


@runtime_checkable
class Compare(Ordered, Protocol):
    """Implements total ordering via delegation to the
    [`compare`][orderings.core.Compare.compare] method.
    """

    @required
    def compare(self, other: Self) -> Ordering:
        """Defines ordering via the [`Ordering`][orderings.core.Ordering] enumeration."""
        ...

    def __lt__(self, other: Self) -> bool:
        return self.compare(other).is_less()

    def __gt__(self, other: Self) -> bool:
        return self.compare(other).is_greater()

    def __le__(self, other: Self) -> bool:
        return self.compare(other).is_less_or_equal()

    def __ge__(self, other: Self) -> bool:
        return self.compare(other).is_greater_or_equal()

    def __eq__(self, other: Any) -> bool:
        return is_same_or_sub_type(other, self) and self.compare(other).is_equal()

    def __ne__(self, other: Any) -> bool:
        return not is_same_or_sub_type(other, self) or self.compare(other).is_not_equal()


def is_compare(item: Any) -> TypeIs[Compare]:
    """Checks if the `item` implements the [`Compare`][orderings.core.Compare] protocol.

    Arguments:
        item: The item to check.

    Returns:
        Whether the `item` implements the [`Compare`][orderings.core.Compare] protocol.
    """
    return is_instance(item, Compare)


def compare(left: PartialOrdered[T], right: T) -> Ordering:
    """Compares `left` and `right`, returning [`Ordering`][orderings.core.Ordering].

    Arguments:
        left: The left value.
        right: The right value.

    Returns:
        The result.
    """
    if left < right:
        return Ordering.LESS

    if left > right:
        return Ordering.GREATER

    return Ordering.EQUAL
