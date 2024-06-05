"""Ordering enumeration and protocols."""

__description__ = "Ordering enumeration and protocols."
__url__ = "https://github.com/nekitdev/orderings"

__title__ = "orderings"
__author__ = "nekitdev"
__license__ = "MIT"
__version__ = "1.6.0"

from orderings.core import Compare, Ordering, PartialCompare, compare, is_compare
from orderings.typing import (
    Greater,
    GreaterOrEqual,
    LenientOrdered,
    Less,
    LessOrEqual,
    Ordered,
    PartialGreater,
    PartialGreaterOrEqual,
    PartialLenientOrdered,
    PartialLess,
    PartialLessOrEqual,
    PartialOrdered,
    PartialStrictOrdered,
    StrictOrdered,
)

__all__ = (
    # core
    "Ordering",
    "PartialCompare",
    "Compare",
    "compare",
    "is_compare",
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
