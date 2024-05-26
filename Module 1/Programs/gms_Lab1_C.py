'''
Lab1_B
Description: Number of days between dates calculation
Author: Garry Scott
Date: 2024-05-25
'''

def calculate_difference_in_dates(year1, month1, day1, year2, month2, day2):
    
    total_days_date1 = year1 * 360 + month1 * 30 + day1
    total_days_date2 = year2 * 360 + month2 * 30 + day2
    difference_in_days = abs(total_days_date1 - total_days_date2)
    
    return difference_in_days

def main():
    
    y1 = int(input('Enter the year for date 1: '))
    m1 = int(input('Enter the month for date 1: '))
    d1 = int(input('Enter the day for date 1: '))
    y2 = int(input('Enter the year for date 2: '))
    m2 = int(input('Enter the month for date 2: '))
    d2 = int(input('Enter the day for date 2: '))
    
    total_num_days = calculate_difference_in_dates(y1, m1, d1, y2, m2, d2)
    
    print(f'The difference between {m1}/{d1}/{y1} and {m2}/{d2}/{y2} is {total_num_days} days!')

if __name__ == "__main__":
    main()