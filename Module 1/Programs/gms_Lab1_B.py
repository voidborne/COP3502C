'''
Lab1_B
Description: Total item price with sales tax
Author: Garry Scott
Date: 2024-05-25
'''

def total_price_with_tax(item_price, sales_tax):
    total_price = item_price + sales_tax
    return total_price

def sales_tax_calculation(item_price, sales_tax_percentage):
    sales_tax_amount = item_price * sales_tax_percentage
    return sales_tax_amount

def prompt_user_for_item_price_and_sales_tax():
    while True:
        try:
            user_item_price_input_str = input('Enter the price of the item (or type "exit" to quit): ').strip()
            if user_item_price_input_str.lower() == 'exit':
                print("Goodbye World!")
                break
            item_price = float(user_item_price_input_str)

            user_sales_tax_percentage_input_str = input('Enter the sales tax percentage (or typr "exit" to quit): ').strip()
            if user_sales_tax_percentage_input_str.lower() == 'exit':
                print("Goodbye World!")
                break
            sales_tax_percentage = float(user_sales_tax_percentage_input_str) / 100

            sales_tax = sales_tax_calculation(item_price, sales_tax_percentage)
            total_price = total_price_with_tax(item_price, sales_tax)

            print(f'Your total is ${total_price:.2f}')
        
        except ValueError:
            print('Invalid input. Please enter a numeric value.')

        except KeyboardInterrupt:
            print('\nGoodbye World!')
            break

def main():
    prompt_user_for_item_price_and_sales_tax()

if __name__ == '__main__':
    main()


