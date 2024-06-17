'''
Module 2 - Lecture 4 Notes 
Description: Examples and notes from class
Author: Garry Scott
Date: 2024-05-20

Mutability
'''

total = float(input('Enter the total: '))

if total > 90:
    print('A Grade')
elif total > 80:
    print('B Grade')
elif 70 < total < 79:
    print('C Grade')
else:
    print('Work harder next time')

item_1 = 2.50
item_2 = 3.75
item_3 = 4.25

highest_cost_item = ''

def highest_price():
    if item_1 > item_2 and item_1 > item_3:
        highest_cost_item = item_1
    elif item_2 > item_1 and item_2 > item_3:
        highest_cost_item = item_2
    else:
        highest_cost_item = item_3
    print(highest_cost_item)

highest_price()

