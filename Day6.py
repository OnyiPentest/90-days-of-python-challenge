#!/usr/bin/env python3
'''
Day 6: Lists and Tuples
- Topics:
 - Learn about lists and tuples: how to create, access, modify, and delete elements.
 - List methods: append(), remove(), pop().
- Project:
 - Create a program that takes a list of numbers and prints the sum and average.

 Steps I took:
1. Created a list of numbers.
2. Calculated the sum of the numbers using the sum() function.
3. Calculated the average by dividing the sum by the length of the list.
4. Print the results.
'''



print ("\nA SIMPLE PYTHON TO PRINT THE SUM AND AVERAGE OF NOS IN A LIST\n")

# Step 1: Create a list of numbers
numbers = [10, 20, 30, 40, 50]

# Step 2: Calculate the sum of the numbers
sum_total = sum(numbers)

# Step 3: Calculate the average of the numbers
average = sum_total / len(numbers)

# Step 4: Print the results
print(f"Sum: {sum_total}")
print(f"Average: {average}")

