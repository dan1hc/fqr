"""Core objects."""

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

    camelCase = lib.re.compile(r'^[a-z]+((\d)|([A-Z0-9][a-z0-9]+))*$')
    """
    Matches strict [lower] camelCase (i.e. RESTful casing) according to \
    the [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html#s5.3-camel-case).

    ---

    Unlike Google, does NOT allow for an optional uppercase character at \
    the end of the string.

    """

    snake_case = lib.re.compile(r'^[a-z0-9_]+$')
    """Matches strict [lower] snake_case (i.e. python casing)."""
