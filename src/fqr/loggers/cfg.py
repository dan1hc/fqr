"""Loggers constants."""

__all__ = (
    'Constants',
    )

from .. import core

from . import lib


class Constants(core.cfg.Constants):
    """Constant values shared across log modules."""

    FTIME_LOG      = '%Y-%m-%d %H:%M:%S'
    FTIME_LOG_MSEC = '%s.%03d UTC'

    LOG_LEVEL      = lib.os.getenv(
        'LOG_LEVEL',
        'DEBUG' if core.cfg.Constants.ENV in {'dev', 'develop', 'local'} else 'INFO'
        ).upper()
    LOG_TRACEBACK  = lib.os.getenv('LOG_TRACEBACK', 'false').lower() == 'true'
    LOG_PRINTS     = lib.os.getenv('LOG_PRINTS', 'false').lower() == 'true'

    SILENCE_MSG    = f'Call to print() silenced by {core.cfg.Constants.PACAKGE}.'
    WARN_MSG       = f'Calls to print() will be silenced by {core.cfg.Constants.PACAKGE}.'
