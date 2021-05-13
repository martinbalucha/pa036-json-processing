from flask import Blueprint, render_template, flash, redirect, url_for, request
from webapp.statistics.utils import manage_indices, run_queries, run_deletes

statistics = Blueprint("statistics", __name__)


@statistics.route("/delete_all")
def delete_all():
    run_deletes()
    flash("All records were successfully deleted", "success")
    return redirect(url_for("statistics.display_statistics"))


@statistics.route("/statistics", methods=["GET", "POST"])
def display_statistics():
    if request.method == "POST":
        invoice_count = int(request.form.get("invoice_count"))
        results = run_queries(invoice_count)
        return render_template("statistics.html", statistics=results)

    return render_template("statistics.html")


@statistics.route("/create_indices", methods=["GET"])
def create_indices():
    manage_indices(True)
    flash("Indices successfully created!", "success")
    return redirect(url_for("statistics.display_statistics"))


@statistics.route("/drop_indices")
def drop_indices():
    manage_indices(False)
    flash("Indices successfully dropped!", "success")
    return redirect(url_for("statistics.display_statistics"))
