from web3 import Web3
from app.config import RPC_URL, WALLET_ADDRESS

w3 = Web3(Web3.HTTPProvider(RPC_URL))


def get_dashboard_data():

    chain_id = w3.eth.chain_id

    latest_block = w3.eth.block_number

    balance = w3.from_wei(
        w3.eth.get_balance(WALLET_ADDRESS),
        "ether"
    )

    tx_count = w3.eth.get_transaction_count(WALLET_ADDRESS)

    gas_price = w3.from_wei(
        w3.eth.gas_price,
        "gwei"
    )

    return {
        "chain_id": chain_id,
        "latest_block": latest_block,
        "wallet": WALLET_ADDRESS,
        "balance": balance,
        "tx_count": tx_count,
        "gas_price": round(float(gas_price), 3)
    }