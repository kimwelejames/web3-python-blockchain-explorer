from flask import Blueprint, render_template
from app.ethereum import get_dashboard_data

main = Blueprint("main", __name__)


@main.route("/")
def index():

    data = get_dashboard_data()

    return render_template(
        "index.html",
        data=data
    )