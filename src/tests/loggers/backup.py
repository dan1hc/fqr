import unittest

import fqr

from fqr . loggers import lib

from .. import mocking

from . import cfg


class Constants(cfg.Constants):
    """Constant values specific to this file."""


class TestLogger(unittest.TestCase):
    """Fixture for testing logger."""

    def setUp(self) -> None:
        self.log = fqr.log
        self.msg_str = 'example'
        self.msg_dict = {'str': 'example', 'a': 2}
        self.msg_cls = mocking.examples.Pet
        self.msg_object_= mocking.examples.Pet(
            id_='abc1234',
            name='Fido',
            type='dog',
            )
        return super().setUp()

    def test_01_log(self):
        """Test str logging."""

        msg = self.msg_str
        level = lib.logging.DEBUG
        expected_output = lib.textwrap.indent(
            lib.json.dumps(
                fqr.loggers.utl.parse_incoming_log_message(msg, level),
                default=fqr.core.strings.utl.convert_for_repr,
                indent=Constants.INDENT,
                sort_keys=True
                ),
            Constants.INDENT * ' '
            )
        with self.assertLogs(self.log, level) as logger:
            fqr.log.debug(msg)
            self.assertEqual(logger.records[0].msg, expected_output)

    def test_02_log(self):
        """Test dict logging."""

        msg = self.msg_dict
        level = lib.logging.INFO
        expected_output = lib.textwrap.indent(
            lib.json.dumps(
                fqr.loggers.utl.parse_incoming_log_message(msg, level),
                default=fqr.core.strings.utl.convert_for_repr,
                indent=Constants.INDENT,
                sort_keys=True
                ),
            Constants.INDENT * ' '
            )
        with self.assertLogs(self.log, level) as logger:
            fqr.log.info(msg)
            self.assertEqual(logger.records[0].msg, expected_output)

    def test_03_log(self):
        """Test cls logging."""

        msg = self.msg_cls
        level = lib.logging.WARNING
        expected_output = lib.textwrap.indent(
            lib.json.dumps(
                fqr.loggers.utl.parse_incoming_log_message(msg, level),
                default=fqr.core.strings.utl.convert_for_repr,
                indent=Constants.INDENT,
                sort_keys=True
                ),
            Constants.INDENT * ' '
            )
        with self.assertLogs(self.log, level) as logger:
            fqr.log.warning(msg)
            self.assertEqual(logger.records[0].msg, expected_output)

    def test_04_log(self):
        """Test object logging."""

        msg = self.msg_object_
        level = lib.logging.ERROR
        expected_output = lib.textwrap.indent(
            lib.json.dumps(
                fqr.loggers.utl.parse_incoming_log_message(msg, level),
                default=fqr.core.strings.utl.convert_for_repr,
                indent=Constants.INDENT,
                sort_keys=True
                ),
            Constants.INDENT * ' '
            )
        with self.assertLogs(self.log, level) as logger:
            fqr.log.error(msg)
            self.assertEqual(logger.records[0].msg, expected_output)

    def test_05_log(self):
        """Test exc logging."""

        msg = self.msg_str
        level = lib.logging.ERROR
        parsed = fqr.loggers.utl.parse_incoming_log_message(msg, level)
        with self.assertLogs(self.log, level) as logger:
            try:
                _ = 1 / 0
            except Exception:
                fqr.log.error(msg)
                expected_output = lib.textwrap.indent(
                    lib.json.dumps(
                        parsed,
                        default=fqr.core.strings.utl.convert_for_repr,
                        indent=Constants.INDENT,
                        sort_keys=True
                        ),
                    Constants.INDENT * ' '
                    )
            self.assertEqual(logger.records[0].msg, expected_output)

    def test_06_log(self):
        """Test exc logging."""

        msg = self.msg_str
        level = lib.logging.DEBUG
        parsed = fqr.loggers.utl.parse_incoming_log_message(msg, level)
        with self.assertLogs(self.log, level) as logger:
            try:
                _ = 1 / 0
            except Exception as e:
                self.log.debug(msg, exc_info=e)
                expected_output = lib.textwrap.indent(
                    lib.json.dumps(
                        parsed,
                        default=fqr.core.strings.utl.convert_for_repr,
                        indent=Constants.INDENT,
                        sort_keys=True
                        ),
                    Constants.INDENT * ' '
                    )
            self.assertEqual(logger.records[0].msg, expected_output)

    def test_07_print(self):
        """Test first print + warning interception."""

        msg = self.msg_str
        level = lib.logging.WARNING
        parsed = fqr.loggers.utl.parse_incoming_log_message(
            Constants.WARN_MSG,
            level
            )
        with self.assertLogs(self.log, level) as logger:
            print(msg)
            expected_output = lib.textwrap.indent(
                lib.json.dumps(
                    parsed,
                    default=fqr.core.strings.utl.convert_for_repr,
                    indent=Constants.INDENT,
                    sort_keys=True
                    ),
                Constants.INDENT * ' '
                )
            self.assertEqual(
                logger.records[0].msg,
                expected_output
                )

    def test_08_print(self):
        """Test subsequent print interceptions."""

        msg = self.msg_str
        with self.assertWarns(Warning) as emitter:
            with self.assertNoLogs(self.log):
                print(msg)
                self.assertEqual(
                    emitter.warnings[0].message.args[0],
                    Constants.WARN_MSG
                    )


