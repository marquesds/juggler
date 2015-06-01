import abc
import uuid
import logging
from decorators import log


class Service():
    __metaclass__ = abc.ABCMeta

    def __init__(self, table):
        self.table = table

    @log.logger(logging.DEBUG, "Generating uuid", "generate_uuid")
    def __generate_uuid__(self):
        return str(uuid.uuid4())

    @abc.abstractmethod
    def __create_id_column__(self):
        """
        :return:
        """

    @abc.abstractmethod
    def list(self):
        """
        :return:
        """

    @abc.abstractmethod
    def save(self):
        """
        :return:
        """

    @abc.abstractmethod
    def delete(self):
        """
        :return:
        """


class CassandraService(Service):
    pass


class ElasticSearchService(Service):
    pass


class MySQLService(Service):
    pass
