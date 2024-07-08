"""Core enumerations."""

__all__ = (
    'SupportedCasing',
    )

from . import lib


class SupportedCasing(lib.enum.Enum):
    """Valid string casings."""

    camelCase = 'camelCase'
    snake_case = 'snake_case'
