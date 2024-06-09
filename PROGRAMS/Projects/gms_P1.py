'''
Lab3
Description: Project 1 - Blackjack Game
Author: Garry Scott
Date: 2024-06-07
'''

import p1_random as p1

rng = p1.P1Random()

games_played = 0
player_wins = 0
dealer_wins = 0
ties = 0
player_hand = 0

def menu():
    print(
       '1. Get another card\n'
       '2. Hold hand\n'
       '3. Print statistics\n'
       '4. Exit' 
    )

def card_value(card):
    if card == 1:
        return "ACE", 1
    elif card == 11:
        return "JACK", 10
    elif card == 12:
        return "QUEEN", 10
    elif card == 13:
        return "KING", 10
    else:
        return str(card), card

def get_another_card():
    global player_hand
    card_num = rng.next_int(13) + 1
    card_name, card_value_num = card_value(card_num)
    player_hand += card_value_num
    print(f"\nYour card is a {card_name}!")
    print(f"Your hand is: {player_hand}")
    
    if player_hand == 21:
        print("\nBLACKJACK! You win!")
        global player_wins
        player_wins += 1
        main(games_played)
    elif player_hand > 21:
        print("\nYou exceeded 21! You lose.")
        global dealer_wins
        dealer_wins += 1
        main(games_played)
    else:
        menu()
        prompt_user_for_input()

def hold_hand():
    global player_hand, dealer_wins, player_wins, ties
    dealer_hand = rng.next_int(11) + 16
    print(f"\nDealer's hand: {dealer_hand}")
    print(f"Your hand is: {player_hand}")
    
    if dealer_hand > 21:
        print("\nYou win!")
        player_wins += 1
    elif dealer_hand == player_hand:
        print("\nIt's a tie! No one wins!")
        ties += 1
    elif dealer_hand > player_hand:
        print("\nDealer wins!")
        dealer_wins += 1
    else:
        print("\nYou win!")
        player_wins += 1
    
    main(games_played)

def print_statistics():
    print(f"Number of Player wins: {player_wins}")
    print(f"Number of Dealer wins: {dealer_wins}")
    print(f"Number of tie games: {ties}")
    print(f"Total # of games played is: {games_played}")
    if games_played > 0:
        win_percentage = (player_wins / games_played) * 100
        print(f"Percentage of Player wins: {win_percentage:.1f}%")
    else:
        print("Percentage of Player wins: 0.0%")
    menu()
    prompt_user_for_input()

def prompt_user_for_input():
    try:
        user_input_int = int(input('Choose an option: '))
        if user_input_int == 1:
            get_another_card()
        elif user_input_int == 2:
            hold_hand()
        elif user_input_int == 3:
            print_statistics()
        elif user_input_int == 4:
            print("\nExiting the game...")
            exit()
        else:
            print(
                'Invalid input!\n'
                'Please enter an integer value between 1 and 4'
            )
            menu()
            prompt_user_for_input()
    except ValueError:
        print(
            'Invalid input!\n'
            'Please enter an integer value between 1 and 4'
        )
        menu()
        prompt_user_for_input()

def main(game_count):
    global games_played, player_hand
    while True:
        games_played += 1
        player_hand = 0
        print(f"\nSTART GAME #{games_played}")
        
        # Deal the first card to the player
        card_num = rng.next_int(13) + 1
        card_name, card_value_num = card_value(card_num)
        player_hand += card_value_num
        print(f"Your card is a {card_name}!")
        print(f"Your hand is: {player_hand}")
        
        menu()
        prompt_user_for_input()

if __name__ == '__main__':
    main(games_played)
