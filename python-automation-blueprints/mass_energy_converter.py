# mass_energy_converter.py

# 1. State Initialization: Prompt user for mass
mass_kg = int(input("Enter mass in kilograms: "))

# 2. Constant Definition: Speed of light in m/s
SPEED_OF_LIGHT = 300000000

# 3. Calculation: E = m * c^2
energy_joules = mass_kg * (SPEED_OF_LIGHT ** 2)

# 4. State Output
print(energy_joules)