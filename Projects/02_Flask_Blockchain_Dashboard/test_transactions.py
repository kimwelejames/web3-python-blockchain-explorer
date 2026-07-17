print("Starting test...")

from app.transactions import get_transactions

wallet = "0xc626831299F5ad837fd0E4c928C34cb5739bB859"

print("Fetching...")

txs = get_transactions(wallet)

print("Result:")
print(txs)

print("Finished")