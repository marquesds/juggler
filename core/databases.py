import abc


class Provider():
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.__connect__()

    @abc.abstractmethod
    def __connect__(self):
        """
        :return:
        """

    @abc.abstractmethod
    def close(self):
        """
        :return:
        """

    @abc.abstractmethod
    def show_tables(self):
        """
        :return:
        """


class CassandraProvider(Provider):
    pass


class ElasticSearchProvider(Provider):
    pass


class MySQLProvider(Provider):
    pass
