#!/usr/bin/env python3
'''

Day 7: Dictionaries and Sets
- Topics:
 - Learn about dictionaries (key-value pairs) and sets (unordered collections).
 - Dictionary methods: get(), keys(), values().
- Project:
 - Create a program that stores user information (name, age) in a dictionary and allows the user to
retrieve it by providing the name


Step-by-Step Approach
1. Define a dictionary to store user information.
2. Add user data (name and age) as key-value pairs.
3. Retrieve data by using the get() method to avoid errors.
4. Implement a menu-driven program for ease of interaction.

'''


print ("\nA SIMPLE PYTHON TO STORE USERS' INFORMATION\n")
def user_info_program():
    # Step 1: Create an empty dictionary to store user data
    user_data = {}

    while True:
        print("\n--- User Information Program ---")
        print("1. Add User Information")
        print("2. Retrieve User Information")
        print("3. Display All Users")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            # Add user information
            name = input("Enter the user's name: ").strip()
            age = input(f"Enter {name}'s age: ").strip()
            
            if name in user_data:
                print(f"{name} is already in the system. Updating age.")
            1
            user_data[name] = age
            print(f"User '{name}' added/updated successfully.")

        elif choice == "2":
            # Retrieve user information
            name = input("Enter the name to retrieve information: ").strip()
            age = user_data.get(name, None)
            
            if age:
                print(f"{name} is {age} years old.")
            else:
                print(f"No information found for '{name}'.")
        
        elif choice == "3":
            # Display all users
            if user_data:
                print("\n--- All Users ---")
                for key, value in user_data.items():
                    print(f"Name: {key}, Age: {value}")
            else:
                print("No user data available.")
        
        elif choice == "4":
            # Exit the program
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")

# Run the program
user_info_program()
