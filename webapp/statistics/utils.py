import json
import ijson
from pathlib import Path
from backend.connectors.mongodb import MongoDbConnector
from backend.connectors.postgres_connector import PostgreSqlConnector
from backend.dto.result_dto import ResultDto
from backend.query_processors.mongodb_processor import MongoDbProcessor
from backend.query_processors.postgres_processor import PostgresProcessor


def _load_queries():
    """
    Loads JSON queries
    :return: JSON queries
    """
    json_query_path = Path(__file__).resolve().parent.joinpath('..', '..', 'webapp', 'resources', 'queries_edited.json')
    with open(json_query_path) as query_file:
        return json.load(query_file)


def instantiate_processors() -> tuple:
    """
    Instantiates query processors for both types of databases
    :return: a tuple of format (PostgresProcessor, MongoDbProcessor)
    """

    postgres_connector = PostgreSqlConnector()
    mongodb_connector = MongoDbConnector()

    postgres_processor = PostgresProcessor(postgres_connector)
    mongodb_processor = MongoDbProcessor(mongodb_connector)
    return postgres_processor, mongodb_processor


def manage_indices(create: bool) -> None:
    """
    Either creates or drops index, depending on the create parameter
    :param create: If it is true, the indexes are creates, otherwise they are dropepd
    """

    operation = "INDEX"
    if not create:
        operation = "DROP_INDEX"

    query_data = _load_queries()
    postgres_processor, mongodb_processor = instantiate_processors()
    index_queries = query_data[operation]
    postgres_processor.run_query(index_queries["postgres_binary"])
    mongodb_processor.run_query(index_queries["mongodb"], index_queries["filter"])


def run_queries(number_of_invoices: int) -> list:
    """
    Runs all queries, records run times and outputs the list of
    DTOs with times
    :param number_of_invoices: the number of invoices that will be processed
    :return: a list with results for each query
    """

    json_array_loaded = load_json_array(number_of_invoices)
    results = []
    postgres_processor, mongodb_processor = instantiate_processors()
    queries = _load_queries()["queries"]

    for query in queries:
        if query["description"] == "Insert":
            results.append(_run_inserts(postgres_processor, mongodb_processor, query, json_array_loaded))
            continue

        postgres_time = postgres_processor.run_query(query["postgres"])
        postgres_binary_time = postgres_processor.run_query(query["postgres_binary"])
        mongodb_time = mongodb_processor.run_query(query["mongodb"], query["filter"], query_json=query)
        result = ResultDto(query["description"], postgres_time, postgres_binary_time, mongodb_time)
        results.append(result)

    return results


def load_json_array(number_of_rows: int):
    """
    Selects the number of invoices from the JSON file
    :param number_of_rows: Number of rows
    :return: Loaded json array
    """
    data_path = Path(__file__).resolve().parent.joinpath('..', '..', 'webapp', 'data', 'fake_invoices.json')
    with open(data_path, encoding='utf-8') as f:
        items = ijson.items(f, "item")
        counter = 0
        json_array = []
        for item in items:
            json_array.append(item)
            if counter == number_of_rows - 1:
                break
            counter += 1
        return json_array


def run_deletes() -> None:
    """
    Deletes data from all tables
    """

    query_data = _load_queries()
    postgres_processor, mongodb_processor = instantiate_processors()
    delete_queries = query_data["DELETE"]
    postgres_processor.run_query(delete_queries["postgres"])
    postgres_processor.run_query(delete_queries["postgres_binary"])
    mongodb_processor.run_query(delete_queries["mongodb"], "{}")


def _run_inserts(postgres_processor: PostgresProcessor, mongodb_processor: MongoDbProcessor, query: dict,
                 data) -> ResultDto:
    """
    Runs insert on the given data. Returns results for the inserts
    Has to be separated because input data have to be in the different formats
    :param postgres_processor: postgres processor for queries
    :param mongodb_processor: mongodb processor for queries
    :param query: a query to be executed
    :param data: data which will be inserted
    :return: result dto
    """

    postgres_parameters = tuple([[json.dumps(item, ensure_ascii=False)] for item in data],)
    postgres_time = postgres_processor.run_query(query["postgres"], postgres_parameters, is_insert=True)
    postgres_binary_time = postgres_processor.run_query(query["postgres_binary"], postgres_parameters, is_insert=True)
    mongodb_time = mongodb_processor.run_query(query["mongodb"], data)
    return ResultDto(query["description"], postgres_time, postgres_binary_time, mongodb_time)
