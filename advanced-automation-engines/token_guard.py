
"""""
Problem 5: The "Bearer Token Guard" (Authentication)
Client Request: "I have a private inventory API. I need a script that connects to it, but it requires a Security Token. If I don't provide the token in the Header, the server rejects me. I need to pull the current stock level for 'Item_77' and print it."

Source: https://api.fake-automation.com/inventory
Skill: Using the headers={} parameter in requests.get().
Logic: Passing a Key-Value pair (Authorization) to prove identity.
Input: * URL: https://api.fake-automation.com/inventory
Token: "secret_token_123"
Output: | Input (Key) | Output (Print Statement) |
| :--- | :--- |
| stock_count | Current Stock: 45 units |
"""""
import sys
import requests

url = "https://api.fake-automation.com/inventory"
token = "secret_token_123"

# Mechanic: The ID card for the server
custom_headers = {
    "Authorization": f"Bearer {token}"
}

# Mechanic: The Handshake
response = requests.get(url, headers=custom_headers)

# 1. THE SAFETY GATE
if response.status_code != 200:
    print(f"Access Denied. Status: {response.status_code}")
    sys.exit()

# 2. THE DATA EXTRACTION (Only happens if status is 200)
data = response.json()
stock = data["Item_77"]

# 3. THE DISPLAY LOGIC
input_key = "Item_77"
output_value = f"Current Stock: {stock} units"

print(f"| {'Input (Key)':<15} | {'Output (Print Statement)':<30} |")
print(f"| {'-'*15} | {'-'*30} |")
print(f"| {input_key:<15} | {output_value:<30} |")


