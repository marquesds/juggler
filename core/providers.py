import abc
import logging
from cassandra.cluster import Cluster, NoHostAvailable
from cassandra.auth import PlainTextAuthProvider


class Provider():
    __metaclass__ = abc.ABCMeta

    def __init__(self, host, port, database, user=None, password=None):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
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
    def __connect__(self):
        try:
            if self.user == None or self.password == None:
                self.auth = PlainTextAuthProvider(username=self.user, password=self.password)
            self.cluster = Cluster(contact_points=self.host, port=self.port, auth_provider=self.auth)
            self.cassandra = self.cluster.connect(self.database)
        except NoHostAvailable as ex:
            print(ex)

    def close(self):
        self.cluster.shutdown()
        self.cassandra.shutdown()

    def show_tables(self):
        return list(self.cluster.metadata.keyspaces[self.database].tables.keys())


class ElasticSearchProvider(Provider):
    def __connect__(self):
        pass

    def close(self):
        pass

    def show_tables(self):
        pass


class MySQLProvider(Provider):
    def __connect__(self):
        pass

    def close(self):
        pass

    def show_tables(self):
        pass
