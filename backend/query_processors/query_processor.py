

class QueryProcessor:
    """
    An interface for query processors
    """

    def run_query(self, query, params=None):
        """
        Runs a query with given parameters
        :param query: a query to be run
        :param params: an optional parameter of query parameters
        """

        raise NotImplementedError
