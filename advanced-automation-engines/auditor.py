#Problem 9: The Account Auditor
import sys
import requests

source = "https://jsonplaceholder.typicode.com/users/"

input_id_list = sys.argv[1:]

print(f"{"USERNAME":<25}{"COMPANY":<10}")
print("-" * 35)

for inp_id in input_id_list:
    if not inp_id.isdigit():
        print(f"{inp_id:<25} Error: Invalid ID")
        continue

    sucess = False
    for attempt in range(3):
        try: 
            response = requests.get(source + inp_id)
            response.raise_for_status()
            data = response.json()
                
       
            user_nme = data["username"]
            cmpy_nme = data["company"]["name"]
            print(f"{user_nme: <25}{cmpy_nme:<10}")
            sucess = True
            break                    
            
        except Exception:
            continue
     
if not sucess:
    print(f"{inp_id}Failed after 3 tries")
    
    
            
            
   
               
            
            
        
        