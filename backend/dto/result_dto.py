

class ResultDto:
    """
    Data transfer object for run times of queries
    """

    def __init__(self, query_type, postgres_json_time, postgres_jsonb_time, mongodb_time):
        """
        Ctor
        :param query_type: Type of the query
        :param postgres_json_time: Run time of the PostgreSQL json processing
        :param postgres_jsonb_time: Run time of the PostgreSQL jsonb processing
        :param mongodb_time: Run time of the MongoDB json processing
        """

        self.query_type = query_type
        self.postgres_json_time = postgres_json_time
        self.postgres_jsonb_time = postgres_jsonb_time
        self.mongodb_time = mongodb_time
