'''
Lab2_A
Description: Triangle classifier
Author: Garry Scott
Date: 2024-05-29
'''

def triangle_classifier(side_len_1, side_len_2, side_len_3):
    if side_len_1 == side_len_2 == side_len_3:
        triangle_type = 'equilateral'
    elif side_len_1 == side_len_2 or side_len_1 == side_len_3 or side_len_2 == side_len_3:
        triangle_type = 'isosceles'
    else:
        triangle_type = 'scalene'
    return triangle_type

def prompt_user_for_input():  
    side_len_1 = input('Side length 1: ').strip()
    side_len_2 = input('Side length 2: ').strip()
    side_len_3 = input('Side length 3: ').strip()
    triangle_type = triangle_classifier(side_len_1, side_len_2, side_len_3)
    print(f'This is an {triangle_type} triangle!')

def main(): 
    prompt_user_for_input()

if __name__ == '__main__':
    main()