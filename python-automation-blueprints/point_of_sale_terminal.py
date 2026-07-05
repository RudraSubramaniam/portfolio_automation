# point_of_sale_terminal.py

def run_pos_terminal():
    # 1. Look-up Price Directory
    menu = {
        "Baja Taco": 4.25, "Burrito": 7.50, "Bowl": 8.50, "Nachos": 11.00,
        "Quesadilla": 8.50, "Super Burrito": 8.50, "Super Quesadilla": 9.50,
        "Taco": 3.00, "Tortilla Salad": 8.00
    }
    
    running_total = 0.0
    
    # 2. Continuous Order State Loop
    while True:
        try:
            item_input = input("Item: ")
        except EOFError:
            # Catch Control-D safely to close out transaction loop
            print() # Insert trailing line break
            break
            
        # 3. Sanitize and Match Text State
        sanitized_item = item_input.strip().title()
        
        # 4. Ledger State Modification
        if sanitized_item in menu:
            running_total += menu[sanitized_item]
            print(f"Total: ${running_total:.2f}")
        else:
            # Filter out non-menu items silently
            pass

def main():
    run_pos_terminal()

main()