#The Weather-User Auditor (Scenario: You are auditing a list of User IDs.)
#Inputs: Numbers (e.g., 1 2 555 apple).

import sys
import requests

source = "https://jsonplaceholder.typicode.com/users/"

numb_list = sys.argv[1:]
print(f"{"NAME":<25}{"LATITUDE":<10}")
print("_" * 35)

for numb in numb_list:
    if not numb.isdigit():
        print(f"{numb:<25} ERROR: Use Numbers Only")
        continue
    
    sucess = False
    for attempts in range(3):
        try:
            response = requests.get(source + numb)
            response.raise_for_status()
            data = response.json()
            
            nme = data["name"]
            lat = data["address"]["geo"]["lat"]
            print(f"{nme:<25}{lat:<10}")
            sucess = True
            break
        
        except Exception:
            continue
        
    if not sucess:
        print(f"{numb:<25} Failed after 3 tries")