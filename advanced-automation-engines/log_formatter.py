import requests
import sys
from datetime import date

source = "https://baconipsum.com/api/?type=all-meat&sentences=1&start-with-lorem=1"

response = requests.get(source)
if response.status_code != 200:
   sys.exit("Server Error: Shutdown")
    

data = response.json()
messy_str = data[0]
clean_str = messy_str.strip().split()[0]

today = date.today()


print(f"""
--- Log Entry Generated ---
Date: {today}
Category: {clean_str}
Status: Success
""")
    
    



