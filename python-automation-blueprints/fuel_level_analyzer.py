# fuel_level_analyzer.py

def calculate_gauge_percentage():
    while True:
        fraction_input = input("Enter fuel fraction (X/Y): ").strip()
        
        # 1. Structural Validation Gate: Verify delimiter presence
        if "/" not in fraction_input:
            continue
            
        try:
            # 2. Tokenize and Cast State
            numerator_str, denominator_str = fraction_input.split("/")
            x = int(numerator_str)
            y = int(denominator_str)
            
            # 3. Rule Invariant Checks
            if x < 0 or y <= 0 or x > y:
                continue
                
            # 4. Arithmetic Evaluation
            percentage = round((x / y) * 100)
            
            # 5. Output Range Calibration Mapping
            if percentage <= 1:
                return "E"
            elif percentage >= 99:
                return "F"
            else:
                return f"{percentage}%"
                
        except (ValueError, ZeroDivisionError):
            # Intercept bad types or division by zero state changes; restart loop
            continue

def main():
    gauge_state = calculate_gauge_percentage()
    print(gauge_state)

main()