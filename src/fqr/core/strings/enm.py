"""Strings enumerations."""

__all__ = (
    'SupportedCasing',
    )

from . import lib
from . import typ


class SupportedCasing(lib.enum.Enum):
    """Valid string casings."""

    camelCase  = typ.camelCase
    snake_case = typ.snake_case
