from flask import Blueprint, render_template, flash, redirect, url_for
from backend.connectors.mongodb import MongoDbConnector
from backend.connectors.postgres_connector import PostgreSqlConnector
from backend.query_processors.mongodb_processor import MongoDbProcessor
from backend.query_processors.postgres_processor import PostgresProcessor

statistics = Blueprint("statistics", __name__)


@statistics.route("/statistics/<count>")
def launch_statistics(count):
    if count not in ["10k", "100k", "1mil"]:
        flash("Allowed invoice numbers are only 10k, 100k and 1mil")
        return redirect(url_for("statistics.display_statistics"))

    postgres_connector = PostgreSqlConnector()
    mongodb_connector = MongoDbConnector()

    postgres_processor = PostgresProcessor()
    mongodb_processor = MongoDbProcessor()

@statistics.route("/statistics")
def display_statistics():
    return render_template("statistics.html")
