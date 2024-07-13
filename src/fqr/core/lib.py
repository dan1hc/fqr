"""Core imports."""

__all__ = (
    'argparse',
    'collections',
    'datetime',
    'enum',
    'functools',
    'os',
    're',
    'sys',
    't',
    'urllib',
    'Never',
    'Self',
    'TypeVarTuple',
    'Unpack',
    )

import argparse
import collections.abc
import datetime
import enum
import functools
import os
import re
import sys
import typing as t
import urllib.parse

if sys.version_info < (3, 11):  # pragma: no cover
    from typing_extensions import Never, Self, TypeVarTuple, Unpack  # noqa  # type: ignore
else:  # pragma: no cover
    from typing import Never, Self, TypeVarTuple, Unpack