class TestDeployedLogger(unittest.TestCase):
    """Fixture for testing logger in higher environments."""

    def setUp(self) -> None:
        Constants.ENV = 'dev'
        fqr.loggers.obj._set_print_interception()
        self.log = fqr.log
        self.msg = mocking.examples.Pet
        return super().setUp()

    def test_01_print(self):
        """Test first print + warning interception."""

        # lib.sys.__dict__['modules'][fqr.loggers.obj.__name__].__dict__.pop('__warningregistry__')

        msg = self.msg
        warn_msg = '\n'.join(
            (
                '.py:line_no: WarningClass: ',
                Constants.WARN_MSG,
                str(msg),
                'lib.warnings.warn()'
                )
            )
        level = lib.logging.WARNING
        parsed = fqr.loggers.utl.parse_incoming_log_message(warn_msg, level)
        with self.assertLogs(self.log, level) as logger:
            # expected_output = lib.textwrap.indent(
            #     lib.json.dumps(
            #         parsed,
            #         default=fqr.core.strings.utl.convert_for_repr,
            #         indent=Constants.INDENT,
            #         sort_keys=True
            #         ),
            #     Constants.INDENT * ' '
            #     )
            expected_output = lib.json.dumps(
                parsed,
                default=fqr.core.strings.utl.convert_for_repr,
                indent=Constants.INDENT,
                sort_keys=True
                )
            print(msg)
            self.assertEqual(
                logger.records[0].msg,
                expected_output
                )

    def test_02_print(self):
        """Test subsequent, same message print interceptions."""

        msg = self.msg
        warn_msg = '\n'.join(
            (
                Constants.SILENCE_MSG,
                str(msg),
                )
            )
        with self.assertWarns(Warning) as emitter:
            with self.assertNoLogs(self.log):
                print(msg)
                self.assertEqual(
                    emitter.warnings[0].message.args[0],
                    warn_msg
                    )

    def test_03_print(self):
        """Test subsequent, new message print + warning interception."""

        msg = 'testing'
        warn_msg = '\n'.join(
            (
                '.py:line_no: WarningClass: ',
                Constants.SILENCE_MSG,
                str(msg),
                'lib.warnings.warn()'
                )
            )
        level = lib.logging.WARNING
        parsed = fqr.loggers.utl.parse_incoming_log_message(warn_msg, level)
        with self.assertLogs(self.log, level) as logger:
            print(msg)
            expected_output = lib.textwrap.indent(
                lib.json.dumps(
                    parsed,
                    default=fqr.core.strings.utl.convert_for_repr,
                    indent=Constants.INDENT,
                    sort_keys=True
                    ),
                Constants.INDENT * ' '
                )
            self.assertEqual(
                logger.records[0].msg,
                expected_output
                )

    def test_04_ext_warning(self):
        """Test external warning interception."""

        msg = repr(self.msg)
        level = lib.logging.WARNING
        parsed = fqr.loggers.utl.parse_incoming_log_message(msg, level)
        with self.assertLogs(self.log, level) as logger:
            lib.warnings.warn(msg, stacklevel=1)
            expected_output = lib.textwrap.indent(
                lib.json.dumps(
                    parsed,
                    default=fqr.core.strings.utl.convert_for_repr,
                    indent=Constants.INDENT,
                    sort_keys=True
                    ),
                Constants.INDENT * ' '
                )
            self.assertEqual(
                logger.records[0].msg,
                expected_output
                )

    def test_05_invalid_log_type_exc(self):
        """Test correct exc is raised."""

        with self.assertNoLogs(self.log):
            self.assertRaises(
                fqr.loggers.exc.InvalidLogMessageTypeError,
                lambda: fqr.log.info(42)
                )

    def test_06_log_truncation(self):
        """Test long strings correctly truncated."""

        msg = {'longString': 'ABCDEFG' * 1024}
        level = lib.logging.CRITICAL
        with self.assertLogs(self.log, level) as logger:
            fqr.log.critical(msg)
            self.assertIn(
                fqr.core.strings.cfg.Constants.M_LINE_TOKEN,
                logger.records[0].msg
                )

    def test_07_log_redaction(self):
        """Test sensitive strings correctly redacted."""

        msg = {'apiKey': 'ABCDEFG'}
        level = lib.logging.INFO
        with self.assertLogs(self.log, level) as logger:
            fqr.log.info(msg)
            self.assertIn(
                '[ REDACTED :: API KEY ]',
                logger.records[0].msg
                )

    def tearDown(self) -> None:
        Constants.ENV = 'local'
        return super().tearDown()


