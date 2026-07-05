# case_style_transformer.py

def camel_to_snake(camel_str):
    # 1. Initialize empty state buffer
    snake_chars = []
    
    # 2. Sequential Logic Iteration Loop
    for char in camel_str.strip():
        # Check if character state is uppercase
        if char.isupper():
            # Inject separator and cast character state to lower
            snake_chars.append("_")
            snake_chars.append(char.lower())
        else:
            # Pass regular character state through
            snake_chars.append(char)
            
    # 3. Join array tokens into final string state
    return "".join(snake_chars)

def main():
    camel_input = input("Enter camelCase variable: ")
    snake_output = camel_to_snake(camel_input)
    print(snake_output)

main()