'''
Extra Credit 1
Description: Movie Ticket Software
Author: Garry Scott
Date: 2024-05-27
'''

ticket_cost = [
    ['adult', {'pre_2pm' : True}],
    ['adult', {'pre_2pm' : False}],
    ['child', {'pre_2pm' : True}], 
    ['child', {'pre_2pm' : False}]
]

print(ticket_cost[1][1]['pre_2pm'])

def prompt_user_for_movie_selection_and_tickets():
    print(
        'Available movies today:\n'
        'A)12 String:     1)2:30    2)4:40   3)7:50   4)10:50\n'
        'B)Coco:          1)12:40   2)3:45\n'
        'C)The Post:      1)12:45   2)3:35   3)7:05   4)9:55'
        )

    user_input_movie_choice_str = input('Movie choice: ').strip()
    movie_choice = user_input_movie_choice_str.upper()

    user_input_showtime_str = input('Showtime: ').strip()
    showtime = int(user_input_showtime_str)

    user_input_adult_tickets_str = input('Adult tickets: ').strip()
    adult_tickets = int(user_input_adult_tickets_str)

    user_input_child_tickets_str = input('Child tickets: ').strip()
    child_tickets = int(user_input_child_tickets_str)

def main():
    prompt_user_for_movie_selection_and_tickets()

if __name__ == '__main__':
    main()