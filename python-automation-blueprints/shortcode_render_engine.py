# shortcode_render_engine.py
import sys
try:
    import emoji
except ImportError:
    sys.exit("❌ Error: Missing package dependency. Run 'pip install emoji'")

def convert_shortcodes(text_state):
    # Pass structural language='alias' named parameter to match shortcut text keys
    return emoji.emojize(text_state, language="alias")

def main():
    user_input = input("Input: ")
    rendered_output = convert_shortcodes(user_input)
    print(f"Output: {rendered_output}")

if __name__ == "__main__":
    main()