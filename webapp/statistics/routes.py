from flask import Blueprint, render_template, flash, redirect, url_for
from backend.connectors.mongodb import MongoDbConnector
from backend.connectors.postgres_connector import PostgreSqlConnector
from backend.query_processors.mongodb_processor import MongoDbProcessor
from backend.query_processors.postgres_processor import PostgresProcessor

statistics = Blueprint("statistics", __name__)


@statistics.route("/statistics")
def display_statistics():
    return render_template("statistics.html")


@statistics.route("/create_indices", methods=["GET"])
def create_indices():
    postgres_processor, mongodb_processor = _instantiate_processors()
    # TODO: load index query
    postgres_index_query = ""
    mongodb_index_query = ""
    postgres_processor.run_query(postgres_index_query)
    mongodb_processor.run_query(mongodb_index_query)
    flash("Indices successfully established!", "success")
    return redirect(url_for("statistics.display_statistics"))


@statistics.route("/drop_indices")
def drop_indices():
    pass


def _instantiate_processors():
    """
    Instantiates query processors for both types of databases
    """

    postgres_connector = PostgreSqlConnector()
    mongodb_connector = MongoDbConnector()

    postgres_processor = PostgresProcessor(postgres_connector)
    mongodb_processor = MongoDbProcessor(mongodb_connector)
    return postgres_processor, mongodb_processor
