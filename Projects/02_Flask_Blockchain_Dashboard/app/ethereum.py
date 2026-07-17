from web3 import Web3
from app.config import RPC_URL
from datetime import datetime

w3 = Web3(Web3.HTTPProvider(RPC_URL))


def get_dashboard_data(wallet_address):

    chain_id = w3.eth.chain_id

    latest_block = w3.eth.block_number

    latest_block_data = w3.eth.get_block("latest")

    block_time = datetime.fromtimestamp(
        latest_block_data.timestamp
    ).strftime("%Y-%m-%d %H:%M:%S")

    balance = w3.from_wei(
        w3.eth.get_balance(wallet_address),
        "ether"
    )

    tx_count = w3.eth.get_transaction_count(wallet_address)

    gas_price = w3.from_wei(
        w3.eth.gas_price,
        "gwei"
    )

    return {
        "chain_id": chain_id,
        "latest_block": latest_block,
        "balance": balance,
        "wallet": wallet_address,
        "tx_count": tx_count,
        "gas_price": gas_price,
        "block_time": block_time,
    }

def get_eth_balance(wallet_address):
    return float(
        w3.from_wei(
            w3.eth.get_balance(wallet_address),
            "ether"
        )
    )