'''
Exam 1 Practice Problems
Description: Practice Problems
Author: Garry Scott
Date: 2024-06-19
'''

'''
def min_terms(n):
    k = 1
    sum_terms = 0
    while True:
        sum_terms += (k**k)/(k*2)
        if sum_terms > n:
            return k
        k += 1

def user_input_int():
    n = int(input('Enter a number: '))
    return n

def main():
    n = user_input_int()
    k = min_terms(n)
    print(k)

if __name__=='__main__':
    main()
'''
'''
def fizzbuzz(max_num):
    for i in range(1, max_num + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i) 

def user_input_int():
    max_num = int(input('Enter a number: '))
    return max_num

def main():
    max_num = user_input_int()
    fizzbuzz(max_num)

if __name__=='__main__':
    main()
'''

def min_terms(n):
    k = 1
    _sum = 0
    while _sum < n:
        _sum += (k**k)/(2*k)
        if _sum >= n:
            return k
        k += 1

k = min_terms(10000)
print(k)