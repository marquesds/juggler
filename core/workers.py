import abc


class Worker():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def syncronize(self):
        """
        :return:
        """

    @abc.abstractmethod
    def is_updated(self):
        """
        :return:
        """


class CassandraWorker(Worker):
    pass


class ElasticSearchWorker(Worker):
    pass


class MySQLWorker(Worker):
    pass
