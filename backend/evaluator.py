

class Evaluator:
    """
    Evaluates statistics
    """

    def __init__(self, postgres_processor, mongodb_processor):
        """
        Ctor
        :param postgres_processor: processor of PostgreSQL queries
        :param mongodb_processor: processor of MongoDB queries
        """

        self.postgres_processor = postgres_processor
        self.mongodb_processor = mongodb_processor

    def evaluate_statistics(self, invoice_count):
        """
        Evaluates statistics for both databases on the given number of invoices
        :param invoice_count: the number of invoices that will be processed
        :return: a result DTO holding times for query performances
        """

        # TODO: load given number of JSONs, load queries