class TestTracedLogger(unittest.TestCase):
    """Fixture for testing logger with tracing."""

    def setUp(self) -> None:
        Constants.LOG_TRACEBACK = True
        self.log = fqr.log
        self.msg_str = 'example'
        return super().setUp()

    def test_01_log(self):
        """Test exc logging."""

        msg = self.msg_str
        level = lib.logging.ERROR
        parsed = fqr.loggers.utl.parse_incoming_log_message(msg, level)
        with self.assertLogs(self.log, level) as logger:
            try:
                _ = 1 / 0
            except Exception:
                fqr.log.error(msg)
                parsed['traceback'] = lib.traceback.format_exc()
                expected_output = lib.textwrap.indent(
                    lib.json.dumps(
                        parsed,
                        default=fqr.core.strings.utl.convert_for_repr,
                        indent=Constants.INDENT,
                        sort_keys=True
                        ),
                    Constants.INDENT * ' '
                    )
            self.assertEqual(logger.records[0].msg, expected_output)

    def test_02_log(self):
        """Test exc logging - no trace for < ERROR."""

        msg = self.msg_str
        level = lib.logging.DEBUG
        parsed = fqr.loggers.utl.parse_incoming_log_message(msg, level)
        with self.assertLogs(self.log, level) as logger:
            try:
                _ = 1 / 0
            except Exception as e:
                self.log.info(msg, exc_info=e)
                expected_output = lib.textwrap.indent(
                    lib.json.dumps(
                        parsed,
                        default=fqr.core.strings.utl.convert_for_repr,
                        indent=Constants.INDENT,
                        sort_keys=True
                        ),
                    Constants.INDENT * ' '
                    )
            self.assertEqual(logger.records[0].msg, expected_output)

    def tearDown(self) -> None:
        Constants.LOG_TRACEBACK = False
        return super().tearDown()
