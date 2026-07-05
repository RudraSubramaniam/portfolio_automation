# text_normalizer.py

def normalize_text(text_state):
    # 1. Verification Block: Check if state is empty
    if not text_state.strip():
        print("⚠️ Warning: Empty input state received.")
        return text_state

    # 2. Verification Block: Check if mutation is needed
    if text_state.islower():
        print("ℹ️ Info: Text is already normalized to lowercase.")
        return text_state

    # 3. State Mutation Execution
    return text_state.lower()

def main():
    raw_text = input("Enter text to normalize: ")
    processed_text = normalize_text(raw_text)
    print(f"Result: {processed_text}")

main()