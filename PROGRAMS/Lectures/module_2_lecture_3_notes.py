'''
Module 2 - Lecture 3 Notes 
Description: Examples and notes from class
Author: Garry Scott
Date: 2024-05-17
'''

a = 15
b = 5 
c = a - b
print('The sum of a and b is', c)
c = a + b
print('The value of a is', a, 'and the value of b is', b, 'and the sum of a and b is', c)


var = 'Garry'
var2 = 32


'''
sep and end will motify the spaces and end of strings
'''


print('My name is', var, sep = '****')

print('My name is', var, 'And my age is', var2, sep = '****')

print('My name is', var, 'And my age is', var2, sep = '****', end = '!')
x = 3.2
print(x)

print(type(round(x)))

# Grade calculator

score = 98

print(f'The final score is: {score}')

pi = 3.14159
print(f'The value of pi is {pi:.2f}')

a = 20
b = 5
c = 4

x = b+a/b*c+c-b
print(x)
print(type(x))

x = (a + b * c) / a
print(2 * x + 5)

a = 20
b = 23 // 4
c = b + 7
d = c % 10

print(d)