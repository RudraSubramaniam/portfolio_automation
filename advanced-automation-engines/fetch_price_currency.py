"""""
Input: Run via terminal: python script.py data_log.json
Goal: Fetch (BTC) current price data. Clean the "disclaimer" string by splitting it at the first period and stripping whitespace. Map the currency codes (USD, GBP, EUR) to a Python Enum. 
Use json.dump to save a dictionary containing the cleaned disclaimer, the current timestamp, 
and the prices into the filename provided in sys.argv[1]. Format the terminal output with padding and sign indicators (even if positive).
"""""
import sys
import requests
import json
from enum import Enum

class Currencies(Enum):
    EUR = "EUR"
    GBP = "GBP"
    USD = "USD"

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
file_name = sys.argv[1]

response = requests.get(url)
raw_data = response.json()

raw_disclaimer = raw_data["disclaimer"]
cleaned_disclaimer = key_data.strip()
cleaned_disclaimer = key_data.split("Bitcoin ")[0].strip()

print(f"Cleaned Disclaimer: {cleaned_disclaimer}\nLog saved to: {file_name}\n")
print(f"{'Currency':<15} | {'Price':<10}")
print(f"{'-'*15}|{'-'*11}")

print()

for c in Currencies:
    price = raw_data["bpi"][c.value]["rate_float"]
    print(f"{c.name:<15} | {price:+10.2f}")


with open(file_name, "w") as f:
    json.dump(raw_data, f)