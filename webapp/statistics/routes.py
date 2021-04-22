from flask import Blueprint, render_template

statistics = Blueprint("statistics", __name__)


@statistics.route("/statistics")
def launch_statistics():
    return render_template("statistics.html")
