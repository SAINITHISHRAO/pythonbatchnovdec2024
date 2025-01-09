"""
Purpose: Temperature Conversions
    - Celsius to Fahrenheit
    - Determine if it's freezing, cold, warm, or hot
"""

# Input: Get temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Conversion: Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

# Output: Display the temperature in Fahrenheit and its category
print(f"{celsius}°C is equal to {fahrenheit}°F.")
