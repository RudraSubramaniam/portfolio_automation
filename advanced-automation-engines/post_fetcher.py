#Practice: Problem 10 (The Post Fetcher)

import sys
import requests

source = "https://jsonplaceholder.typicode.com/posts/"

print(f"{"Title":<25}{"Body":<10}")
print("_" * 35)
post = sys.argv[1:]

for pst in post:
    if not pst.isdigit():
        print(f"{pst:<25} ERROR: Use Numbers Only")
        continue
    
    sucess = False
    for attempts in range(3):
        try:
            response = requests.get(source + pst)
            response.raise_for_status()
            data = response.json()
            
            title = data["title"]
            body = data["body"]
            print(f"{title: <25}{body:<10}")
            sucess = True
            break
        
        except Exception:
            continue
    if not sucess:
        print(f"{pst:15} Failed after 3 tries")

