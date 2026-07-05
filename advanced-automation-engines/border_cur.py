library = ["USD", "EUR", "GBP", "JPY", "INR"]

while True:

    currency = input("Enter Banknote:").strip().split() 
    try:
        if len(currency) != 2: 
            data_a , data_x = currency
            if data_a.upper() in library:
                amount = data_a.upper()
                sign = float(data_x)
                
            elif data_x.upper() in library:
                amount = data_x.upper()
                sign = float(data_a)
                
            if amount > 0:
                print(f"number is : {sign} {amount:.2f}")
            
            else:
                continue
   
        else:
            continue
 
    except (NameError, ValueError):  
        continue

    