#!/usr/bin/env python3


'''
Day 12: Working with JSON
- Topics:
 - Learn how to parse and create JSON data using Python’s json library.
 - Understanding JSON format and how it is used in APIs.
- Project:
 - Create a script that reads a JSON file and prints out specific values based on user input.

How It Works

The script opens and reads data.json using json.load().
It displays all the top-level keys in the JSON file to guide the user.
The user is prompted to input a key.
Based on the key:
If the value is a list, it prints all items and allows further filtering if they are dictionaries.
If the value is a dictionary, it prints all key-value pairs.
If the value is a single value (e.g., string or number), it directly prints the value

'''

print("\nA SIMPLE PYTHON PROGRAM TO READ A JSON FILE AND PRINT SPECIFIC VALUES BASED ON USER INPUT\n")


import json

# Load the JSON data from file
with open('data.json', 'r') as file:
    data = json.load(file)

# Display keys available in the JSON file
print("Available keys in the JSON file:")
for key in data.keys():
    print(f"- {key}")

# Ask the user for input
key = input("\nEnter the key you want to retrieve (e.g., employees, company, location): ")

# Check if the user input matches a top-level key
if key in data:
    value = data[key]
    
    # Handle lists (like 'employees')
    if isinstance(value, list):
        print("\nThe value is a list. Here are the items:")
        for index, item in enumerate(value):
            print(f"{index + 1}: {item}")
        
        # Ask the user if they want to search inside the list
        search_key = input("\nEnter a field to search within the list (e.g., name, age, department): ")
        search_value = input(f"Enter the value to search for in '{search_key}': ")

        found = False
        for item in value:
            if search_key in item and item[search_key] == search_value:
                print(f"Match found: {item}")
                found = True
                break

        if not found:
            print(f"No match found for {search_key} = {search_value}.")
    
    # Handle dictionaries (e.g., 'location')
    elif isinstance(value, dict):
        print("\nThe value is a dictionary. Here are the key-value pairs:")
        for sub_key, sub_value in value.items():
            print(f"{sub_key}: {sub_value}")
    
    # Handle single values (e.g., 'company')
    else:
        print(f"\nThe value for '{key}' is: {value}")

else:
    print(f"Key '{key}' not found in the JSON file.")
