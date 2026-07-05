# meal_scheduler.py

def convert(time_str):
    # 1. Parse string: Split into structural hours and minutes
    hours, minutes = time_str.strip().split(":")
    
    # 2. State calculation: Translate minutes to fractional hour float
    fractional_hours = float(hours) + (float(minutes) / 60.0)
    return fractional_hours

def main():
    raw_time = input("What time is it? ")
    current_hour_state = convert(raw_time)
    
    # 3. Schedule Evaluation (Inclusive Hour Boundaries)
    if 7.0 <= current_hour_state <= 8.0:
        print("breakfast time")
    elif 12.0 <= current_hour_state <= 13.0:
        print("lunch time")
    elif 18.0 <= current_hour_state <= 19.0:
        print("dinner time")
    else:
        # Non-meal window: State terminates silently
        pass

if __name__ == "__main__":
    main()