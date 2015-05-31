import abc


class Service():
    __metaclass__ = abc.ABCMeta

    def __generate_id__(self):
        pass

    @abc.abstractmethod
    def get_all_tables(self):
        """
        :return:
        """

    @abc.abstractmethod
    def get_all_data(self):
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
