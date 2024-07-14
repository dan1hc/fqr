"""Strings objects."""

from . import lib

__all__ = (
    'Pattern',
    )


class Pattern:
    """Compiled regex patterns."""

    SnakeToCamelReplacements = lib.re.compile(r'(_[a-z0-9])')
    """
    Matches all lower case alphanumeric characters following any \
    non-leading underscore.

    ---

    Note: match is inclusive of underscores to improve substitution \
    performance.

    """

    CamelToSnakeReplacements = lib.re.compile(
        r'[A-Z0-9]([0-9]+|[a-z]+|([0-9][a-z])+)'
        )
    """Matches all Title Case and numeric components."""

    camelCase = lib.re.compile(r'^[a-z]+((\d)|([A-Z0-9][a-z0-9]{1,128})){0,32}$')
    """
    Matches strict [lower] camelCase (i.e. RESTful casing) according to \
    the [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html#s5.3-camel-case).

    ---

    Unlike Google, does NOT allow for an optional uppercase character at \
    the end of the string.

    Strings with moreThan32IndividualWords or \
    withWordsLongerThan128Characters will not be parsed.

    """

    snake_case = lib.re.compile(r'^[a-z0-9_]{1,256}$')
    """
    Matches strict [lower] snake_case (i.e. python casing).

    ---

    Strings longer than 256 characters will not be matched.

    """

    NumberPattern = lib.re.compile(
        r'^(([+-]?(([0-9](_?[0-9]){0,64})?(\.([0-9](_?[0-9]){0,64})?)?))+(e[+-]?([0-9](_?[0-9]){0,64})+)?)'  # noqa
        r'(j|(([+-](([0-9](_?[0-9]){0,64})?(\.([0-9](_?[0-9]){0,64})?)?))+(e[+-]?([0-9](_?[0-9]){0,64})+)?j))?$'  # noqa
        )
    """
    Matches integers, floats, scientific notation, and complex numbers.

    ---

    Supports precision up to 64 digits either side of a decimal point.

    Recognizes valid, pythonic underscore usage as well.

    """
