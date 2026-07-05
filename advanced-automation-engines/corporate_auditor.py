"""""
The Corporate Data Auditor API
Clean a standardized report from a messy list of companies from a global database, save it into a specific file so it can read it later.

Goal: Fetch the user list. For each user, clean the company["name"] by splitting it at the period and stripping whitespace. Map the account status to a Python Enum 
(e.g., Status.ACTIVE). Use json.dump to save a list of dictionaries to the filename in sys.argv[1] containing the cleaned company name, 
the Enum value (as a string), and a UTC timestamp. Format the terminal output using f-string padding (:<20) and sign indicators (:+d) for the user IDs.

Input: python script.py audit_log.json
"""""
import sys
import requests
import json
from datetime import datetime, UTC
from enum import Enum

# 1. Define the Enum
class Status(Enum):
    ACTIVE = "ACTIVE"

# 2. Configuration
URL = "https://jsonplaceholder.typicode.com/users"
filename = sys.argv[1]
cleaned_data = []

try:
    # Fetch data
    response = requests.get(URL)
    users = response.json()

    # 3. Process Data first to get the count
    for user in users:
        # Clean company name
        clean_name = user["company"]["name"].split(".")[0].strip()
        
        # Modern UTC Timestamp
        timestamp = datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S")

        # Assemble dictionary
        entry = {
            "user_id": user["id"],
            "company": clean_name,
            "status": Status.ACTIVE.name,
            "timestamp": timestamp
        }
        cleaned_data.append(entry)

    # 4. Final Output Display
    print(f"Cleaned {len(cleaned_data)} records.")
    print(f"File saved to: {filename}\n")

    print(f"{'User ID':<10} | {'Company':<20}")
    print("-" * 35)

    for entry in cleaned_data:
        # Mechanics: < (Left Align), + (Show Sign), 10 (Width), d (Integer)
        print(f"{entry['user_id']:<+10d} | {entry['company']:<20}")

    # 5. Save to File
    with open(filename, "w") as f:
        json.dump(cleaned_data, f, indent=4)

except Exception as e:
    print(f"Connection Error: {e}")