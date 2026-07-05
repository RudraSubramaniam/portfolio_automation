# emoticon_parser.py

def convert_and_validate(text_state):
    emoticon_map = {
        ":)": "🙂", "(:": "🙂", "=)": "🙂",
        ":(": "🙁", "):": "🙁", "=(": "🙁",
        ":D": "😀", ";)": "😉", ";(": "😢",
        ":P": "😛", ":p": "😛", ":O": "😮", 
        ":o": "😮", "<3": "❤️", "xD": "😆",
        "B)": "😎", ":*": "😘", ":/": "😕"
    }
    
    # 1. Tokenize: Split string by spaces into an iterable list
    words = text_state.split(" ")
    final_words = []
    
    # 2. State Verification Loop
    for word in words:
        if word in emoticon_map:
            # Match found: Mutate token state to emoji
            final_words.append(emoticon_map[word])
        elif (":" in word or ";" in word or "=" in word) and len(word) >= 2:
            # Fault Detected: Token looks like a text emoticon but is missing from map
            print(f"⚠️ Notice: Unrecognized emoticon detected -> {word}")
            final_words.append(word)
        else:
            # Regular text state: Pass through unchanged
            final_words.append(word)
            
    # 3. Rebuild string state
    return " ".join(final_words)

def main():
    raw_text = input("Enter text: ")
    parsed_text = convert_and_validate(raw_text)
    print(parsed_text)

main()