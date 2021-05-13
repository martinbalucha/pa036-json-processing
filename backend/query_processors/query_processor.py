from abc import ABC, abstractmethod
from configparser import ConfigParser
from pathlib import Path


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
        path = Path(__file__).resolve().parent.joinpath("..", "..", "config.ini")
        self.parser.read(path)

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
