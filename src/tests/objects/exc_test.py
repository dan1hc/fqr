import pickle
import unittest

import fqr


class TestExceptions(unittest.TestCase):
    """Fixture for testing exceptions."""

    def setUp(self) -> None:
        return super().setUp()

    def test_01_serialization(self):
        """Test multi-arg exc serializes correctly."""

        exc = fqr.objects.exc.IncorrectCasingError(('a', 'b'))
        dump = pickle.dumps(exc)
        reloaded: fqr.core.typ.PackageExceptionType = pickle.loads(dump)
        self.assertTupleEqual(
            exc.args,
            reloaded.args
            )

    def test_02_serialization(self):
        """Test multi-arg exc serializes correctly."""

        exc = fqr.objects.exc.IncorrectDefaultTypeError('test', str, 2)
        dump = pickle.dumps(exc)
        reloaded: fqr.core.typ.PackageExceptionType = pickle.loads(dump)
        self.assertTupleEqual(
            exc.args,
            reloaded.args
            )

    def test_03_serialization(self):
        """Test multi-arg exc serializes correctly."""

        exc = fqr.objects.exc.IncorrectTypeError('test', str, 2)
        dump = pickle.dumps(exc)
        reloaded: fqr.core.typ.PackageExceptionType = pickle.loads(dump)
        self.assertTupleEqual(
            exc.args,
            reloaded.args
            )

    def test_04_serialization(self):
        """Test multi-arg exc serializes correctly."""

        exc = fqr.objects.exc.InvalidComparisonTypeError('test', str, 2)
        dump = pickle.dumps(exc)
        reloaded: fqr.core.typ.PackageExceptionType = pickle.loads(dump)
        self.assertTupleEqual(
            exc.args,
            reloaded.args
            )

    def test_05_serialization(self):
        """Test multi-arg exc serializes correctly."""

        exc = fqr.objects.exc.InvalidContainerComparisonTypeError(
            'test',
            list[str],
            2
            )
        dump = pickle.dumps(exc)
        reloaded: fqr.core.typ.PackageExceptionType = pickle.loads(dump)
        self.assertTupleEqual(
            exc.args,
            reloaded.args
            )

    def test_06_serialization(self):
        """Test exc serializes correctly."""

        exc = fqr.objects.exc.FieldAnnotationError('test', int)
        dump = pickle.dumps(exc)
        reloaded: fqr.core.typ.PackageExceptionType = pickle.loads(dump)
        self.assertTupleEqual(exc.args, reloaded.args)
