# text_serial_joiner.py
import sys
try:
    import inflect
except ImportError:
    sys.exit("❌ Error: Missing package dependency. Run 'pip install inflect'")

def build_serial_phrase():
    engine = inflect.engine()
    name_buffer = []
    
    while True:
        try:
            name_token = input("Name: ").strip()
            if name_token:
                name_buffer.append(name_token)
        except EOFError:
            print() # Print empty line break on break sequence
            break
            
    if not name_buffer:
        return None
        
    # Join array items with proper Oxford comma punctuation engine rules
    return f"Adieu, adieu, to {engine.join(name_buffer)}"

def main():
    formatted_phrase = build_serial_phrase()
    if formatted_phrase:
        print(formatted_phrase)

if __name__ == "__main__":
    main()