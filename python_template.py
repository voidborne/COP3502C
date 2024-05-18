'''
Module 1 - Lecture 1 Notes 
Description: Examples and notes from class
Author: Garry Scott
Date: 2024-05-15
'''

'''
# Import statments

# Standard Library
import os
import sys
import time

# Third-party Library
import requests

# Local Application
from my_module import my_function
'''

'''
# Constants 

BASE_URL = "https://api.example.com"
TIMEOUT = 30
'''

'''
# Global Variables

response_cache = {}
'''

'''
def fetch_data(url: str) -> dict:
    """
    Fetch data from the given URL.

    Parameters:
    url (str): The URL to fetch data from.

    Returns:
    dict: The fetched data.
    """
    try:
        response = requests.get(url, timeout=TIMEOUT)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return {}
'''

def main():

    # Print a greeting message
    print('Hello World\n')

    # Print a message with nested quotes
    print('''They said, "It's raining".''')

    # Assign a string to a variable and print it
    my_name = 'Garry Scott'
    print(f'\nMy name is: {my_name}\n')

    # Perform basic arithmetic operations
    a = 15
    b = 5
    c = a - b

    # Print the value of variables and results of operations
    print('Arithmetic Operations:')
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = a - b = {c}')
    print(f'c * 5 = {c * 5}\n')

    # More arithmetic operations with reassignment
    x = 5
    y = 3 * x
    x = y - 5
    y = 2 * x

    # Print the sum of x and y
    print('More Arithmetic Operations:')
    print(f'x = {x}')
    print(f'y = {y}')
    print(f'x + y = {x + y}\n')

    # Modulus operation with a floating point number
    test = 45 % 3.67
    print('Modulus Operation with Floating Point:')
    print(f'45 % 3.67 = {test}\n')

    # Division operations
    a = 20
    b = 30
    c = b / a    # Floating-point division
    d = b // a   # Integer (floor) division
    print('Division Operations:')
    print(f'b / a = {c}')
    print(f'b // a = {d}')
    print(f'b / a + b // a = {c + d}\n')

    # Modulus operation with integers
    a = 80
    b = 90
    print('Modulus Operation with Integers:')
    print(f'80 % 90 = {a % b}')

# The entry point for the program
if __name__ == '__main__':
    main()