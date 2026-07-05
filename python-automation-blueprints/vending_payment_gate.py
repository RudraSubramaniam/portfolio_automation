# vending_payment_gate.py

def process_vending_payment():
    # 1. State Trackers Initialization
    amount_due = 50
    accepted_coins = {25, 10, 5}
    
    # 2. Decremental Loop Engine
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        try:
            coin = int(input("Insert Coin: "))
        except ValueError:
            # Handle invalid non-integer crash scenarios
            continue
            
        # Validation Gate: Enforce currency denomination rules
        if coin in accepted_coins:
            amount_due -= coin
        else:
            # Fault Detected: Filter out rogue integer inputs quietly
            pass
            
    # 3. Final Change Calculation State Change
    change_owed = abs(amount_due)
    print(f"Change Owed: {change_owed}")

def main():
    process_vending_payment()

main()