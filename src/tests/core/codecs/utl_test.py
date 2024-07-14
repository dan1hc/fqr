"""Module utils unit tests."""

import unittest

import fqr

from . import cns


class Constants(cns.Constants):
    """Constant values specific to unit tests in this file."""

    SimpleDict: dict[str, tuple[int, ...]] = {
        'a_simple_key': (0, ),
        '_and_another_': (4, 3, 2, ),
        'components': (1, 2, )
        }
    SimpleTuple = (1, 2, 3, )
    BoolTuple = (True, False, True, )
    BoundType = fqr.core.lib.t.TypeVar('BoundType', bound=int)
    ComplexStr = '1.134_12e+2-1.134_12e+2j'
    ConstrainedType = fqr.core.lib.t.TypeVar('ConstrainedType', bool, int)
    AnotherConstrainedType = fqr.core.lib.t.TypeVar(
        'AnotherConstrainedType',
        tuple[int] | tuple[str],
        tuple[bool] | tuple[int],
        tuple[float] | tuple[bool] | tuple[int] | bool
        )
    NestedDict = {'nesting': SimpleDict}


class TestUtils(unittest.TestCase):
    """Fixture for testing."""

    def test_01_tuple_parse(self):
        """Test `parse` on `tuple[int, ...]`."""

        self.assertEqual(
            Constants.SimpleTuple,
            fqr.core.codecs.utl.parse(
                fqr.core.codecs.lib.json.dumps(Constants.SimpleTuple),
                tuple[int, ...]
                )
            )

    def test_02_dict_parse(self):
        """Test `parse` on `dict[str, tuple[int, ...]]`."""

        self.assertEqual(
            Constants.SimpleDict,
            fqr.core.codecs.utl.parse(
                fqr.core.codecs.lib.json.dumps(Constants.SimpleDict),
                dict[str, tuple[int, ...]]
                )
            )

    def test_03_typevar_parse_bound(self):
        """Test `parse` on `tuple[BoundType, ...]`."""

        self.assertNotEqual(
            Constants.SimpleTuple,
            fqr.core.codecs.utl.parse(
                fqr.core.codecs.lib.json.dumps(Constants.BoolTuple),
                tuple[Constants.BoundType, ...]
                )
            )

    def test_04_typevar_parse_bound(self):
        """Test `parse` on `tuple[BoundType, ...]`."""

        self.assertEqual(
            Constants.BoolTuple,
            fqr.core.codecs.utl.parse(
                fqr.core.codecs.lib.json.dumps(Constants.BoolTuple),
                tuple[Constants.BoundType, ...]
                )
            )

    def test_05_typevar_parse_constrained(self):
        """Test `parse` on `tuple[ConstrainedType, ...]`."""

        self.assertEqual(
            Constants.BoolTuple,
            fqr.core.codecs.utl.parse(
                fqr.core.codecs.lib.json.dumps(Constants.BoolTuple),
                tuple[Constants.ConstrainedType, ...]
                )
            )

    def test_06_nested_dict_parse(self):
        """Test `parse` on `dict[str, dict[str, tuple[int, ...]]]`."""

        self.assertEqual(
            Constants.NestedDict,
            fqr.core.codecs.utl.parse(
                fqr.core.codecs.lib.json.dumps(Constants.NestedDict),
                dict[str, dict[str, tuple[int, ...]]]
                )
            )

    def test_07_bool_parse(self):
        """Test `parse` on `bool`."""

        self.assertIs(True, fqr.core.codecs.utl.parse('true', bool))

    def test_08_anti_bool_parse(self):
        """Test `parse` on `bool`."""

        self.assertEqual(
            fqr.core.codecs.enm.ParseErrorRef.bool_decode,
            fqr.core.codecs.utl.parse('asdf', bool)
            )

    def test_09_float_parse(self):
        """Test `parse` on `float`."""

        self.assertEqual(1.8, fqr.core.codecs.utl.parse('1.8', float))

    def test_10_anti_float_parse(self):
        """Test `parse` on `float`."""

        self.assertEqual(
            fqr.core.codecs.enm.ParseErrorRef.number_decode,
            fqr.core.codecs.utl.parse('asdf', float)
            )

    def test_11_complex_parse(self):
        """Test `parse` on `complex`."""

        self.assertEqual(
            complex(Constants.ComplexStr),
            fqr.core.codecs.utl.parse(Constants.ComplexStr, complex)
            )

    def test_12_none_parse(self):
        """Test `parse` on `None`."""

        self.assertIsNone(fqr.core.codecs.utl.parse('null', type(None)))

    def test_13_anti_none_parse(self):
        """Test `parse` on `None`."""

        self.assertEqual(
            fqr.core.codecs.enm.ParseErrorRef.null_decode,
            fqr.core.codecs.utl.parse('asdf', type(None))
            )

    def test_14_union_parse(self):
        """Test `parse` on `int | str`."""

        self.assertIsInstance(fqr.core.codecs.utl.parse('42', tuple[int] | int), int)

    def test_15_anti_tuple_parse(self):
        """Test `parse` on `tuple[int, ...]`."""

        self.assertEqual(
            fqr.core.codecs.enm.ParseErrorRef.invalid_arr_decode,
            fqr.core.codecs.utl.parse(
                fqr.core.codecs.lib.json.dumps(Constants.SimpleTuple),
                tuple[frozenset, ...]
                )
            )

    def test_16_known_tuple_parse(self):
        """Test `parse` on `tuple[int, int, int]`."""

        self.assertEqual(
            Constants.SimpleTuple,
            fqr.core.codecs.utl.parse(
                fqr.core.codecs.lib.json.dumps(Constants.SimpleTuple),
                tuple[int, int, int]
                )
            )

    def test_17_anti_known_tuple_parse(self):
        """Test `parse` on `tuple[int, int, int]`."""

        self.assertEqual(
            fqr.core.codecs.enm.ParseErrorRef.invalid_arr_len,
            fqr.core.codecs.utl.parse(
                fqr.core.codecs.lib.json.dumps(Constants.SimpleTuple),
                tuple[int, int]
                )
            )

    def test_18_anti_known_tuple_parse(self):
        """Test `parse` on `tuple[int, int, int]`."""

        self.assertEqual(
            fqr.core.codecs.enm.ParseErrorRef.invalid_arr_decode,
            fqr.core.codecs.utl.parse(
                fqr.core.codecs.lib.json.dumps(Constants.SimpleTuple),
                tuple[frozenset, list, tuple]
                )
            )

    def test_19_list_parse(self):
        """Test `parse` on `list[int]`."""

        self.assertEqual(
            list(Constants.SimpleTuple),
            fqr.core.codecs.utl.parse(
                fqr.core.codecs.lib.json.dumps(Constants.SimpleTuple),
                list[int]
                )
            )

    def test_20_anti_list_parse(self):
        """Test `parse` on `list[int]`."""

        self.assertEqual(
            fqr.core.codecs.enm.ParseErrorRef.value_decode,
            fqr.core.codecs.utl.parse('42', list[int])
            )

    def test_21_anti_list_parse(self):
        """Test `parse` on `list[int]`."""

        self.assertEqual(
            fqr.core.codecs.enm.ParseErrorRef.invalid_arr_decode,
            fqr.core.codecs.utl.parse(
                fqr.core.codecs.lib.json.dumps(Constants.SimpleTuple),
                list[frozenset]
                )
            )

    def test_22_anti_list_parse(self):
        """Test `parse` on `list[int]`."""

        self.assertEqual(
            fqr.core.codecs.enm.ParseErrorRef.invalid_json,
            fqr.core.codecs.utl.parse('asdf', list[frozenset])
            )

    def test_23_anti_dict_parse(self):
        """Test `parse` on `dict[str, tuple[int, ...]]`."""

        self.assertEqual(
            fqr.core.codecs.enm.ParseErrorRef.invalid_json,
            fqr.core.codecs.utl.parse('asdf', dict[str, tuple[int, ...]])
            )

    def test_24_anti_dict_parse(self):
        """Test `parse` on `dict[str, tuple[int, ...]]`."""

        self.assertEqual(
            fqr.core.codecs.enm.ParseErrorRef.invalid_keys_decode,
            fqr.core.codecs.utl.parse(
                fqr.core.codecs.lib.json.dumps(
                    {
                        i: v
                        for (i, v)
                        in enumerate(Constants.SimpleDict.values())
                        }
                    ),
                dict[tuple[str], tuple[int, ...]]
                )
            )

    def test_25_anti_dict_parse(self):
        """Test `parse` on `dict[str, tuple[int, ...]]`."""

        self.assertEqual(
            fqr.core.codecs.enm.ParseErrorRef.invalid_values_decode,
            fqr.core.codecs.utl.parse(
                fqr.core.codecs.lib.json.dumps(
                    {
                        k: i
                        for (i, k)
                        in enumerate(Constants.SimpleDict.keys())
                        }
                    ),
                dict[str, tuple[int, ...]]
                )
            )

    def test_26_anti_dict_parse(self):
        """Test `parse` on `dict[str, tuple[int, ...]]`."""

        self.assertEqual(
            fqr.core.codecs.enm.ParseErrorRef.invalid_map_decode,
            fqr.core.codecs.utl.parse(
                fqr.core.codecs.lib.json.dumps(Constants.SimpleDict),
                dict[str]
                )
            )

    def test_27_anti_dict_parse(self):
        """Test `parse` on `dict[str, tuple[int, ...]]`."""

        self.assertEqual(
            fqr.core.codecs.enm.ParseErrorRef.value_decode,
            fqr.core.codecs.utl.parse(
                fqr.core.codecs.lib.json.dumps(Constants.SimpleTuple),
                dict[str, tuple[int, ...]]
                )
            )

    def test_28_typevar_parse_unbound(self):
        """Test `parse` on `tuple[BoundType, ...]`."""

        self.assertEqual(
            Constants.BoolTuple,
            fqr.core.codecs.utl.parse(
                fqr.core.codecs.lib.json.dumps(Constants.BoolTuple),
                tuple[fqr.core.typ.AnyType, ...]
                )
            )

    def test_29_typevar_parse_constrained_again(self):
        """Test `parse` on `tuple[AnotherConstrainedType, ...]`."""

        self.assertEqual(
            Constants.BoolTuple,
            fqr.core.codecs.utl.parse(
                fqr.core.codecs.lib.json.dumps(Constants.BoolTuple),
                tuple[Constants.AnotherConstrainedType, ...]
                )
            )
