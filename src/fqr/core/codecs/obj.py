"""Codecs objects."""

from . import lib

__all__ = (
    'Pattern',
    )


class Pattern:
    """Compiled regex patterns."""

    DateTime = lib.re.compile(r'[0-9]{4}-[0-9]{2}-[0-9]{2}[ T][0-9]{2}:[0-9]{2}:[0-9]{2}(\.([0-9]{1,6}))?([+-][0-9]{2}:[0-9]{2})?')  # noqa
    """
    Matches valid python `datetime` strings.

    ---

    Note: validity is determined by parsability `fromisoformat()`.

    """
