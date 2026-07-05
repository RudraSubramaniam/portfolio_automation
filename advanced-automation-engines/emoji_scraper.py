import requests
from bs4 import BeautifulSoup

# 1. Capture: Get the raw HTML from the web
url = "https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias"
response = requests.get(url)

# 2. Parse: Turn the raw HTML string into a "Soup" object we can search
soup = BeautifulSoup(response.text, "html.parser")

# 3. Search: Find every Table Data (td) cell on the page
cells = soup.find_all("td")

# 4. Storage: Create an empty dictionary to act as our local database
emoji_map = {}

# 5. Loop: State Tracking
# Logic: We know the table has (usually) the emoji in one cell and the alias next to it
for i in range(0, len(cells) - 1, 2):
    emoji_icon = cells[i].text.strip()
    # Strip the colons so the input works without them
    alias = cells[i+1].text.replace(":", "").strip()
    
    # Store in our dictionary
    emoji_map[alias] = emoji_icon

# 6. Execution: User Input vs. Local Database
entry = input("Input: ")
result = emoji_map.get(entry, entry) # Logic: Get emoji, or return original text if not found

print("Output:", result)