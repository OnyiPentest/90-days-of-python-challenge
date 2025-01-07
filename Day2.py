#!/usr/bin/env python3
'''
Variables and Data Types
- Topics:
 - Learn about variables and different data types: int, str, float, bool.
 - Type casting: converting between types.
- Project:
 - Create a program that takes user input for their name and age, then prints a greeting with their name
and calculates the year they were born.
'''

print("---------------------------------------------------")

# A PYTHON PROGRAM THAT GREETS A USER AND CALCULATES BIRTH YEAR

try:
    # Get user input
    name = input("What is your name? ")
    age = int(input("How old are you? "))  # Convert input to integer

    # Calculate year of birth
    current_year = 2025
    year_of_birth = current_year - age

    # Output the result
    print(f"Hello, {name}! You were born in {year_of_birth}.")
except ValueError:
    # Handle the case where the user inputs a non-integer for age
    print("Error: Please enter a valid number for age.")




