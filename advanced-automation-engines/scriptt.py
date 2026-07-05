
import sys
import requests

# 1. Start with clean URL
source = "https://geocoding-api.open-meteo.com/v1/search?name="

# 2. Collect cities from command line arguments (skipping the script name)
city_list = sys.argv[1:] 

print(f"{'CITY':<15}{'LAT':<10}{'LON':<10}")
print("-" * 35)

for city in city_list:
    # 3. Validation: Check if input is only letters
    if not city.isalpha():
        print(f"{city:<15} ERROR: Use Alphabets Only")
        continue

    # 4. Request with Retry Logic (Max 3 tries)
    success = False
    for attempt in range(3):
        try:
            response = requests.get(source + city)
            response.raise_for_status()
            data = response.json()
            
            if "results" in data:
                lat = data["results"][0]["latitude"]
                lon = data["results"][0]["longitude"]
                print(f"{city:<15}{lat:<10}{lon:<10}")
                success = True
                break # Exit the retry loop on success
        except Exception:
            continue # Try again if the server flakes out

    if not success:
        print(f"{city:<15} FAILED after 3 tries")