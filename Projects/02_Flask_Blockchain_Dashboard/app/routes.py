from flask import Blueprint, render_template, request


from app.erc20 import get_portfolio
from app.alchemy import (get_asset_transfers, format_transactions)
from app.ethereum import get_dashboard_data
from app.market import (get_eth_price, get_gas_price, get_latest_block, network_status)

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def index():

    wallet = None
    eth_balance = None
    portfolio = []
    eth_price = get_eth_price()
    gas_price = get_gas_price()
    latest_block = get_latest_block()
    status = network_status()
    transactions = []


    if request.method == "POST":

        wallet = request.form["wallet"]

        dashboard = get_dashboard_data(wallet)

        portfolio = get_portfolio(wallet)

        raw = get_asset_transfers(wallet)

        transactions = format_transactions(raw)

        eth_balance = dashboard["balance"]

    return render_template(
        "index.html",
        wallet=wallet,
        eth_balance=eth_balance,
        portfolio=portfolio,
        transactions=transactions,

        eth_price=eth_price,
        gas_price=gas_price,
        latest_block=latest_block,
        status=status
    )