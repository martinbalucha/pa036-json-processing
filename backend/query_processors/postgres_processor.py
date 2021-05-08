from time import time
from backend.query_processors.query_processor import QueryProcessor


class PostgresProcessor(QueryProcessor):
    """
    An implementation of the QueryProcessor
    """

    def __init__(self, connector):
        """
        Ctor
        :param connector: DB connector
        """

        super().__init__()
        self.connector = connector

    def run_query(self, query, params=None):
        host = self.parser.get("postgres", "host")
        database = self.parser.get("postgres", "database")
        port = self.parser.get("postgres", "port")
        username = self.parser.get("postgres", "username")
        password = self.parser.get("postgres", "password")

        with self.connector.connector(host, port, username, password, db_name=database) as connection:

            with connection.cursor() as cursor:
                start_time = time()
                cursor.execute(query, params)
                end_time = time()
                return end_time - start_time
