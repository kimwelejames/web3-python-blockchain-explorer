from web3 import Web3
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

rpc_url = os.getenv("RPC_URL")
wallet = os.getenv("WALLET_ADDRESS")

w3 = Web3(Web3.HTTPProvider(rpc_url))

print("=" * 60)
print("🚀 WEB3 BOOTCAMP")
print("Ethereum Wallet Explorer")
print("=" * 60)

print("Date :", datetime.now().strftime("%Y-%m-%d"))
print("Time :", datetime.now().strftime("%H:%M:%S"))
print()

print("✅ Connected to Ethereum\n")

print(f"Chain ID          : {w3.eth.chain_id}")
print(f"Latest Block      : {w3.eth.block_number}")

balance = w3.eth.get_balance(wallet)
eth_balance = w3.from_wei(balance, "ether")

print(f"Wallet Address    : {wallet}")
print(f"Balance           : {eth_balance} ETH")

nonce = w3.eth.get_transaction_count(wallet)
print(f"Transaction Count : {nonce}")

gas_price = w3.eth.gas_price
gas_gwei = w3.from_wei(gas_price, "gwei")

print(f"Gas Price         : {gas_gwei} Gwei")

latest_block = w3.eth.get_block("latest")

block_time = datetime.fromtimestamp(latest_block.timestamp)

print(f"Block Timestamp   : {block_time}")