
#logic—Triggered Accumulation
percentage = "x"
current_time = "y"
change = "z"


def step_rounding():
        while current_time < 15: # Safety exit at 15 minutes
        if current_time % 5 == 0:
            # Action: Add the change
            percentage += change 
            
            # Action: Apply the Step-Rounding Formula
            # (Result = round(18.3 / 3) * 3)
            result = round(percentage / change) * change
            
            print(f"At {current_time} mins, Result is {result}")
            
        current_time += 1 # Critical: Increment time to avoid infinite loop