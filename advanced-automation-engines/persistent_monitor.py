"""""
Goal: Create a persistent monitor using a while True loop that attempts to PATCH the resource every 5 seconds. You must use a try/except block to catch connection errors. Each cycle must timestamp the attempt. The loop should break only after 3 successful updates are confirmed by a 200 status code.
Desired Output:
"""""


import sys
import requests
import datetime
from datetime import datetime
url = "https://jsonplaceholder.typicode.com/posts/1"

payload = {"title": sys.argv[1], "body": sys.argv[2]}
success_count = 0

while True:
    try:
        response = requests.patch(url, json=payload)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if response.status_code == 200:
            success_count =+ 1
            print(f"[{now}] Attempt {success_count}: Success. Status 200")
            
            if success_count > 3:
                print("Target reached. Terminating agent.")
                break
        time.sleep(5)
        
    except Exception as e:
        print(f"Connection Error: {e}")
        time.sleep(5)
        continue
