
from pathlib import Path
from flask import Blueprint, render_template, flash, redirect, url_for, request
from backend.dto.result_dto import ResultDto
from webapp.statistics.utils import instantiate_processors, manage_indices

statistics = Blueprint("statistics", __name__)

json_path = Path(__file__).resolve().parent.joinpath('..', '..', 'webapp', 'data', 'invoice_example.json')


@statistics.route("/statistics", methods=["GET", "POST"])
def display_statistics():
    if request.method == "POST":
        invoice_count = request.form.get("invoice_count")
        postgres_processor, mongodb_processor = instantiate_processors()
        queries = []  # TODO: load queries
        results = []
        for query in queries:
            postgres_binary_time = postgres_processor.run_query(query)
            postgres_time = postgres_processor.run_query(query)
            mongodb_time = mongodb_processor.run_query(query)

            query_type = ""
            result = ResultDto(query_type, postgres_time, postgres_binary_time, mongodb_time)
            results.append(result)
        return render_template("statistics.html", statistics=results)

    return render_template("statistics.html")


@statistics.route("/create_indices", methods=["GET"])
def create_indices():
    manage_indices(True)
    flash("Indices successfully established!", "success")
    return redirect(url_for("statistics.display_statistics"))


@statistics.route("/drop_indices")
def drop_indices():
    manage_indices(False)
    flash("Indices successfully dropped!", "success")
    return redirect(url_for("statistics.display_statistics"))
