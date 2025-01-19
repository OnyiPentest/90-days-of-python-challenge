#!/usr/bin/env python3


'''
Day 14: Working with APIs
- Topics:
 - Learn how to send requests and handle JSON responses from APIs.
- Authentication methods for APIs (e.g., using API keys).

- Project:
 - Write a program that interacts with the GitHub API to fetch user data (like profile information

How It Works

This program interacts with the GitHub API to fetch user profile information.
It uses the endpoint https://api.github.com/users/{username} to send an HTTP GET request.
If the request is successful (status code 200), it extracts and displays the following details:

Name
Bio
Location
Number of public repositories
Number of followers and following
If the request fails, it displays an error message.

'''

print("\nA SIMPLE PYTHON PROGRAM TO INTERACT WITH THE GITHUB API AND FETCH USER PROFILE INFORMATION\n")


import requests

# Base URL for the GitHub API
BASE_URL = "https://api.github.com/users"

# Function to fetch GitHub user data
def get_github_user(username):
    # Construct the API URL
    url = f"{BASE_URL}/{username}"

    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response
        print("\nUser Profile Information:")
        print(f"Name: {data.get('name', 'N/A')}")
        print(f"Bio: {data.get('bio', 'N/A')}")
        print(f"Location: {data.get('location', 'N/A')}")
        print(f"Public Repositories: {data.get('public_repos', 0)}")
        print(f"Followers: {data.get('followers', 0)}")
        print(f"Following: {data.get('following', 0)}")
    else:
        print(f"Error: Unable to fetch data for user '{username}' (Status Code: {response.status_code})")

# Ask the user for a GitHub username
username = input("Enter a GitHub username: ")
get_github_user(username)


