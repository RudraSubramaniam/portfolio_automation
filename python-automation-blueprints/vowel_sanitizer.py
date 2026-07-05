# vowel_sanitizer.py

def sanitize_vowels(text_state):
    # 1. Memory Look-up Set (Fast O(1) evaluation)
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    
    # 2. Rebuild string without targeted vowel characters
    clean_chars = [char for char in text_state if char not in vowels]
    return "".join(clean_chars)

def main():
    raw_text = input("Input: ")
    processed_text = sanitize_vowels(raw_text)
    print(f"Output: {processed_text}")

main()