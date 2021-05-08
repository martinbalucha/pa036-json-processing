from query_processor import QueryProcessor
from time import time


class PostgresProcessor(QueryProcessor):
    """
    An implementation of the QueryProcessor
    """

    def __init__(self, connector):
        """
        Ctor
        :param connector: DB connector
        """

        self.connector = connector

    def run_query(self, query, params=None):
        with self.connector.connector() as connection:
            with connection.cursor() as cursor:
                start_time = time()
                cursor.execute(query, params)
                end_time = time()
                return end_time - start_time
