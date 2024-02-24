"""Ordering enumeration and protocols."""

__description__ = "Ordering enumeration and protocols."
__url__ = "https://github.com/nekitdev/orderings"

__title__ = "orderings"
__author__ = "nekitdev"
__license__ = "MIT"
__version__ = "1.3.0"

from orderings.core import Compare, Ordering
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
    "Compare",
    "Ordering",
    "Less",
    "Greater",
    "StrictOrdered",
    "LessOrEqual",
    "GreaterOrEqual",
    "LenientOrdered",
    "Ordered",
)
