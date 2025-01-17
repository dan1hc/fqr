"""Module utils unit tests."""

import unittest

import fqr

from ... import mocking

from . import cfg


class SimpleTypedObj(fqr.core.lib.t.TypedDict):
    """Simple `SupportsAnnotation` object."""

    name: str
    id_: int


class InitVarClass(fqr.Object):
    """Has an InitVar for testing."""

    init_var: fqr.Field[fqr.core.lib.dataclasses.InitVar]
    init_var_as_str: 'fqr.Field[fqr.core.lib.dataclasses.InitVar]'


class Constants(cfg.Constants):
    """Constant values specific to unit tests in this file."""


class TestUtils(unittest.TestCase):
    """Fixture for testing."""

    def test_01_str_to_forwardref(self):
        """Test `str` to `ForwardRef` casting."""

        self.assertIsInstance(
            fqr.core.typ.utl.hint.parse_str_to_ref('int', False),
            fqr.core.lib.t.ForwardRef
            )

    def test_02_str_to_type(self):
        """Test `str` to `type` casting."""

        self.assertIs(
            fqr.core.typ.utl.hint.resolve_type(
                'int',
                globals(),
                locals()
                ),
            int
            )

    def test_03_arg_ref_handling_no_ns(self):
        """Test `ForwardRef` handling for types not yet resolvable."""

        self.assertIsInstance(
            fqr.core.typ.utl.hint.resolve_type('Unresolvable'),
            fqr.core.lib.t.ForwardRef
            )

    def test_04_arg_ref_handling(self):
        """Test `ForwardRef` handling for types with args."""

        self.assertIs(
            fqr.core.typ.utl.hint.resolve_type(
                'Mockery[tuple[int, ...]]',
                globals(),
                locals()
                ),
            Mockery[tuple[int, ...]]
            )

    def test_05_anti_is_array_type(self):
        """Test `is_array_type`."""

        self.assertFalse(fqr.core.typ.utl.check.is_array_type(None))

    def test_06_anti_is_variadic_array_type(self):
        """Test `is_variadic_array_type`."""

        self.assertFalse(
            fqr.core.typ.utl.check.is_variadic_array_type(None)
            )

    def test_07_anti_is_mapping_type(self):
        """Test `is_mapping_type`."""

        self.assertFalse(fqr.core.typ.utl.check.is_mapping_type(None))

    def test_08_anti_is_none_type(self):
        """Test `is_none_type`."""

        self.assertFalse(fqr.core.typ.utl.check.is_none_type(None))

    def test_09_anti_is_number_type(self):
        """Test `is_number_type`."""

        self.assertFalse(fqr.core.typ.utl.check.is_number_type(None))

    def test_10_anti_is_bool_type(self):
        """Test `is_bool_type`."""

        self.assertFalse(fqr.core.typ.utl.check.is_bool_type(None))

    def test_11_anti_is_datetime_type(self):
        """Test `is_datetime_type`."""

        self.assertFalse(fqr.core.typ.utl.check.is_datetime_type(None))

    def test_12_anti_is_date_type(self):
        """Test `is_date_type`."""

        self.assertFalse(fqr.core.typ.utl.check.is_date_type(None))

    def test_13_annotations_cache(self):
        """Test `collect_annotations`."""

        self.assertEqual(
            SimpleTypedObj.__annotations__,
            fqr.core.typ.utl.hint.collect_annotations(SimpleTypedObj)
            )

    def test_14_is_object(self):
        """Test `is_object`."""

        self.assertTrue(
            fqr.core.typ.utl.check.is_object(mocking.Derivative)
            )

    def test_15_is_field_type_forward_str(self):
        """Test `is_field_type` works with `str` ForwardRef."""

        self.assertTrue(
            fqr.core.typ.utl.check.is_field_type('Field[Any]')
            )

    def test_16_is_immutable_type(self):
        """Test `is_immutable_type`."""

        self.assertTrue(
            fqr.core.typ.utl.check.is_immutable_type(
                tuple[str, ...]
                )
            )


class Mockery(fqr.core.lib.t.Generic[fqr.core.typ.AnyType]):
    """An as yet undefined generic class for testing."""
