# mental_arithmetic_trainer.py
import random
import sys

def main():
    selected_level = get_level()
    current_score = 0
    
    # Generate exactly 10 distinct mathematical problems sequentially
    for _ in range(10):
        val_x = generate_integer(selected_level)
        val_y = generate_integer(selected_level)
        correct_sum = val_x + val_y
        
        # Strike management tracking variable
        failed_attempts = 0
        
        while failed_attempts < 3:
            try:
                user_answer = int(input(f"{val_x} + {val_y} = "))
                if user_answer == correct_sum:
                    current_score += 1
                    break
                else:
                    print("EEE")
                    failed_attempts += 1
            except ValueError:
                print("EEE")
                failed_attempts += 1
                
        # If terminal maximum count reached without validation, dump correct state
        if failed_attempts == 3:
            print(f"{val_x} + {val_y} = {correct_sum}")
            
    print(f"Score: {current_score}")

def get_level():
    while True:
        level_input = input("Level: ").strip()
        if level_input in ["1", "2", "3"]:
            return int(level_input)

def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError("Invalid target math complexity setting.")
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()