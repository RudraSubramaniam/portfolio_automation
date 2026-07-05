# iso_date_normalizer.py

def normalize_to_iso():
    months_catalog = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    while True:
        date_raw = input("Date: ").strip()
        
        # --- PIPELINE A: DIGITAL FORMAT (MM/DD/YYYY) ---
        if "/" in date_raw:
            try:
                month_part, day_part, year_part = date_raw.split("/")
                m = int(month_part)
                d = int(day_part)
                y = int(year_part)
                
                # Boundary verification
                if 1 <= m <= 12 and 1 <= d <= 31:
                    return f"{y:04d}-{m:02d}-{d:02d}"
            except ValueError:
                pass
                
        # --- PIPELINE B: TEXTUAL FORMAT (Month DD, YYYY) ---
        elif "," in date_raw:
            try:
                # Isolate month/day string from year string
                left_phrase, year_part = date_raw.split(",")
                year_val = int(year_part.strip())
                
                # Isolate month title from day token
                month_title, day_part = left_phrase.strip().split(" ")
                day_val = int(day_part)
                
                # Check text month string against structural catalog array
                if month_title in months_catalog:
                    month_val = months_catalog.index(month_title) + 1
                    
                    if 1 <= day_val <= 31:
                        return f"{year_val:04d}-{month_val:02d}-{day_val:02d}"
            except ValueError:
                pass
                
        # Format layout error state detected: drop down and rerun loop
        continue

def main():
    iso_string = normalize_to_iso()
    print(iso_string)

main()