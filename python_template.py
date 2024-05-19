'''
Title: Example Project
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

# Function to print greeting messages
def greeting():
    my_name = 'Garry Scott'
    print(
        '\n'
        f'''Hello World. My name is {my_name}. Let's check out a few "functions".\n'''
        '\n'
        )

# Function to demonstrate basic arithmetic operations
def arithmetic_operations():
    a = 15
    b = 5
    c = a - b
    print(
        'Arithmetic Operations:\n'
        '\n'
        f'{a = }\n'
        f'{b = }\n'
        f'c = {c = }\n'
        f'{c * 5 = }\n'
        '\n'
    )

# Function to demonstrate more complex arithmetic operations with reassignment
def more_arithmetic_operations():
    x = 5
    y = 3 * x
    x = y - 5
    y = 2 * x
    print(
        'More Arithmetic Operations:\n'
        '\n'
        f'{x = }\n'
        f'{y = }\n'
        f'{x + y = }\n'
        '\n'
    )

# Function to demonstrate modulus operation with floating point numbers
def modulus_floating_point():
    a = 45
    b = 3.67
    print(
        'Modulus Operation with Floating Point:\n'
        '\n'
        f'{a % b = }\n'
        '\n'
    )

# Function to demonstrate various division operations
def division_operations():
    a = 20
    b = 30
    print(
        'Division Operations:\n'
        '\n'
        f'{b / a = }\n'
        f'{b // a = }\n'
        f'{b / a + b // a = }\n'
        '\n'
    )

# Function to demonstrate modulus operation with integers
def modulus_integers():
    a = 80
    b = 90
    print(
        'Modulus Operation with Integers:\n'
        '\n'
        f'{a % b = }\n'
        '\n'
    )

# The main function that calls all other functions to execute the script
def main():
    greeting()
    arithmetic_operations()
    more_arithmetic_operations()
    modulus_floating_point()
    division_operations()
    modulus_integers()

if __name__ == '__main__':
    main()