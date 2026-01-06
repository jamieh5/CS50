from config import api_key
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
try:
    response = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}")
    o = response.json()
    price = float(o["data"]["priceUsd"])
    print(f"${price * bitcoins:,.4f}")
except requests.RequestException:
    sys.exit()
