#Persistent Agent (Data Update Agent)
"""""
run the script, you provide it with two "tools": a New Title and a Timer. The agent takes these and prepares to talk to a specific server (the "Source" URL).
Input: python script.py "COMPLETED" 5

Goal: Create a persistent agent using a while True loop that performs a PUT request to update the entire resource. The first argument sets the new "title," and the second argument
is a delay in seconds. Use json.dumps() to prepare the payload. The agent must use time.sleep() for rate limiting and datetime for logging. 
Implement a try/except block to handle potential request failures. Stop the loop once 5 successful cycles are completed.

"""""
import sys
import requests
import json
import time
from datetime import datetime

Source =  "https://jsonplaceholder.typicode.com/todos/1"
status_payload = {"userId": 1, "id": 1, "title": sys.argv[1], "completed": True}
timer_payload = int(sys.argv[2])
success_count = 0

while True:
    try:
        json_string = json.dumps(status_payload)
        payload_size = len(json_string)
        response = requests.put(Source, data=json_string)        
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if response.status_code == 200:
            success_count += 1
            print(f"[{now}] PUT Request Sent | Status: {response.status_code} | Payload Size:{payload_size}")
            
            if success_count == 5:
                print("Cycle limit reached. Agent exiting.")
                break
            
        time.sleep(timer_payload)
        
    except Exception as e:
        print(f"Connection Error: {e}")
    time.sleep(timer_payload)
        
