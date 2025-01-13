#!/usr/bin/env python3
'''
Day 8: File I/O
- Topics:
- Learn how to read and write files in Python using open(), read(), write().
 - Working with text and CSV files.
- Project:
 - Write a script that reads a text file and counts how many lines and words are in the file

Step-by-Step Guide
1. Open the file in read mode.
2. Read all lines into a list using readlines().
3. Count the lines using len().
4. Split each line into words using split() and count the total words.
5. Display the results.

'''
def count_lines_and_words(file_name):
    try:
        with open(file_name, 'r') as file:  # Use the parameter as the file name
            lines = file.readlines()  # Read all lines
            line_count = len(lines)  # Count lines
            
            word_count = 0
            for line in lines:
                words = line.split()  # Split line into words
                word_count += len(words)  # Count words in each line
            
            print(f"Number of lines: {line_count}")
            print(f"Number of words: {word_count}")
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Test the function
file_name = 'simple_text.txt'  
count_lines_and_words(file_name)
