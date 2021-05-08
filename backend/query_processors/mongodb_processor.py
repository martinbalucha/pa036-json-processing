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

        self.connector = connector
        self.database = connector[""]
        self.table = self.database["invoice"]

    def run_query(self, query, params=None):
        query = str.lower(query)
        operation = getattr(self.table, query)

        if operation is None:
            raise ValueError(f"Mongo Client does not provide method {query}")

        start_time = time()
        operation(params)
        end_time = time()
        return end_time - start_time
