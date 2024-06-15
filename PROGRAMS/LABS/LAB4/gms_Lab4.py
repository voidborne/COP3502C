'''
Lab4
Description: Functions
Author: Garry Scott
Date: 2024-06-12
'''

def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        f1, f2 = 0, 1
        for _ in range(2, n):
            f1, f2 = f2, f1 + f2
        return f2

def is_prime(p):
    if p <= 1:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    for i in range(3, int(p**0.5) + 1, 2):
        if p % i == 0:
            return False
    return True

def print_prime_factors(num):
    if num <= 1:
        return

    original_num = num
    factors_list = []
    divisor = 2
    while num > 1:
        while num % divisor == 0:
            factors_list.append(divisor)
            num //= divisor
        divisor += 1

    print(f"{original_num} = ", end="")
    first = True
    for factor in factors_list:
        if first:
            print(factor, end="")
            first = False
        else:
            print(f" * {factor}", end="")
    print()

def prompt_user_for_input():
    n = int(input('Pick a Fibonacci sequence position: '))
    p = int(input('Pick a number to check if it is prime: '))
    f = int(input('Pick a number to find its prime factors: '))
    return n, p, f
'''
def main():
    n, p, f = prompt_user_for_input()
    fib_num = fibonacci(n)
    prime_num = is_prime(p)
    print(f"The {n}th Fibonacci number is: {fib_num}")
    print(f"Is {p} a prime number? {'Yes' if prime_num else 'No'}")
    print_prime_factors(f)
'''

def main():
    '''
    n, p, f = prompt_user_for_input()
    fib_num = fibonacci(n)
    prime_num = is_prime(p)
    print_prime_factors(f)
    '''
    print(fibonacci(25) == 46368)
    print(is_prime(-2) == False)
    print(print_prime_factors(2475))

if __name__ == '__main__':
    main()