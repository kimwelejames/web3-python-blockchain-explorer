from web3 import Web3


class EthereumExplorer:
    def __init__(self, rpc_url):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))

    def is_connected(self):
        return self.w3.is_connected()

    def latest_block(self):
        return self.w3.eth.block_number

    def chain_id(self):
        return self.w3.eth.chain_id

    def balance(self, wallet):
        balance = self.w3.eth.get_balance(wallet)
        return self.w3.from_wei(balance, "ether")

    def gas_price(self):
        return self.w3.from_wei(self.w3.eth.gas_price, "gwei")

    def nonce(self, wallet):
        return self.w3.eth.get_transaction_count(wallet)

    def latest_block_data(self):
        return self.w3.eth.get_block("latest")