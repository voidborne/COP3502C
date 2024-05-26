'''
Lab1_A
Description: Celsius to Fahrenheit Converter
Author: Garry Scott
Date: 2024-05-25
'''

def celsius_to_fahrenheit(celsius_temp):
    fahrenheit_temp = celsius_temp * 1.8 + 32
    return fahrenheit_temp

def prompt_user_for_temperature():
    
    while True:
        try:
            user_input_str = input('Enter the temperature in Celsius (or type "exit" to quit): ').strip()
            if user_input_str.lower() == 'exit':
                print('Goodbye World!')
                break
            
            celsius_temp = float(user_input_str)
            fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
            
            print(f'That is {fahrenheit_temp:.1f} degrees Fahrenheit!')
        
        except ValueError:
            print('Invalid input. Please enter a numeric value.')
        
        except KeyboardInterrupt:
            print('\nGoodbye World!')
            break

def main():
    prompt_user_for_temperature()

if __name__ == '__main__':
    main()

'''
#Unit Test

import unittest

class TestTemperatureConverter(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        """Test conversion from Celsius to Fahrenheit."""
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32)
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212)
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40)
        self.assertAlmostEqual(celsius_to_fahrenheit(37), 98.6, places=1)

if __name__ == '__main__':
    unittest.main()
'''

