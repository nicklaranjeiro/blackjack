import random

SUITS = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

def deal_card():
    """Return a random card from the deck
       Deck is a tuple of (rank, suit) """
    deck = [(rank, suit) for rank in RANKS for suit in SUITS]
    return random.choice(deck)

def get_hand_score(hand):
    """Return the total score of the given hand
       If you bust and have an ace it automatically makes it a 1 """
    score = 0
    num_aces = 0
    for card in hand:
        rank = card[0]
        if rank.isdigit():
            score += int(rank)
        elif rank in ['Jack', 'Queen', 'King']:
            score += 10
        elif rank == 'Ace':
            num_aces += 1
            score += 11
    while num_aces > 0 and score > 21:
        score -= 10
        num_aces -= 1
    return score

def play_blackjack():
    """Play a game of Blackjack"""
    print("Welcome to Blackjack!\n")
    user_hand = [deal_card(), deal_card()]
    print("Your hand:")
    for card in user_hand:
        print(card[0], "of", card[1])
    user_score = get_hand_score(user_hand)
    print("Total score:", user_score)
    while True:
        if user_score == 21:
            print("Congratulations, you got a Blackjack!")
            return
        elif user_score > 21:
            print("Sorry, you busted!")
            return
        else:
            draw_card = input("Do you want to draw another card? (y/n): ")
            if draw_card.lower() == 'y':
                new_card = deal_card()
                user_hand.append(new_card)
                print("You drew:", new_card[0], "of", new_card[1])
                user_score = get_hand_score(user_hand)
                print("Total score:", user_score)
            else:
                break
    dealer_hand = [deal_card()]
    dealer_score = get_hand_score(dealer_hand)
    print("\nDealer's hand:")
    print(dealer_hand[0][0], "of", dealer_hand[0][1])
    while dealer_score < 16:
        new_card = deal_card()
        dealer_hand.append(new_card)
        dealer_score = get_hand_score(dealer_hand)
        print("Dealer drew:", new_card[0], "of", new_card[1])
        print("Total score:", dealer_score)
    if dealer_score == 21:
        print("\nSorry, dealer got a Blackjack!")
        return
    elif dealer_score > 21:
        print("\nCongratulations, dealer busted! You win!")
        return
    else:
        print("\nYour score:", user_score)
        print("Dealer's score:", dealer_score)
        if user_score > dealer_score:
            print("Congratulations, you win!")
        elif user_score == dealer_score:
            print("It's a tie!")
        else:
            print("Sorry, you lose!")

play_blackjack()