"""Core typing."""

__all__ = (
    'AnyDict',
    'AnyType',
    'ArgsType',
    'OptionalAnyDict',
    'PackageExceptionType',
    )

from . import lib

if lib.t.TYPE_CHECKING:  # pragma: no cover
    from . import exc  # noqa: F401

AnyDict = dict[str, lib.t.Any]
OptionalAnyDict = lib.t.Optional[dict[str, lib.t.Any]]

AnyType = lib.t.TypeVar('AnyType')
ArgsType = lib.TypeVarTuple('ArgsType')

PackageExceptionType = lib.t.TypeVar(
    'PackageExceptionType',
    bound='exc.BasePackageException',
    covariant=True,
    )
