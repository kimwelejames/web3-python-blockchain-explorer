from web3 import Web3
from app.config import RPC_URL


w3 = Web3(Web3.HTTPProvider(RPC_URL))


TOKENS = {
    "LINK": "0x779877A7B0D9E8603169DdbD7836e478b4624789",
    "USDC": "0x1c7D4B196Cb0C7B01d743Fbc6116a902379C7238",
    "DAI":  "0x776b6fc2ed15d6bb5fc32e0c89de68683118c62a",
}

ERC20_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "", "type": "uint256"}],
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "symbol",
        "outputs": [{"name": "", "type": "string"}],
        "type": "function",
    },
]


def get_contract(token_address):
    return w3.eth.contract(
        address=Web3.to_checksum_address(token_address),
        abi=ERC20_ABI
    )


def get_symbol(token_address):
    contract = get_contract(token_address)
    return contract.functions.symbol().call()

def get_decimals(token_address):
    contract = get_contract(token_address)
    return contract.functions.decimals().call()


def get_balance(token_address, wallet):
    contract = get_contract(token_address)

    balance = contract.functions.balanceOf(
        Web3.to_checksum_address(wallet)
    ).call()

    decimals = get_decimals(token_address)

    return balance / (10 ** decimals)

def get_token_info(token_address, wallet):
    return {
        "symbol": get_symbol(token_address),
        "decimals": get_decimals(token_address),
        "balance": get_balance(token_address, wallet),
    }


def get_portfolio(wallet):
    portfolio = []

    for name, address in TOKENS.items():
        portfolio.append(
            get_token_info(address, wallet)
        )

    return portfolio
