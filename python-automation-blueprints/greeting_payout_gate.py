# greeting_payout_gate.py

def calculate_payout(greeting_state):
    # 1. Sanitize text state
    clean_greeting = greeting_state.strip().lower()
    
    # 2. Structural Conditional Evaluation
    if clean_greeting.startswith("hello"):
        return 0
    elif clean_greeting.startswith("h"):
        return 20
    else:
        return 100

def main():
    user_greeting = input("Enter greeting: ")
    payout = calculate_payout(user_greeting)
    print(f"${payout}")

main()