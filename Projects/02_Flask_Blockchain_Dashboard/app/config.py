import os
from dotenv import load_dotenv

load_dotenv()

RPC_URL = os.getenv("RPC_URL")
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")
ALCHEMY_API_KEY = os.getenv("ALCHEMY_API_KEY")