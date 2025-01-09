"""
Purpose: To check whether the given character
        is vowels or consonant

        vowels - aeiou

in operator  works with any iterable object

Algorithm:
============
1) is it empty 
2) is it alphabet 
3) is it vowel or not 

NOTE: handle case-sensitivity 
"""

char = input("Enter a character: ").strip()

# Algoritm 1: Check if the input is empty

if not char:
    print("No character entered. Please try again.")

# Algoritm 2: Check if the input is a single alphabetic character

elif not char.isalpha() or len(char) > 1:
    print("Invalid input. Please enter a single alphabetic character.")
    
# Algoritm 3: Check if the character is a vowel
else:
    # Convert to lowercase to handle case-sensitivity
    char = char.lower()
    
    # Define vowels
    vowels = "aeiou"
    
    if char in vowels:
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is a consonant.")