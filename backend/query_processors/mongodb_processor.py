import json
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

    def run_query(self, query, params=None, **kwargs) -> float:
        query = str.lower(query)

        host = self.parser.get("mongodb", "host")
        database = self.parser.get("mongodb", "database")
        port = int(self.parser.get("mongodb", "port"))

        connection = self.connector.connector(host, port)
        database = connection[database]
        table = database["invoice"]

        if query == "find":
            count = False
            if kwargs.get("query_json") is not None:
                count = kwargs.get("query_json")["count"]
            params = json.loads(params)
            return self._run_find(table, params, count)
        elif query == "update_many":
            update = json.loads(kwargs.get("query_json")["update"])
            params = json.loads(params)
            return self._run_update(table, update, params)

        operation = getattr(table, query)
        if operation is None:
            raise ValueError(f"Mongo Client does not provide method {query}")

        if params is not None and query not in ["insert_many", "create_index"]:
            params = json.loads(params)

        start_time = time()
        operation(params)
        end_time = time()
        return end_time - start_time

    def _run_find(self, table, parameters, count=False) -> float:
        """
        Runs find command
        :param table: the table on which the query will run
        :param parameters: find condition
        :param count: optional parameter denoting that the count function should be used
        :return: run time of the find query
        """

        if count:
            start_time = time()
            table.find(parameters).count()
            end_time = time()
            return end_time - start_time

        start_time = time()
        result = table.find(parameters)
        end_time = time()
        return end_time - start_time

    def _run_update(self, table, update, condition) -> float:
        """
        Runs update_many command
        :param table: the table on which the query will run
        :return: Run time of the update_many operation
        """

        start_time = time()
        table.update_many(condition, update)
        end_time = time()
        return end_time - start_time
