# universal_truth_validator.py

def validate_truth(answer_state):
    # 1. Sanitize input: Strip whitespace and cast to lowercase
    clean_state = answer_state.strip().lower()
    
    # 2. Define valid matches in a set container
    valid_answers = {"42", "forty-two", "forty two"}
    
    # 3. Conditional Check
    if clean_state in valid_answers:
        return "Yes"
    else:
        return "No"

def main():
    user_input = input("What is the answer to the Great Question? ")
    result = validate_truth(user_input)
    print(result)

main()