"""Strings typing."""

from .. import typ

__all__ = (
    'camelCase',
    'snake_case',
    'string',
    'Casing',
    'CasingType',
    *typ.__all__
    )

from .. typ import *

from . import lib

camelCase = lib.t.NewType('camelCase', str)
snake_case = lib.t.NewType('snake_case', str)

Casing = (
    camelCase
    | snake_case
    )

CasingType = lib.t.TypeVar('CasingType', bound=Casing)


class string(str, lib.t.Generic[CasingType]):
    """Protocol for a cased `str`."""
