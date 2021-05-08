from time import time
from backend.query_processors.query_processor import QueryProcessor


class MongoDbProcessor(QueryProcessor):
    """
    Implementation of the QueryProcessor interface
    """

    def __init__(self, connector):
        """
        Ctor
        :param connector: DB connector
        """

        super().__init__()
        self.connector = connector

    def run_query(self, query, params=None):
        query = str.lower(query)

        host = self.parser.get("mongodb", "host")
        database = self.parser.get("mongodb", "database")
        port = int(self.parser.get("mongodb", "port"))

        connection = self.connector.connector(host, port)
        database = connection[database]
        table = database["invoice"]
        operation = getattr(table, query)

        if operation is None:
            raise ValueError(f"Mongo Client does not provide method {query}")

        start_time = time()
        operation(params)
        end_time = time()
        return end_time - start_time
