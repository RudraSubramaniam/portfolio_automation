"""""
The "Recursive Retry" (Looping Logic)

To try 3 times, you wrap the connection logic in a for loop. You use the break command to escape the loop only if the connection is successful.
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

import requests
import sys
import time

URL = "https://api.fake-automation.com/inventory"
TOKEN = "secret_token_123"
custom_headers = {"Authorization": f"Bearer {TOKEN}"}

# 1. The Retry Loop
# Logic: Try the code inside this block 3 times.
for attempt in range(3):
    print(f"Attempt {attempt + 1}...")
    
    try:
        response = requests.get(URL, headers=custom_headers)
        
        # 2. The Success Check
        if response.status_code == 200:
            data = response.json()
            print(f"Current Stock: {data['Item_77']} units")
            break  # EXIT the loop because we succeeded
            
    except requests.exceptions.RequestException:
        print("Network Error.")

    # 3. The Wait Mechanic
    # If the code reaches here, it means it didn't 'break' (failed).
    if attempt < 2:  # Don't wait after the very last try
        print("Retrying in 2 seconds...")
        time.sleep(2)
else:
    # 4. The Final Fault
    # This block runs ONLY if the loop finishes 3 times without a 'break'.
    print("Error: Server unavailable after 3 attempts.")
    sys.exit()