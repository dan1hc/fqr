"""Typing utility functions."""

__all__ = (
    'get_type_args',
    'resolve_type',
    )

from . import lib
from . import obj
from . import typ


eval_type: lib.t.Callable[
    [
        typ.AnyOrForwardRef,
        lib.t.Any,
        lib.t.Any,
        lib.t.Optional[frozenset]
        ],
    lib.t.Any
    ] = lib.t._eval_type  # type: ignore[attr-defined]
"""
Evaluate all `ForwardRef` in the given `type`.

---

For use of globalns and localns see the docstring for `get_type_hints()`.

`recursive_guard` is used to prevent infinite recursion with a recursive
`ForwardRef`.

"""


@lib.functools.cache
def get_args(typ: lib.t.Any) -> tuple[lib.t.Any, ...]:
    """Memoized wrapper for `typing.get_args`."""

    return lib.t.get_args(typ)


@lib.t.overload
def get_type_args(
    typ: obj.SupportsParams[lib.Unpack[typ.ArgsType]],
    ) -> tuple[lib.Unpack[typ.ArgsType]]: ...
@lib.t.overload
def get_type_args(
    typ: obj.SupportsParams[lib.Unpack[tuple[lib.t.Any, ...]]]
    ) -> tuple[lib.t.Any, ...]: ...
def get_type_args(
    typ: (
        obj.SupportsParams[lib.Unpack[typ.ArgsType]]
        | obj.SupportsParams[lib.Unpack[tuple[lib.t.Any, ...]]]
        )
    ) -> (
        tuple[lib.Unpack[typ.ArgsType]]
        | tuple[lib.t.Any, ...]
        ):
    """
    Get generic arguments for `type[Any]`.

    ---

    ### Example

    ```py
    get_type_args(tuple[str, int])
    (str, int, )

    ```

    """

    return get_args(typ)


@lib.t.overload
def is_params_type(
    typ: obj.SupportsParams[lib.Unpack[typ.ArgsType]],
    ) -> lib.t.TypeGuard[
        obj.SupportsParams[lib.Unpack[typ.ArgsType]]
        ]: ...
@lib.t.overload
def is_params_type(
    typ: lib.t.Any
    ) -> lib.t.TypeGuard[
        obj.SupportsParams[lib.Unpack[tuple[lib.t.Any, ...]]]
        ]: ...
def is_params_type(
    typ: obj.SupportsParams[lib.Unpack[typ.ArgsType]] | lib.t.Any
    ) -> lib.t.TypeGuard[
        obj.SupportsParams[lib.Unpack[typ.ArgsType]]
        | obj.SupportsParams[lib.Unpack[tuple[lib.t.Any, ...]]]
        ]:
    """Return `True` if `typ` has type args."""

    return bool(get_args(typ))


@lib.t.overload
def parse_ref_to_typ(
    ref: lib.t.ForwardRef,
    globalns: None,
    localns: typ.OptionalAnyDict
    ) -> lib.t.ForwardRef: ...
@lib.t.overload
def parse_ref_to_typ(
    ref: lib.t.ForwardRef,
    globalns: typ.OptionalAnyDict,
    localns: typ.OptionalAnyDict
    ) -> typ.AnyOrForwardRef: ...
def parse_ref_to_typ(
    ref: lib.t.ForwardRef,
    globalns: typ.OptionalAnyDict = None,
    localns: typ.OptionalAnyDict = None
    ) -> typ.AnyOrForwardRef:
    """Attempt to cast `ForwardRef` to `type`."""

    try:
        typ = eval_type(
            ref,
            globalns,
            localns,
            frozenset()
            )
    except NameError:
        return ref
    else:
        return typ


def parse_str_to_ref(
    typ_as_str: str,
    is_argument: bool,
    ) -> lib.t.ForwardRef:
    """Cast `str` to `ForwardRef`."""

    return lib.t.ForwardRef(
        typ_as_str,
        is_argument=is_argument,
        is_class=True
        )


@lib.t.overload
def resolve_type(
    typ_ref_or_str: typ.AnyType | typ.StrOrForwardRef,
    globalns: typ.AnyDict,
    localns: typ.AnyDict,
    is_argument: bool
    ) -> typ.AnyType | lib.t.Any: ...
@lib.t.overload
def resolve_type(
    typ_ref_or_str: typ.AnyType | typ.StrOrForwardRef,
    globalns: typ.OptionalAnyDict,
    localns: typ.OptionalAnyDict,
    is_argument: bool
    ) -> typ.AnyType | typ.AnyOrForwardRef: ...
@lib.t.overload
def resolve_type(
    typ_ref_or_str: typ.StrOrForwardRef,
    globalns: typ.OptionalAnyDict = None,
    localns: typ.OptionalAnyDict = None,
    is_argument: bool = False
    ) -> typ.AnyOrForwardRef: ...
def resolve_type(
    typ_ref_or_str: typ.AnyType | typ.StrOrForwardRef,
    globalns: typ.OptionalAnyDict = None,
    localns: typ.OptionalAnyDict = None,
    is_argument: bool = False
    ) -> typ.AnyType | typ.AnyOrForwardRef:
    """
    Attempt to resolve `str` or `ForwardRef` to `type`.

    ---

    Recursively resolves parameterized generics.

    """

    if isinstance(typ_ref_or_str, str):
        ref = parse_str_to_ref(typ_ref_or_str, is_argument)
        return resolve_type(ref, globalns, localns, is_argument)
    elif is_params_type(typ_ref_or_str):
        args = get_type_args(typ_ref_or_str)
        for arg in args:
            resolve_type(arg, globalns, localns, True)
        return typ_ref_or_str
    elif isinstance(typ_ref_or_str, lib.t.ForwardRef):
        typ_or_ref = parse_ref_to_typ(typ_ref_or_str, globalns, localns)
        if is_params_type(typ_or_ref):
            return resolve_type(typ_or_ref, globalns, localns, is_argument)
        else:
            return typ_or_ref
    else:
        return typ_ref_or_str
