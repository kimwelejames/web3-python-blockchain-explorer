from flask import Blueprint, render_template, request
from app.portfolio import calculate_portfolio_stats
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
    transactions = []

    # Dashboard stats
    token_count = 0
    total_token_balance = 0
    active_tokens = 0

    # Network stats
    eth_price = get_eth_price()
    gas_price = get_gas_price()
    latest_block = get_latest_block()
    status = network_status()
    stats = {"token_count": 0, "active_tokens": 0, "total_token_balance": 0, "portfolio_value": 0}

    if request.method == "POST":

        wallet = request.form["wallet"]

        dashboard = get_dashboard_data(wallet)

        portfolio = get_portfolio(wallet)

        raw = get_asset_transfers(wallet)

        transactions = format_transactions(raw)

        eth_balance = dashboard["balance"]

        stats = calculate_portfolio_stats(
            portfolio,
            eth_balance,
            eth_price
        )

    return render_template(
        "index.html",
        wallet=wallet,
        eth_balance=eth_balance,
        portfolio=portfolio,
        transactions=transactions,
        eth_price=eth_price,
        gas_price=gas_price,
        latest_block=latest_block,
        status=status,

        token_count=stats["token_count"],
        active_tokens=stats["active_tokens"],
        total_token_balance=stats["total_token_balance"],
        portfolio_value=stats["portfolio_value"],
    )