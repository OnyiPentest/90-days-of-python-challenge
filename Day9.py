#!/usr/bin/env python3

'''

Day 9: Error Handling
- Topics:
 - Learn how to use try, except, and finally for error handling.
 - Handling specific exceptions like ValueError, FileNotFoundError.
- Project:
 - Create a program that takes user input for a number and catches errors if the user inputs something
invalid (non-integer).

Step-by-Step Procedures
1. Use try to attempt converting user input into an integer.
2. Use except to catch errors like ValueError (e.g., if the user types letters instead of numbers).
3. Optionally, add a finally block to display a final message.
'''

print ("\nA SIMPLE PYTHON TO HANDLE USER INPUT ERRORS\n")

def get_user_number():
    try:
        # Ask the user to input a number
        user_input = input("Enter a number: ")
        number = int(user_input)  # Try converting input to an integer
        print(f"You entered: {number}")
    except ValueError:  # Catch invalid input
        print("Oops! That’s not a valid number. Please try again.")
    finally:
        print("Thank you for using the program.")  # Always runs, even if there's an error

# Test the function
get_user_number()
