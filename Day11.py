'''
Day 11: Regular Expressions
- Topics:
 - Introduction to the re library.
 - Basic regex syntax: \d, \w, \s, +, *, ?.

 Project:
 - Build a program that validates email addresses using regular expression


 Step-by-Step Procedures

1. Import the re Library: This allows us to use regular expressions for pattern matching.
2. Define a Regex Pattern: Use r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$" to validate email formats.
3. Create the validate_email() Function: Check if the input matches the regex pattern and return True for valid emails and False for invalid ones.
4. Loop for User Input: Use a while True loop to keep asking for input until the user enters a valid email.
5. Validate Input: Inside the loop, call validate_email() to check if the email is valid.
6. Provide Feedback: Display success or error messages based on the validation result.
7. Break the Loop: Exit the loop when a valid email is entered.

'''

print("\nA SIMPLE PYTHON PROGRAM TO VALIDATE EMAIL ADDRESSES USING REGULAR EXPRESSIONS\n")


import re

# Function to validate an email address
def validate_email(email):
    # Regex pattern for a valid email
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    # Check if the email matches the pattern
    return bool(re.match(pattern, email))

# Function to repeatedly prompt the user until a valid email is entered
def main():
    while True:
        # Ask the user to input an email address
        email = input("Enter an email address to validate: ")
        
        # Validate the email
        if validate_email(email):
            print(f"'{email}' is a valid email address. Thank you!")
            break
        else:
            print(f"'{email}' is NOT a valid email address. Please try again.")

# Run the program
main()
