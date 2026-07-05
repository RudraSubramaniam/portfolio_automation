
""""'""
s = input("Date: ").strip()

d = s.replace(",", "").replace("/", " ").replace("-", " ")
date = d.split()

print(date) 
""""'""


months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()
    
    try:
        # Scenario A: The Slash Format (Month/Day/Year)
        if "/" in date:
            m, d, y = date.split("/")
            # Convert to integers for range checking
            month, day, year = int(m), int(d), int(y)
            
        # Scenario B: The Text Format (Month Day, Year)
        elif "," in date:
            # Split by space and remove the comma from the day
            m_text, d_text, year = date.split(" ")
            if m_text in months:
                month = months.index(m_text) + 1
                day = int(d_text.replace(",", ""))
                year = int(year)
            else:
                continue # Month name not in list
        else:
            continue # Neither slash nor comma found

        # Range Validation
        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{year}-{month:02}-{day:02}")
            break

    except (ValueError, NameError):
        continue