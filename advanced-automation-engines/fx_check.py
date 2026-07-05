"""""
Task 1: The Global Currency Monitor
Goal: Create a script fx_check.py that fetches exchange rates and formats financial data.

Mechanic: Use requests.get to call a public exchange rate API (e.g., JSONPlaceholder for structure testing or a mock FX endpoint).

Requirements: 1. Pass a "base currency" via sys.argv[1].
2. Format the resulting float using f"{value:.2f}".
3. Use f"{value:,}" if the volume is over 1,000.
4. Handle a ValueError if the user provides a number instead of a currency code.
"""""

import requests
import sys

# 1. State: Ensure argument exists
if len(sys.argv) < 2:
    sys.exit("Usage: python fx_check.py [CURRENCY]")

currency = sys.argv[1].upper() # Normalize to uppercase

try:
    # 2. Logic: Check if it's a number OR wrong length
    if currency.isdigit() or len(currency) != 3:
        raise ValueError # THIS triggers the jump to 'except'

    # 3. Action: Request data
    response = requests.get("https://open.er-api.com/v6/latest/USD")
    response.raise_for_status() # Check if web service is alive
    
    data = response.json()
    
    # 4. Access: Find the rate for the user's currency
    # Note: We look up the 'currency' inside the 'USD' rates dictionary
    rate = data["rates"][currency]
    
    # 5. Result: Format with , and .2f
    print(f"{rate:,.2f}")

except ValueError:
    print("Error: Use a 3-letter currency code (e.g., EUR)")
    sys.exit(1)
except KeyError:
    print(f"Error: Currency '{currency}' not found.")
    sys.exit(1)