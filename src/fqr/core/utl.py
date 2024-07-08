"""Core utility functions."""

__all__ = (
    'camel_case_to_snake_case',
    'cname_for',
    'isCamelCaseIterable',
    'is_snake_case_iterable',
    'is_snake_case_string',
    'isCamelCaseString',
    'snake_case_to_camel_case',
    'validate_casing',
    )

from . import typ
from . import enm
from . import exc
from . import lib
from . import obj


def isCamelCaseString(
    string: str
    ) -> lib.t.TypeGuard[typ.camelCaseString]:
    """
    Check if `string` is valid `camelCase`.

    ---

    Checks for strict [lower] `camelCase` (i.e. `RESTful casing`) \
    according to the [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html#s5.3-camel-case).

    Unlike Google, does *NOT* allow for an optional uppercase character \
    at the end of the `string`.

    """

    return _isCamelCaseString(string)


@lib.functools.cache
def _isCamelCaseString(string: str) -> bool:
    return bool(obj.Pattern.camelCase.match(string))


def is_snake_case_string(
    string: str
    ) -> lib.t.TypeGuard[typ.snake_case_string]:
    """
    Check if `string` is valid `snake_case`.

    ---

    Checks for strict [lower] `snake_case` (i.e. `python casing`).

    """

    return _is_snake_case_string(string)


@lib.functools.cache
def _is_snake_case_string(string: str) -> bool:
    return bool(obj.Pattern.snake_case.match(string))


@lib.functools.cache
def validate_casing(
    value: lib.t.Any,
    casing: typ.Casing
    ) -> lib.t.Optional[lib.Never]:
    """
    Assert value is `str` and of correct `Casing`.

    ---

    Raises `TypeError` if not `str`.

    Raises `StringCasingError` if `str` of incorrect `Casing`.

    """

    if not isinstance(value, str):
        raise TypeError(
            f'{value!s} is not a valid `str`.'
            )
    elif (
        casing == enm.SupportedCasing.snake_case.value
        and not is_snake_case_string(value)
        ):
        raise exc.StringCasingError(value, casing)
    elif (
        casing == enm.SupportedCasing.camelCase.value
        and not isCamelCaseString(value)
        ):
        raise exc.StringCasingError(value, casing)
    else:
        return None


@lib.functools.cache
def snake_case_to_camel_case(
    snake_case_string: typ.snake_case_string
    ) -> typ.camelCaseString:
    """Convert a valid `snake_case_string` to `camelCase`."""

    camelCaseString: typ.camelCaseString = (
        obj.Pattern.SnakeToCamelReplacements.sub(
            lambda match: match.group()[-1].upper(),
            snake_case_string
            )
        )

    return camelCaseString


@lib.functools.cache
def camel_case_to_snake_case(
    camelCaseString: typ.camelCaseString
    ) -> typ.snake_case_string:
    """Convert a valid `camelCaseString` to `snake_case`."""

    snake_case_string: typ.snake_case_string = (
        obj.Pattern.CamelToSnakeReplacements.sub(
            lambda match: '_' + match.group().lower(),
            camelCaseString
            )
        )

    return snake_case_string


def is_snake_case_iterable(
    strings: lib.t.Iterable[str]
    ) -> lib.t.TypeGuard[lib.t.Iterable[typ.snake_case_string]]:
    """
    Check if all `strings` are `snake_case`.

    ---

    Ignores leading and / or trailing underscores.

    """

    return all(
        is_snake_case_string(string)
        for _string
        in strings
        if (string := _string.strip('_'))
        )


def isCamelCaseIterable(
    strings: lib.t.Iterable[str]
    ) -> lib.t.TypeGuard[lib.t.Iterable[typ.camelCaseString]]:
    """
    Check if all `strings` are `camelCase`.

    ---

    Ignores leading and / or trailing underscores.

    """

    return all(
        isCamelCaseString(string)
        for _string
        in strings
        if (string := _string.strip('_'))
        )


def cname_for(
    string: str,
    container: lib.t.Container
    ) -> lib.t.Optional[str] | lib.Never:
    """
    Get the actual, canonical name for valid `string`, as contained in \
    an arbitrary, valid `container`, agnostic of `string` casing and / or \
    underscores.

    ---

    ### Example Usage

    ```py
    d = {'_id': 123}
    cname_for(d, 'id')
    >>>
    '_id'
    ```

    """

    if (
        (k := (_k := string.strip('_'))) in container
        or (k := '_' + _k) in container
        or (k := _k + '_') in container
        or (k := '_' + _k + '_') in container
        ):
        return k
    elif (
        is_snake_case_string(string)
        and (
            (
                camel_k := (
                    _camel_k := snake_case_to_camel_case(
                        string.strip('_')
                        )
                    )
                ) in container
            or (camel_k := '_' + _camel_k) in container
            or (camel_k := _camel_k + '_') in container
            or (camel_k := '_' + _camel_k + '_') in container
            )
        ):
        return camel_k
    else:
        return None
