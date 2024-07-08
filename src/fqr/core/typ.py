"""Core typing."""

__all__ = (
    'camelCaseString',
    'snake_case_string',
    'ArgsType',
    'Casing',
    'PackageExceptionType',
    )

from . import lib

if lib.t.TYPE_CHECKING:  # pragma: no cover
    from . import exc  # noqa: F401

camelCaseString = lib.t.NewType('camelCaseString', str)
snake_case_string = lib.t.NewType('snake_case_string', str)

Casing = (
    lib.t.Literal['camelCase']
    | lib.t.Literal['snake_case']
    )

ArgsType = lib.TypeVarTuple('ArgsType')

PackageExceptionType = lib.t.TypeVar(
    'PackageExceptionType',
    bound='exc.BasePackageException',
    covariant=True,
    )
