"""Typing objects."""

__all__ = (
    'string',
    'ArrayProto',
    'FieldPattern',
    'MappingProto',
    'MetaLike',
    'ObjectLike',
    'SupportsAnnotations',
    'SupportsParams',
    'VariadicArrayProto',
    'WrapperPattern',
    )

from . import cfg
from . import lib

if lib.t.TYPE_CHECKING:  # pragma: no cover
    from . import typ  # noqa: F401


class Constants(cfg.Constants):
    """Constant values specific to this file."""


# Note: these need to be here to avoid circular import.
# They are however imported by adjacent typ and injected
# to typ's __all__ for consistency.
AnyType = lib.t.TypeVar('AnyType')
AnyOtherType = lib.t.TypeVar('AnyOtherType')
AnyTypeCo = lib.t.TypeVar('AnyTypeCo', covariant=True)
AnyOtherTypeCo = lib.t.TypeVar('AnyOtherTypeCo', covariant=True)
ArgsType = lib.TypeVarTuple('ArgsType')
StringType = lib.t.TypeVar('StringType', bound='typ.StringFormat')


class ArrayProto(lib.t.Protocol, lib.t.Collection[AnyTypeCo]):
    """Protocol for a generic, single-parameter array."""

    def __init__(
        self,
        iterable: lib.t.Iterable[AnyTypeCo],
        /
        ) -> None: ...

    def __iter__(self) -> lib.t.Iterator[AnyTypeCo]: ...


class VariadicArrayProto(
    ArrayProto[tuple[lib.Unpack[ArgsType]]],
    lib.t.Protocol
    ):
    """Protocol for a generic, any-parameter array."""

    def __hash__(self) -> int: ...


class MappingProto(
    lib.t.Protocol,
    lib.t.Generic[AnyTypeCo, AnyOtherTypeCo]
    ):
    """Protocol for a generic, double-parameter mapping."""

    def __init__(self, *args: lib.t.Any, **kwargs: lib.t.Any) -> None: ...

    def __iter__(self) -> lib.t.Iterator[AnyTypeCo]: ...

    def __getitem__(
        self,
        __name: str,
        __default: lib.t.Optional[AnyType] = None
        ) -> AnyTypeCo | AnyType: ...

    def items(self) -> lib.t.ItemsView[AnyTypeCo, AnyOtherTypeCo]: ...

    def keys(self) -> lib.t.KeysView[AnyTypeCo]: ...

    def values(self) -> lib.t.ValuesView[AnyOtherTypeCo]: ...


class SupportsAnnotations(lib.t.Protocol):
    """
    Protocol for a typed object.

    ---

    Typed objects include `dataclass`, `TypedDict`, `pydantic.Model`, \
    and both `fqr.Field` and `fqr.Object` amongst others.

    """

    __annotations__: dict[str, lib.t.Any]
    __bases__: tuple[type, ...]

    def __init__(self, *args: lib.t.Any, **kwargs: lib.t.Any) -> None: ...


class SupportsParams(lib.t.Protocol, lib.t.Generic[lib.Unpack[ArgsType]]):
    """Protocol for a generic with any number of parameters."""

    if lib.sys.version_info >= (3, 9):
        def __class_getitem__(
            cls,
            item: tuple[lib.Unpack[ArgsType]],
            /
            ) -> lib.types.GenericAlias: ...

    __args__: tuple[lib.Unpack[ArgsType]]

    def __hash__(self) -> int: ...


class MetaLike(lib.t.Protocol):
    """Meta protocol."""

    __annotations__: 'typ.SnakeDict'
    __dataclass_fields__: 'lib.t.ClassVar[typ.DataClassFields]'


class ObjectLike(lib.t.Protocol):
    """Object protocol."""

    __annotations__: 'typ.SnakeDict'
    __bases__: tuple[type, ...]
    __dataclass_fields__: 'lib.t.ClassVar[typ.DataClassFields]'

    def __contains__(self, __key: lib.t.Any, /) -> bool: ...

    def __getitem__(self, __key: lib.t.Any, /) -> lib.t.Any: ...

    def __setitem__(
        self,
        __key: str,
        __value: lib.t.Any
        ) -> lib.t.Optional[lib.Never]: ...

    def __ior__(self, other: 'ObjectLike', /) -> lib.Self: ...

    def get(
        self,
        __key: 'typ.AnyString',
        __default: AnyType = None
        ) -> lib.t.Any | AnyType: ...

    def items(
        self
        ) -> 'lib.t.ItemsView[typ.string[typ.snake_case], lib.t.Any]': ...

    @classmethod
    def keys(cls) -> 'lib.t.KeysView[typ.string[typ.snake_case]]': ...

    def pop(
        self,
        __key: str,
        /,
        __default: AnyType = Constants.UNDEFINED
        ) -> AnyType | lib.t.Any | lib.Never: ...

    def setdefault(
        self,
        __key: str,
        __value: lib.t.Any
        ) -> lib.t.Optional[lib.Never]: ...

    def update(self, other: 'ObjectLike', /) -> None: ...

    def values(self) -> lib.t.ValuesView[lib.t.Any]: ...

    @lib.t.overload
    def to_dict(
        self,
        camel_case: lib.t.Literal[False] = False,
        include_null: bool = True
        ) -> 'typ.SnakeDict': ...
    @lib.t.overload
    def to_dict(
        self,
        camel_case: lib.t.Literal[True],
        include_null: bool
        ) -> 'typ.CamelDict': ...
    @lib.t.overload
    def to_dict(
        self,
        camel_case: bool,
        include_null: bool
        ) -> 'typ.SnakeDict | typ.CamelDict': ...
    def to_dict(
        self,
        camel_case: bool = False,
        include_null: bool = True
        ) -> 'typ.SnakeDict | typ.CamelDict': ...


