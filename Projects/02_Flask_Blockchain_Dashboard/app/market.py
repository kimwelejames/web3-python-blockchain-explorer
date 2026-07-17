import requests
from app.ethereum import w3
def get_eth_price():
    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": "ethereum",
        "vs_currencies": "usd"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        return data["ethereum"]["usd"]

    except Exception:
        return None


def get_gas_price():

        gas = w3.eth.gas_price

        return round(w3.from_wei(gas, "gwei"), 2)


def get_latest_block():

    return w3.eth.block_number


def network_status():

    return "Connected" if w3.is_connected() else "Disconnected"