import requests

from app.config import ALCHEMY_API_KEY

BASE_URL = f"https://eth-sepolia.g.alchemy.com/v2/{ALCHEMY_API_KEY}"


def get_asset_transfers(wallet):

    incoming_payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "alchemy_getAssetTransfers",
        "params": [{
            "fromBlock": "0x0",
            "toBlock": "latest",
            "toAddress": wallet,
            "category": [
                "external",
                "erc20"
            ],
            "withMetadata": True,
            "excludeZeroValue": True,
            "maxCount": "0xA"
        }]
    }

    outgoing_payload = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "alchemy_getAssetTransfers",
        "params": [{
            "fromBlock": "0x0",
            "toBlock": "latest",
            "fromAddress": wallet,
            "category": [
                "external",
                "erc20"
            ],
            "withMetadata": True,
            "excludeZeroValue": True,
            "maxCount": "0xA"
        }]
    }

    incoming = requests.post(BASE_URL, json=incoming_payload).json()
    outgoing = requests.post(BASE_URL, json=outgoing_payload).json()

    return {
        "incoming": incoming["result"]["transfers"],
        "outgoing": outgoing["result"]["transfers"]
    }


def format_transactions(data):

    transactions = []

    for tx in data["incoming"]:
        transactions.append({
            "time": tx["metadata"]["blockTimestamp"],
            "type": "Received",
            "asset": tx["asset"],
            "amount": tx["value"],
            "hash": tx["hash"]
        })

    for tx in data["outgoing"]:
        transactions.append({
            "time": tx["metadata"]["blockTimestamp"],
            "type": "Sent",
            "asset": tx["asset"],
            "amount": tx["value"],
            "hash": tx["hash"]
        })

    transactions.sort(
        key=lambda x: x["time"],
        reverse=True
    )

    return transactions

