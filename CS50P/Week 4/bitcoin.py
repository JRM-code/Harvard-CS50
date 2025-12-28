import json
import requests
import sys

try:
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    else:
        sys.argv[1] = float(sys.argv[1])

except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=b89b2dc84825e4b83eff9217d69447bbbc241788c48dccf5ea1ea8e186ccfd8a")
except requests.RequestException:
    sys.exit()

object = response.json()

price = float(object["data"]["priceUsd"])
value = price * sys.argv[1]
print(f"${value:,.4f}")
