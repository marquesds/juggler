from unittest import TestCase
from testfixtures import log_capture
from decorators.log import *
import logging


@logger(logging.INFO, 'my message', 'test')
def func():
    pass


class TestLog(TestCase):
    @log_capture()
    def test_logger(self, l):
        func()

        l.check(
            ('test', 'INFO', 'my message'),
        )
