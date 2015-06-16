from unittest import TestCase
from core.providers import *


class TestCassandraProvider(TestCase):
    def test_connection(self):
        cassandra = CassandraProvider(host=['192.168.0.7'], port=9042, database='system')

    def test_close_connection(self):
        pass

    def test_show_tables(self):
        pass
