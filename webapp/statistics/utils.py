import json
from pathlib import Path
from backend.connectors.mongodb import MongoDbConnector
from backend.connectors.postgres_connector import PostgreSqlConnector
from backend.query_processors.mongodb_processor import MongoDbProcessor
from backend.query_processors.postgres_processor import PostgresProcessor


json_query_path = Path(__file__).resolve().parent.joinpath('..', '..', 'webapp', 'resources', 'queries.json')

def instantiate_processors():
    """
    Instantiates query processors for both types of databases
    """

    postgres_connector = PostgreSqlConnector()
    mongodb_connector = MongoDbConnector()

    postgres_processor = PostgresProcessor(postgres_connector)
    mongodb_processor = MongoDbProcessor(mongodb_connector)
    return postgres_processor, mongodb_processor


def manage_indices(create: bool):
    """
    Either creates or drops indices
    """

    query_name = "INDEXES"
    if not create:
        query_name = "DROP_INDEXES"

    with open(json_query_path) as queries:
        query_data = json.load(queries)

    postgres_processor, mongodb_processor = instantiate_processors()
    postgres_index_query = query_data["postgres"]["invoice_binary"][query_name]
    mongodb_index_query = query_data["mongo"][query_name]["queryType"]
    postgres_processor.run_query(postgres_index_query)
    mongodb_processor.run_query(mongodb_index_query, query_data["mongo"][query_name]["parameter"])
