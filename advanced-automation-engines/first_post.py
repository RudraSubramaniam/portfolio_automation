# #Practice: Problem 11 (The First Post Fetcher) --- The List-in-Dictionary Combo ---

import sys
import requests

source = "https://jsonplaceholder.typicode.com/users/"
source_2 = "/posts"
print(f"{"USER ID":<25}{"FIRST POST":<10}")
print("_" * 100)

id_entry = sys.argv[1:]

for entry in id_entry:
    if not entry.isdigit():
        
        print(f"{entry:<25} ERROR: Use Numbers Only")
        continue
    
    sucess = False
    for attempts in range(3):
        try:
            response = requests.get(source + entry + source_2)
            response.raise_for_status()
            data = response.json()
            
            if len(data) > 0:
                first_post = data[0]
                user_id = first_post["userId"]
                fp_title = first_post["title"]
                print(f"{user_id:<25}{fp_title:<10}")
                sucess = True
                break
 
            else:
                print("User has no posts.")
                    
        except Exception:
            continue
    if not sucess:
        print(f"{entry:<25} Failed after 3 tries")