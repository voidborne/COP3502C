'''
Extra Credit 1
Description: Movie Ticket Software
Author: Garry Scott
Date: 2024-05-27
'''

# Global Data Structures
showtime_list = {
    'A1' : 'post_2pm',
    'A2' : 'post_2pm',
    'A3' : 'post_2pm',
    'A4' : 'post_2pm',
    'B1' : 'pre_2pm',
    'B2' : 'post_2pm', 
    'C1' : 'pre_2pm',  
    'C2' : 'post_2pm',
    'C3' : 'post_2pm',
    'C4' : 'post_2pm'
}

adult_price_list = {
    'pre_2pm' : 11.17,
    'post_2pm' : 12.45
}

child_price_list = {
    'pre_2pm' : 8.00,
    'post_2pm' : 9.68
}

# Calculate cost of tickets
def ticket_cost_calculator(movie_choice, showtime, adult_tickets, child_tickets):
    price_status_key = f'{movie_choice}{showtime}'
    
    if price_status_key not in showtime_list:
        print('Invalid option; please restart app...')
        return None

    price_status = showtime_list[price_status_key]
    adult_price = adult_price_list[price_status]
    child_price = child_price_list[price_status]
    total_cost = adult_price * adult_tickets + child_price * child_tickets
    
    return total_cost

# Take user input
def prompt_user_for_movie_selection_and_tickets():
    print(
        'Available movies today:\n'
        'A)12 Strong:     1)2:30    2)4:40   3)7:50   4)10:50\n'
        'B)Coco:          1)12:40   2)3:45\n'
        'C)The Post:      1)12:45   2)3:35   3)7:05   4)9:55'
        )

    user_input_movie_choice_str = input('Movie choice: ').strip()
    movie_choice = user_input_movie_choice_str.upper()

    user_input_showtime_str = input('Showtime: ').strip()
    showtime = int(user_input_showtime_str)
    if f'{movie_choice}{showtime}' not in showtime_list:
        print('Invalid option; please restart app...')
        return None

    user_input_adult_tickets_str = input('Adult tickets: ').strip()
    adult_tickets = int(user_input_adult_tickets_str)
    if adult_tickets > 30:
        print('Invalid option; please restart app...')
        return None

    user_input_child_tickets_str = input('Kid tickets: ').strip()
    child_tickets = int(user_input_child_tickets_str)
    if (adult_tickets + child_tickets) > 30:
        print('Invalid option; please restart app...')
        return None

    return movie_choice, showtime, adult_tickets, child_tickets

# Main function
def main():
    
    user_input = prompt_user_for_movie_selection_and_tickets()
    
    if user_input is None:
        return
    
    else:
        movie_choice, showtime, adult_tickets, child_tickets = user_input
        total_cost = ticket_cost_calculator(movie_choice, showtime, adult_tickets, child_tickets)
        total_cost_str = f'{total_cost:.2f}'
        total_cost_str = total_cost_str.rstrip('0')

        if total_cost is not None:
            print(f'Total cost: ${total_cost_str}')
    
if __name__ == '__main__':
    main()