"""Core typing."""

__all__ = (
    'camelCase',
    'snake_case',
    'string',
    'AnyType',
    'ArgsType',
    'Casing',
    'CasingType',
    'PackageExceptionType',
    )

from . import lib

if lib.t.TYPE_CHECKING:  # pragma: no cover
    from . import exc  # noqa: F401

camelCase = lib.t.NewType('camelCase', str)
snake_case = lib.t.NewType('snake_case', str)

Casing = (
    camelCase
    | snake_case
    )

ArgsType = lib.TypeVarTuple('ArgsType')

PackageExceptionType = lib.t.TypeVar(
    'PackageExceptionType',
    bound='exc.BasePackageException',
    covariant=True,
    )

AnyType = lib.t.TypeVar('AnyType')
CasingType = lib.t.TypeVar('CasingType', bound=Casing)


class string(str, lib.t.Generic[CasingType]):
    """Protocol for a cased `str`."""
