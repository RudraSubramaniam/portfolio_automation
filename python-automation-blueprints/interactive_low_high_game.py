# interactive_low_high_game.py
import random
import sys

def get_positive_integer(prompt_text):
    while True:
        try:
            value = int(input(prompt_text))
            if value > 0:
                return value
        except ValueError:
            pass

def run_game_engine():
    # 1. Establish range state
    max_level = get_positive_integer("Level: ")
    
    # 2. Compute static goal variable
    target_secret = random.randint(1, max_level)
    
    # 3. Dynamic evaluation checking loops
    while True:
        user_guess = get_positive_integer("Guess: ")
        
        if user_guess < target_secret:
            print("Too small!")
        elif user_guess > target_secret:
            print("Too large!")
        else:
            print("Just right!")
            sys.exit(0)

def main():
    run_game_engine()

if __name__ == "__main__":
    main()