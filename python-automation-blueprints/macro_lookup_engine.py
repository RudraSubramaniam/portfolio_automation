# macro_lookup_engine.py

def fetch_calories(fruit_name):
    # 1. Lowercase Target Map Directory
    fda_nutrition_catalog = {
        "apple": 130, "avocado": 50, "banana": 110, "cantaloupe": 50,
        "grapefruit": 60, "grapes": 90, "honeydew melon": 50, "kiwifruit": 90,
        "lemon": 15, "lime": 20, "nectarine": 60, "orange": 80,
        "peach": 60, "pear": 100, "pineapple": 50, "plums": 70,
        "strawberries": 50, "sweet cherries": 100, "tangerine": 50, "watermelon": 80
    }
    
    # 2. Sanitize search key state
    lookup_key = fruit_name.strip().lower()
    
    # 3. Membership Gate Conditional
    if lookup_key in fda_nutrition_catalog:
        return fda_nutrition_catalog[lookup_key]
    return None

def main():
    fruit_input = input("Item: ")
    calorie_count = fetch_calories(fruit_input)
    
    # 4. Filter State Result Output
    if calorie_count is not None:
        print(f"Calories: {calorie_count}")
    else:
        # Invalid item or non-fruit data: terminate silently
        pass

main()