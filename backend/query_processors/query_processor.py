from abc import ABC, abstractmethod
from configparser import ConfigParser


class QueryProcessor(ABC):
    """
    An abstract class for query processors
    """

    @abstractmethod
    def __init__(self):
        """
        Ctor that reads the configuration file
        """

        self.parser = ConfigParser()
        self.parser.read("../config.ini")

    @abstractmethod
    def run_query(self, query, params=None, **kwargs) -> float:
        """
        Runs a query with given parameters
        :param query: a query to be run
        :param params: an optional parameter of query parameters
        :param kwargs: additional parameters
        :return: the run time of the query
        """

        raise NotImplementedError
