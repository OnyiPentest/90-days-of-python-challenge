#!/usr/bin/env python3
'''
Day 5: Functions
- Topics:
 - Learn how to define functions using def.
 - Understand function arguments, return values, and scope.
- Project:
- Write a function that takes a number as input and returns the factorial of that number.
'''



print ("\nA SIMPLE PYTHON TO PRINT THE FACTORIAL OF A NUMBER\n")


# Function to calculate the factorial of a number
def factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers."
    elif number == 0 or number == 1:
        return 1
    else:
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result

# Main program with input validation
while True:
    user_input = input("Enter a number to find its factorial (or type 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    
    if user_input.isdigit():
        number = int(user_input)
        result = factorial(number)
        print(f"The factorial of {number} is: {result}\n")
    else:
        print("Invalid input. Please enter a valid non-negative integer.")
