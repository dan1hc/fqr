"""Typing types."""

from .. import typ

__all__ = (
    'AnyOrForwardRef',
    'StrOrForwardRef',
    *typ.__all__
    )

from .. typ import *

from . import lib

AnyOrForwardRef = lib.t.ForwardRef | lib.t.Any
StrOrForwardRef = lib.t.ForwardRef | str
