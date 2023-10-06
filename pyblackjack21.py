import random;
import art
import os
import sys

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10];

user_cards = [];
dealer_cards = [];
user_score = 0;
dealer_score = 0;

#functions needed

#random cards generator && score calculator:

def random_cards (target_list):
    for _ in range(2):
        random_index = random.randrange(len(cards))
        random_item = cards[random_index]
        target_list.append(random_item);

    score = sum(target_list);         
    return score;




start_msg = input("Do you want to play a game of blackjack? y or n: ").lower();
if start_msg == "y":
    os.system('cls');
    print(art.logo);
    user_score = random_cards(user_cards);
    dealer_score = random_cards(dealer_cards);
    print(f"Your cards: {user_cards}, current score: {user_score} ")
else:
    print("Exiting...")
    sys.exit()

    

