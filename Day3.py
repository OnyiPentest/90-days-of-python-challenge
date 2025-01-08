#!/usr/bin/env python3
'''
Day 3: Conditional Statements
- Topics:
 - Learn about if, else, and elif statements.
 - Logical operators: and, or, not

Project:

Build a simple age checker: Ask the user for their age and tell them if they are eligible for certain
services (e.g., "You are eligible to vote" or "You are too young to vote").
'''



print ("A PYTHON PROGRAM SIMPLE AGE CHECKER FOR VOTE ELIGIBILITY\n")

#Collecting user Details

name = input ("\nPlease Enter your name: ")

age = input("\nPlease Enter your Age: " )

#Validating user input to make sure the right input was made

if age.isdigit():
    age = int(age)

    if age <=17:
        print(f"\n{name}, You are too young to vote\n")

    elif age >=18 and age < 100:
        print (f"\n{name}, You are eligible to vote\n")
    
    else:
        print (f"\n{name}, You're not eligible to vote becaause you're above 100yrs! ")


else:
    print(f"{name}, This is an invalid input, please input a valid age.")