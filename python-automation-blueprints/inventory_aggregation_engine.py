# inventory_aggregation_engine.py

def aggregate_inventory():
    inventory_ledger = {}
    
    # 1. Continuous Input Collection Phase
    while True:
        try:
            item = input()
        except EOFError:
            print() # Structural spacing format
            break
            
        # Sanitize token to uppercase state
        clean_item = item.strip().upper()
        
        if not clean_item:
            continue
            
        # 2. Frequency Tracking Logic
        if clean_item in inventory_ledger:
            inventory_ledger[clean_item] += 1
        else:
            inventory_ledger[clean_item] = 1
            
    # 3. Output Generation Phase (Alphabetized Sort Evaluation)
    for sorted_item in sorted(inventory_ledger.keys()):
        count = inventory_ledger[sorted_item]
        print(f"{count} {sorted_item}")

def main():
    aggregate_inventory()

main()