FieldPattern = lib.re.compile(
    r'(fqr(\.[a-zA-Z]{1,32}){0,32}\.)?Field'
    r'\[((\[)?[\.\|\,a-zA-Z0-9_ ]{1,64}(\])?){1,64}\]'
    )

WrapperPattern = lib.re.compile(
    r'([a-zA-Z]{1,64}\.?)?(Annotated|ClassVar|Final|InitVar)'
    r'\[((\[)?[\.\|\,a-zA-Z0-9_ ]{1,64}(\])?){1,64}\]'
    )


class string(str, lib.t.Generic[StringType]):
    """Generic `str` protocol."""

    @lib.t.overload
    def __new__(cls, object: object = ...) -> lib.Self: ...
    @lib.t.overload
    def __new__(
        cls,
        object: 'lib.builtins.ReadableBuffer',
        encoding: str = ...,
        errors: str = ...
        ) -> lib.Self: ...
    @lib.t.overload
    def capitalize(self: lib.t.LiteralString) -> lib.t.LiteralString: ...
    @lib.t.overload
    def capitalize(self) -> 'lib.t.Self[StringType] | string[lib.t.Any]': ...
    @lib.t.overload
    def casefold(self: lib.t.LiteralString) -> lib.t.LiteralString: ...
    @lib.t.overload
    def casefold(self) -> 'lib.t.Self[StringType] | string[lib.t.Any]': ...
    @lib.t.overload
    def center(
        self: lib.t.LiteralString,
        width: lib.t.SupportsIndex,
        fillchar: lib.t.LiteralString = " ",
        /
        ) -> lib.t.LiteralString: ...
    @lib.t.overload
    def center(
        self,
        width: lib.t.SupportsIndex,
        fillchar: str = " ",
        /
        ) -> 'lib.t.Self[StringType] | string[lib.t.Any]': ...
    @lib.t.overload
    def expandtabs(
        self: lib.t.LiteralString,
        tabsize: lib.t.SupportsIndex = 8
        ) -> lib.t.LiteralString: ...
    @lib.t.overload
    def expandtabs(
        self,
        tabsize: lib.t.SupportsIndex = 8
        ) -> 'lib.t.Self[StringType] | string[lib.t.Any]': ...
    @lib.t.overload
    def format(
        self: lib.t.LiteralString,
        *args: lib.t.LiteralString,
        **kwargs: lib.t.LiteralString
        ) -> lib.t.LiteralString: ...
    @lib.t.overload
    def format(
        self,
        *args: object,
        **kwargs: object
        ) -> 'lib.t.Self[StringType] | string[lib.t.Any]': ...
    def format_map(
        self,
        mapping: 'lib.builtins._FormatMapMapping',
        /
        ) -> 'lib.t.Self[StringType] | string[lib.t.Any]': ...
    @lib.t.overload
    def join(
        self: lib.t.LiteralString,
        iterable: lib.t.Iterable[lib.t.LiteralString],
        /
        ) -> lib.t.LiteralString: ...
    @lib.t.overload
    def join(
        self,
        iterable: 'lib.t.Iterable[string[StringType]]',
        /
        ) -> 'string[StringType]': ...
    @lib.t.overload
    def join(
        self,
        iterable: str,
        /
        ) -> 'string[lib.t.Any]': ...
    @lib.t.overload
    def ljust(
        self: lib.t.LiteralString,
        width: lib.t.SupportsIndex,
        fillchar: lib.t.LiteralString = " ",
        /
        ) -> lib.t.LiteralString: ...
    @lib.t.overload
    def ljust(
        self,
        width: lib.t.SupportsIndex,
        fillchar: str = " ",
        /
        ) -> 'lib.t.Self[StringType] | string[lib.t.Any]': ...
    @lib.t.overload
    def lower(self: lib.t.LiteralString) -> lib.t.LiteralString: ...
    @lib.t.overload
    def lower(self) -> 'lib.t.Self[StringType] | string[lib.t.Any]': ...
    @lib.t.overload
    def lstrip(
        self: lib.t.LiteralString,
        chars: lib.t.LiteralString | None = None,
        /
        ) -> lib.t.LiteralString: ...
    @lib.t.overload
    def lstrip(
        self,
        chars: str | None = None,
        /
        ) -> 'lib.t.Self[StringType] | string[lib.t.Any]': ...
    @lib.t.overload
    def partition(
        self: lib.t.LiteralString,
        sep: lib.t.LiteralString,
        /
        ) -> tuple[
            lib.t.LiteralString,
            lib.t.LiteralString,
            lib.t.LiteralString
            ]: ...
    @lib.t.overload
    def partition(self, sep: str, /) -> tuple[
        'lib.t.Self[StringType] | string[lib.t.Any]', 
        'lib.t.Self[StringType] | string[lib.t.Any]', 
        'lib.t.Self[StringType] | string[lib.t.Any]'
        ]: ...
    if lib.sys.version_info >= (3, 13):  # pragma: no cover
        @lib.t.overload
        def replace(
            self: lib.t.LiteralString,
            old: lib.t.LiteralString,
            new: lib.t.LiteralString,
            /,
            count: lib.t.SupportsIndex = -1
        ) -> lib.t.LiteralString: ...
        @lib.t.overload
        def replace(
            self,
            old: str,
            new: str,
            /,
            count: lib.t.SupportsIndex = -1
            ) -> 'lib.t.Self[StringType] | string[lib.t.Any]': ...
    else:  # pragma: no cover
        @lib.t.overload
        def replace(
            self: lib.t.LiteralString,
            old: lib.t.LiteralString,
            new: lib.t.LiteralString,
            count: lib.t.SupportsIndex = -1,
            /
        ) -> lib.t.LiteralString: ...
        @lib.t.overload
        def replace(
            self,
            old: str,
            new: str,
            count: lib.t.SupportsIndex = -1,
            /
            ) -> 'lib.t.Self[StringType] | string[lib.t.Any]': ...
    if lib.sys.version_info >= (3, 9):
        @lib.t.overload
        def removeprefix(
            self: lib.t.LiteralString,
            prefix: lib.t.LiteralString,
            /
            ) -> lib.t.LiteralString: ...
        @lib.t.overload
        def removeprefix(
            self,
            prefix: str,
            /
            ) -> 'lib.t.Self[StringType] | string[lib.t.Any]': ...
        @lib.t.overload
        def removesuffix(
            self: lib.t.LiteralString,
            suffix: lib.t.LiteralString,
            /
            ) -> lib.t.LiteralString: ...
        @lib.t.overload
        def removesuffix(
            self,
            suffix: str,
            /
            ) -> 'lib.t.Self[StringType] | string[lib.t.Any]': ...

    @lib.t.overload
    def rjust(
        self: lib.t.LiteralString,
        width: lib.t.SupportsIndex,
        fillchar: lib.t.LiteralString = " ",
        /
        ) -> lib.t.LiteralString: ...
    @lib.t.overload
    def rjust(
        self,
        width: lib.t.SupportsIndex,
        fillchar: str = " ",
        /
        ) -> 'lib.t.Self[StringType] | string[lib.t.Any]': ...
    @lib.t.overload
    def rpartition(
        self: lib.t.LiteralString,
        sep: lib.t.LiteralString,
        /
        ) -> tuple[
            lib.t.LiteralString,
            lib.t.LiteralString,
            lib.t.LiteralString
            ]: ...
    @lib.t.overload
    def rpartition(
        self,
        sep: str,
        /
        ) -> tuple[
            'lib.t.Self[StringType] | string[lib.t.Any]', 
            'lib.t.Self[StringType] | string[lib.t.Any]', 
            'lib.t.Self[StringType] | string[lib.t.Any]'
            ]: ...
    @lib.t.overload
    def rsplit(
        self: lib.t.LiteralString,
        sep: lib.t.LiteralString | None = None,
        maxsplit: lib.t.SupportsIndex = -1
        ) -> list[lib.t.LiteralString]: ...
    @lib.t.overload
    def rsplit(
        self,
        sep: str | None = None,
        maxsplit: lib.t.SupportsIndex = -1
        ) -> 'list[lib.t.Self[StringType] | string[lib.t.Any]]': ...
    @lib.t.overload
    def rstrip(
        self: lib.t.LiteralString,
        chars: lib.t.LiteralString | None = None,
        /
        ) -> lib.t.LiteralString: ...
    @lib.t.overload
    def rstrip(
        self,
        chars: str | None = None,
        /
        ) -> 'lib.t.Self[StringType] | string[lib.t.Any]': ...
    @lib.t.overload
    def split(
        self: lib.t.LiteralString,
        sep: lib.t.LiteralString | None = None,
        maxsplit: lib.t.SupportsIndex = -1
        ) -> list[lib.t.LiteralString]: ...
    @lib.t.overload
    def split(
        self,
        sep: str | None = None,
        maxsplit: lib.t.SupportsIndex = -1
        ) -> 'list[lib.t.Self[StringType] | string[lib.t.Any]]': ...
    @lib.t.overload
    def splitlines(
        self: lib.t.LiteralString,
        keepends: bool = False
        ) -> list[lib.t.LiteralString]: ...
    @lib.t.overload
    def splitlines(
        self,
        keepends: bool = False
        ) -> 'list[lib.t.Self[StringType] | string[lib.t.Any]]': ...
    @lib.t.overload
    def strip(
        self: lib.t.LiteralString,
        chars: lib.t.LiteralString | None = None,
        /
        ) -> lib.t.LiteralString: ...
    @lib.t.overload
    def strip(
        self,
        chars: str | None = None,
        /
        ) -> 'lib.t.Self[StringType] | string[lib.t.Any]': ...
    @lib.t.overload
    def swapcase(self: lib.t.LiteralString) -> lib.t.LiteralString: ...
    @lib.t.overload
    def swapcase(self) -> 'lib.t.Self[StringType] | string[lib.t.Any]': ...
    @lib.t.overload
    def title(self: lib.t.LiteralString) -> lib.t.LiteralString: ...
    @lib.t.overload
    def title(self) -> 'lib.t.Self[StringType] | string[lib.t.Any]': ...
    def translate(
        self,
        table: 'lib.builtins._TranslateTable',
        /
        ) -> 'lib.t.Self[StringType] | string[lib.t.Any]': ...
    @lib.t.overload
    def upper(self: lib.t.LiteralString) -> lib.t.LiteralString: ...
    @lib.t.overload
    def upper(self) -> 'lib.t.Self[StringType] | string[lib.t.Any]': ...
    @lib.t.overload
    def zfill(
        self: lib.t.LiteralString,
        width: lib.t.SupportsIndex,
        /
        ) -> lib.t.LiteralString: ...
    @lib.t.overload
    def zfill(
        self,
        width: lib.t.SupportsIndex,
        /
        ) -> 'lib.t.Self[StringType] | string[lib.t.Any]': ...
    @lib.t.overload
    def __add__(
        self: lib.t.LiteralString,
        value: lib.t.LiteralString,
        /
        ) -> lib.t.LiteralString: ...
    @lib.t.overload
    def __add__(
        self,
        value: str,
        /
        ) -> 'lib.t.Self[StringType] | string[lib.t.Any]': ...
    def __getitem__(
        self,
        key: lib.t.SupportsIndex | slice,
        /
        ) -> 'lib.t.Self[StringType] | string[lib.t.Any]': ...
    @lib.t.overload
    def __iter__(
        self: lib.t.LiteralString
        ) -> lib.t.Iterator[lib.t.LiteralString]: ...
    @lib.t.overload
    def __iter__(
        self
        ) -> 'lib.t.Iterator[lib.t.Self[StringType] | string[lib.t.Any]]': ...
    @lib.t.overload
    def __mod__(
        self: lib.t.LiteralString,
        value: lib.t.LiteralString | tuple[lib.t.LiteralString, ...],
        /
        ) -> lib.t.LiteralString: ...
    @lib.t.overload
    def __mod__(
        self,
        value: lib.t.Any,
        /
        ) -> 'lib.t.Self[StringType] | string[lib.t.Any]': ...
    @lib.t.overload
    def __mul__(
        self: lib.t.LiteralString,
        value: lib.t.SupportsIndex,
        /
        ) -> lib.t.LiteralString: ...
    @lib.t.overload
    def __mul__(
        self,
        value: lib.t.SupportsIndex,
        /
        ) -> 'lib.t.Self[StringType] | string[lib.t.Any]': ...
    @lib.t.overload
    def __rmul__(
        self: lib.t.LiteralString,
        value: lib.t.SupportsIndex,
        /
        ) -> lib.t.LiteralString: ...
    @lib.t.overload
    def __rmul__(
        self,
        value: lib.t.SupportsIndex,
        /
        ) -> 'lib.t.Self[StringType] | string[lib.t.Any]': ...
    def __getnewargs__(
        self
        ) -> 'tuple[lib.t.Self[StringType] | string[lib.t.Any]]': ...
