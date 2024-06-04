'''
Lab2_C
Description: Temperature Converter
Author: Garry Scott
Date: 2024-06-01
'''

def into_celsius_temperature_converter(start_temp_unit, temp_num):
    if start_temp_unit == 'Fahrenheit':
        celsius_temp = (temp_num - 32) * 5 / 9
    elif start_temp_unit == 'Kelvin':
        celsius_temp = temp_num - 273.15
    else:
        celsius_temp = temp_num
    return celsius_temp

def desired_temperature(celsius_temp, end_temp_unit):
    if end_temp_unit == 'Fahrenheit':
        temp = celsius_temp * 9 / 5 + 32
    elif end_temp_unit == 'Kelvin':
        temp = celsius_temp + 273.15
    else:
        temp = celsius_temp 
    return temp

def prompt_user_for_temperature():
    user_input_start_temp_str = input('Enter the unit you are converting from: ')
    user_input_end_temp_str = input('Enter the unit you are converting to: ')
    user_input_temp_num_str = float(input(f'Enter the temperature in {user_input_start_temp_str}: '))
    return user_input_start_temp_str, user_input_end_temp_str, user_input_temp_num_str

def main():
    start_temp_unit, end_temp_unit, temp_num = prompt_user_for_temperature()
    celsius_temp = into_celsius_temperature_converter(start_temp_unit, temp_num)
    converted_temp = desired_temperature(celsius_temp, end_temp_unit)
    print(f'That is {converted_temp:.1f} degrees {end_temp_unit}.')

if __name__ == '__main__':
    main()
