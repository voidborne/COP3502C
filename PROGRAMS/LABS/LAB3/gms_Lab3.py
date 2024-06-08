'''
Lab3
Description: Scientific Calculator
Author: Garry Scott
Date: 2024-06-04
'''

import math

calculation_result = 0.0
calculation_sum = 0.0
calculation_num = 0

def calculation_counter(calculation_num):
    calculation_num += 1
    return calculation_num

def average_calculator(calculation_sum, calculation_num):
    calculation_avg = calculation_sum / calculation_num
    return calculation_avg

def sum_of_calculations(calculation_sum, calculation_result):
    calculation_sum += calculation_result
    return calculation_sum

def calculator(user_input_int, operand_1, operand_2):
    if user_input_int == 1:
        return operand_1 + operand_2
    elif user_input_int == 2:
        return operand_1 - operand_2
    elif user_input_int == 3:
        return operand_1 * operand_2
    elif user_input_int == 4:
        if operand_2 == 0:
            print('Error: Invalid Input!')
            return None
        return operand_1 / operand_2
    elif user_input_int == 5:
        return operand_1 ** operand_2
    elif user_input_int == 6:
        return math.log(operand_2, operand_1)

def prompt_user_for_input(calculation_result, calculation_sum, calculation_num):
    while True:
        print(
            '\n'
            f'Current Result: {calculation_result}\n'
            '\n'
            'Calculator Menu\n'
            '---------------\n'
            '0. Exit Program\n'
            '1. Addition\n'
            '2. Subtraction\n'
            '3. Multiplication\n'
            '4. Division\n'
            '5. Exponentiation\n'
            '6. Logarithm\n'
            '7. Display Average\n'
            '\n'
        )
        user_input_int = int(input('Enter Menu Selection: '))
        if user_input_int == 0:
            print('Thanks for using this calculator. Goodbye!')
            break
        elif user_input_int in range(1, 7):
            operand_1_input = input('Enter first operand: ')
            operand_2_input = input('Enter second operand: ')
            operand_1 = calculation_result if operand_1_input == 'RESULT' else float(operand_1_input)
            operand_2 = calculation_result if operand_2_input == 'RESULT' else float(operand_2_input)
            new_result = calculator(user_input_int, operand_1, operand_2)
            if new_result is not None:
                calculation_result = new_result
                calculation_sum = sum_of_calculations(calculation_sum, calculation_result)
                calculation_num = calculation_counter(calculation_num)
                print(f'Current Result: {calculation_result}')
        elif user_input_int == 7:
            if calculation_num != 0:
                calculation_avg = average_calculator(calculation_sum, calculation_num)
                print(
                    f'Sum of calculations: {calculation_sum}\n'
                    f'Number of calculations: {calculation_num}\n'
                    f'Average of calculations: {calculation_avg}\n'
                )
            else:
                print('Error: No calculations yet to average!')
        else:
            print('Error: Invalid selection!')

def main():
    global calculation_result, calculation_sum, calculation_num
    prompt_user_for_input(calculation_result, calculation_sum, calculation_num)

if __name__ == '__main__':
    main()
