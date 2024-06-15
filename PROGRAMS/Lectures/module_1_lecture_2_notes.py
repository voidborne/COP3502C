'''
Module 1 - Lecture 2 Notes
Description: Examples and notes from class
Author: Garry Scott
Date: 2024-05-15
'''

'''
Note on variable naming conventions - Always start a variable name with a letter, not a number. And no special charactors.
'''

a = 15
b = 5 
c = a - b
print('The sum of a and b is', c)
c = a + b
print('The value of a is', a, 'and the value of b is', b, 'and the sum of a and b is', c)


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