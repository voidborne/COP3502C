'''
Project 2A
Description: Project 2 - Standalone Menu
Author: Garry Scott
Date: 2024-06-17
'''

import console_gfx

def display_menu():
    print(
        '\n\n'
        'RLE Menu\n'
        '--------\n'
        '0. Exit\n'
        '1. Load File\n'
        '2. Load Test Image\n'
        '3. Read RLE String\n'
        '4. Read RLE Hex String\n'
        '5. Read Data Hex String\n'
        '6. Display Image\n'
        '7. Display RLE Hex String\n'
        '8. Display Hex RLE Data\n'
        '9. Display Hex Flat Data\n'
    )

def prompt_user_for_input(image_data):
    file_name = None
    user_input_int = int(input('Select a Menu Option: '))
    if user_input_int == 0:
        exit()
    elif user_input_int == 1:
        file_name = input('Enter the name of the file: ')
        image_data = console_gfx.load_file(file_name)
    elif user_input_int == 2:
        image_data = console_gfx.test_image
        print('Test image data is loaded')
    elif user_input_int == 6:
        console_gfx.display_image(image_data)
    return image_data

def main():
    print(
        'Welcome to the RLE image encoder!\n\n'
        'Displaying Spectrum Image:'
    )
    
    console_gfx.display_image(console_gfx.test_rainbow)
    
    image_data = None
    while True:
        display_menu()
        image_data = prompt_user_for_input(image_data)

if __name__=='__main__':
    main()