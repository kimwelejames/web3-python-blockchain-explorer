from web3 import Web3

from app.ethereum import w3


def get_transactions(address, limit=10):
    """
    Returns latest transactions involving this wallet.
    NOTE:
    Ethereum RPC cannot search history directly.
    We inspect recent blocks for demo purposes.
    """

    address = Web3.to_checksum_address(address)

    latest = w3.eth.block_number

    txs = []

    for block_number in range(latest, latest - 250, -1):

        block = w3.eth.get_block(block_number, full_transactions=True)

        for tx in block.transactions:

            sender = tx["from"]

            receiver = tx["to"]

            if sender == address or receiver == address:

                txs.append({

                    "hash": tx["hash"].hex(),

                    "from": sender,

                    "to": receiver,

                    "value": w3.from_wei(tx["value"], "ether"),

                    "block": block_number,

                })

                if len(txs) >= limit:
                    return txs

    return txs