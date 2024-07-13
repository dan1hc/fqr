"""Module utils unit tests."""

import unittest

import fqr

from . import cns


class Constants(cns.Constants):
    """Constant values specific to unit tests in this file."""

    VALID_CAMEL_STRING_EXAMPLES = (
        'upperSnakeCaseString100SureFift337aGood',
        '_privateValidCamelCaseString'
        )
    VALID_SNAKE_STRING_EXAMPLES = (
        'upper_snake_case_string_100_sure_fift_337a_good',
        '_snake_case_string_'
        )


class TestUtils(unittest.TestCase):
    """Fixture for testing."""

    def test_01_str_to_forwardref(self):
        """Test `str` to `ForwardRef` casting."""

        self.assertIsInstance(
            fqr.core.typings.utl.parse_str_to_ref('int', False),
            fqr.core.lib.t.ForwardRef
            )

    def test_02_str_to_type(self):
        """Test `str` to `type` casting."""

        self.assertIs(
            fqr.core.typings.utl.resolve_type('int', globals(), locals()),
            int
            )

    def test_03_arg_ref_handling_no_ns(self):
        """Test `ForwardRef` handling for types not yet resolvable."""

        self.assertIsInstance(
            fqr.core.typings.utl.resolve_type('Unresolvable'),
            fqr.core.lib.t.ForwardRef
            )

    def test_04_arg_ref_handling(self):
        """Test `ForwardRef` handling for types with args."""

        self.assertIs(
            fqr.core.typings.utl.resolve_type(
                'Mockery[tuple[int, ...]]',
                globals(),
                locals()
                ),
            Mockery[tuple[int, ...]]
            )


class Mockery(fqr.core.lib.t.Generic[fqr.core.typ.AnyType]):
    """An as yet undefined generic class for testing."""
