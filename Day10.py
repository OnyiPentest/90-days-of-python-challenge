#!/usr/bin/env python3

'''

Day 10: Introduction to Libraries
- Topics:
 - Introduction to Python libraries: how to install and use them (using pip).
- Using built-in libraries like os, sys, math.

- Project:
- Write a Python script that calculates the square root of a number using the math library.

How It Works:

Import math: Enables tools like math.sqrt().
Get_whole_number(): Ensures the user inputs a valid whole number.
Math.sqrt(): Calculates the square root of the input.
Print(): Displays the result clearly.

'''

print ("\nA SIMPLE PYTHON TO CALCULATE SQUARE ROOT OF A NUMBER\n")

# Step 1: Import the math library
import math

# Step 2: Function to check if input is a valid whole number
def get_whole_number():
    while True:
        try:
            # Ask the user to enter a number
            number = int(input("Enter a whole number to find its square root: "))
            return number
        except ValueError:
            print("Oops! That’s not a valid whole number. Please try again.")

# Step 3: Get a valid whole number from the user
number = get_whole_number()

# Step 4: Calculate the square root
square_root = math.sqrt(number)

# Step 5: Print the result
print(f"The square root of {number} is {square_root}")
