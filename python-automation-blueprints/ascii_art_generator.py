# ascii_art_generator.py
import random
import sys

try:
    from pyfiglet import Figlet
except ImportError:
    sys.exit("❌ Error: Missing package dependency. Run 'pip install pyfiglet'")

def configure_engine():
    figlet = Figlet()
    available_fonts = figlet.getFonts()
    
    # 1. Read command line argument arrays
    arg_count = len(sys.argv)
    
    if arg_count == 1:
        # Zero args passed: pick random structural font
        selected_font = random.choice(available_fonts)
    elif arg_count == 3:
        # Flag and font identifier passed
        flag = sys.argv[1]
        font_name = sys.argv[2]
        
        if flag not in ["-f", "--font"] or font_name not in available_fonts:
            sys.exit("Invalid usage")
        selected_font = font_name
    else:
        sys.exit("Invalid usage")
        
    figlet.setFont(font=selected_font)
    return figlet

def main():
    rendering_tool = configure_engine()
    user_text = input("Input: ")
    print(rendering_tool.renderText(user_text))

if __name__ == "__main__":
    main()