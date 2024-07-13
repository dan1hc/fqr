"""Typing objects."""

from . import lib
from . import typ

__all__ = (
    'SupportsParams',
    )


class SupportsParams(lib.t.Protocol, lib.t.Generic[lib.Unpack[typ.ArgsType]]):
    """Protocol for a generic with any number of parameters."""

    @property
    def __args__(self) -> tuple[lib.Unpack[typ.ArgsType]]: ...

    def __hash__(self) -> int: ...
