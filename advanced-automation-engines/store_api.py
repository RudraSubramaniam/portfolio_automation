import sys
import requests


source = "https://dummyjson.com/products/"

input_entry = sys.argv[1:]

print(f"{'TITLE':<25}{'PRICE':<10}")
print("-" * 35)

for inpe in input_entry:
    if not inpe.isdigit():
        print(f"{inpe:<25} Invalid ID")
        continue

    sucess = False
    for attempt in range(3):
        try:
            response = requests.get(source + input)
            response.raise_for_status()
            data = response.json()
            
            title = data["title"]
            price = data["price"]
            sucess = True
            print(f"{title:<25}{[price]:<10}")
            
            
            
        except Exception as e:
            continue
    
    if not sucess:
        print(f"{inpe} Failed after 3 tries")
        
        
            
        

