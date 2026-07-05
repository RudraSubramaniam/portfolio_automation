import sys
import requests
import json # REQUIRED for the .loads mechanic

source = "https://dummyjson.com/carts/1"

try:
    response = requests.get(source)
    response.raise_for_status()
    data = response.json()
except:
    # Use the 's' for String parsing
    fallback = '{"products": [{"title": "Emergency Item", "discountPercentage": -10.0}]}'
    data = json.loads(fallback)

print("--- Inventory Audit ---")

# MECHANIC: Loop the list inside the "products" key
for item in data["products"]:
    name = item["title"]
    # Target the specific key inside the nested dictionary
    disc = item["discountPercentage"]
    
    # State: Using :+ to force the sign and .2f to limit decimals
    print(f"Item: {name} | Discount: {disc:+.2f}%")
    
    response.raise_for_status()