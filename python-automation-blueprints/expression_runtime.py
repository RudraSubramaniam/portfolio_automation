# expression_runtime.py

def evaluate_expression(expression_state):
    # 1. Tokenize string into logical structures [x, y, z]
    tokens = expression_state.strip().split(" ")
    
    if len(tokens) != 3:
        print("❌ Error: Input state must follow 'x y z' token sequence.")
        return None
        
    # 2. State Extraction and Casting
    x = float(tokens[0])
    operator = tokens[1]
    z = float(tokens[2])
    
    # 3. Functional Mapping
    if operator == "+":
        return x + z
    elif operator == "-":
        return x - z
    elif operator == "*":
        return x * z
    elif operator == "/":
        if z == 0.0:
            print("❌ Error: Zero division state change blocked.")
            return None
        return x / z
    else:
        print(f"❌ Error: Unrecognized operational state '{operator}'.")
        return None

def main():
    expression = input("Expression: ")
    result = evaluate_expression(expression)
    if result is not None:
        print(f"{result:.1f}")

main()