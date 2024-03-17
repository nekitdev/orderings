"""Ordering enumeration and protocols."""

__description__ = "Ordering enumeration and protocols."
__url__ = "https://github.com/nekitdev/orderings"

__title__ = "orderings"
__author__ = "nekitdev"
__license__ = "MIT"
__version__ = "1.3.2"

from orderings.core import Compare, Ordering, is_compare
from orderings.typing import (
    Greater,
    GreaterOrEqual,
    LenientOrdered,
    Less,
    LessOrEqual,
    Ordered,
    StrictOrdered,
)

__all__ = (
    # core
    "Compare",
    "Ordering",
    "is_compare",
    # typing
    "Less",
    "Greater",
    "StrictOrdered",
    "LessOrEqual",
    "GreaterOrEqual",
    "LenientOrdered",
    "Ordered",
)
