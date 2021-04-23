from abc import ABCMeta, abstractmethod


class ConnectorInterface(object):
    """
    An interface implementations of which are the backend scripts capable of connecting to the relevant databases
    """
    __metaclass__ = ABCMeta

    def __enter__(self):
        """
        Implementation of '__enter__' and '__exit__' methods allows resource to be used with 'with' statement.
        :return: 'this' resource instance
        """
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        """
        Implementation of '__enter__' and '__exit__' methods allows resource to be used with 'with' statement.
        :param exception_type: Optional type of an exception thrown during 'with' body execution
        :param exception_value: Optional instance of an exception thrown during 'with' body execution
        :param traceback: Optional traceback of an exception thrown during 'with' body execution
        """
        self.close()

    @abstractmethod
    def connector(self, host: str, port: int, username: str = None, password: str = None, **kwargs):
        """
        This method should be implemented while trying to create the connector to either MongoDB or PostgreSQL databases
        :param host: Database host address
        :param port: Database port number
        :param username: Username to be used for authentication
        :param password: Password to be used for authentication
        :return: Connector instance to the relevant database
        """
        pass
