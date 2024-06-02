'''
Lab2_B
Description: Tax Calculator
Author: Garry Scott
Date: 2024-06-01
'''

def income_tax_calculator(total_income):
    if total_income - 11001 < 0:
        owed_taxes = 0.10 * total_income
    elif total_income - 44726 < 0:
        owed_taxes = (0.10 * 11000) + (0.12 * (total_income - 11000))
    elif total_income - 95376 < 0:
        owed_taxes = (0.10 * 11000) + (0.12 * 44725) + (0.22 * (total_income - 44725))
    elif total_income - 182101 < 0:
        owed_taxes = (0.10 * 11000) + (0.12 * (44725 - 11000)) + (0.22 * (95375 - 44725)) + (0.24 * (total_income - 95375))
    elif total_income - 231251 < 0:
        owed_taxes = (0.10 * 11000) + (0.12 * (44725 - 11000)) + (0.22 * (95375 - 44725)) + (0.24 * (182100 - 95375)) + (0.32 * (total_income - 182100))
    elif total_income - 578126 < 0:
        owed_taxes = (0.10 * 11000) + (0.12 * (44725 - 11000)) + (0.22 * (95375 - 44725)) + (0.24 * (182100 - 95375)) + (0.32 * (231250 - 182100)) + (0.35 * (total_income - 231250))
    elif total_income > 578125:
        owed_taxes = (0.10 * 11000) + (0.12 * (44725 - 11000)) + (0.22 * (95375 - 44725)) + (0.24 * (182100 - 95375)) + (0.32 * (231250 - 182100)) + (0.35 * (578125 - 231250)) + (0.37 * (total_income - 578125))
    return owed_taxes

def prompt_user_for_taxable_income():
    total_income = float(input('Enter your total income this year: '))
    owed_taxes = income_tax_calculator(total_income)
    print(f'You owe ${owed_taxes:.2f} this year.')

def main():
    prompt_user_for_taxable_income()

if __name__ == '__main__':
    main()