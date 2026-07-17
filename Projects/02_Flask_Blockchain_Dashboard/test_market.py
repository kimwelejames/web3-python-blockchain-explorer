from app.market import *

print("ETH Price (USD):", get_eth_price())
print("Gas Price:", get_gas_price(), "Gwei")
print("Block:", get_latest_block())
print("Status:", network_status())