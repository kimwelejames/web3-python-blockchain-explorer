from pprint import pprint

from app.alchemy import (
    get_asset_transfers,
    format_transactions
)

from app.config import WALLET_ADDRESS

data = get_asset_transfers(WALLET_ADDRESS)

transactions = format_transactions(data)

pprint(transactions)