# text_pacer.py

def pace_speech(text_state):
    # 1. Tokenize text into an array based on spaces
    tokens = text_state.split(" ")
    
    # 2. State Verification: If array has only 1 element, no spaces exist
    if len(tokens) == 1:
        print("⚠️ Notice: No space boundaries found in input text state.")
        return text_state

    # 3. State Transformation: Rebuild with pacing syntax
    return "...".join(tokens)

def main():
    raw_speech = input("Enter speech text: ")
    paced_output = pace_speech(raw_speech)
    print(f"Paced Output: {paced_output}")

main()