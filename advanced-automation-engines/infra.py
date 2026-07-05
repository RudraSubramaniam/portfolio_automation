import requests
import sys
import json


server_record = "https://jsonplaceholder.typicode.com/posts/1"

payload = {sys.argv[1]: sys.argv[2]}


json_output = json.dumps(payload, indent=2)
print("--- Request Sent ---")
print(json_output)


response = requests.patch(server_record, json=payload)


print("\n--- Server Response ---")
print(f"Status updated to: {response.json()[sys.argv[1]]}")