# license_compliance_validator.py

def is_valid(plate_str):
    # Rule 1: Length Validation Block
    if not (2 <= len(plate_str) <= 6):
        return False
        
    # Rule 2: Verify first two tokens are strictly alphabetical
    if not (plate_str[0].isalpha() and plate_str[1].isalpha()):
        return False
        
    # Rule 3: Character Content Verification
    has_number_started = False
    for i in range(len(plate_str)):
        char = plate_str[i]
        
        # Enforce alphanumerical content only (No punctuation/spaces)
        if not char.isalnum():
            return False
            
        # Analyze number sequence logic
        if char.isdigit():
            # First number in sequence cannot register as zero state
            if not has_number_started and char == "0":
                return False
            has_number_started = True
            
        # If number sequence started, trailing characters cannot be letters
        if has_number_started and char.isalpha():
            return False
            
    return True

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

main()