# gratuity_calculator.py

def dollars_to_float(dollar_str):
    # Sanitize: Strip spaces and remove leading '$' if present
    clean_str = dollar_str.strip().lstrip("$")
    try:
        return float(clean_str)
    except ValueError:
        print(f"❌ Error: Cannot convert '{dollar_str}' to currency float.")
        return 0.0

def percent_to_float(percent_str):
    # Sanitize: Strip spaces and remove trailing '%' if present
    clean_str = percent_str.strip().rstrip("%")
    try:
        return float(clean_str) / 100
    except ValueError:
        print(f"❌ Error: Cannot convert '{percent_str}' to percentage float.")
        return 0.0

def main():
    # 1. Initialize State and Filter Inputs
    meal_cost = dollars_to_float(input("How much was the meal? "))
    tip_percent = percent_to_float(input("What percentage would you like to tip? "))
    
    # 2. State Guard Check
    if meal_cost <= 0.0 or tip_percent <= 0.0:
        print("❌ Calculation halted: Invalid numeric financial values.")
        return

    # 3. Mathematical State Calculation
    tip_amount = meal_cost * tip_percent
    
    # 4. Advanced Logic: Apply extreme tip alert safety flag
    if tip_percent > 0.50:
        print("⚠️ Alert: Tip setting exceeds 50% of the total cost.")

    print(f"Leave ${tip_amount:.2f}")

main()