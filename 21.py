# user inputs the 3 cards dealt
card_1 = input('What\'s your first card? >')
card_2 = input('What\'s your second card? >')
card_3 = input('What\'s your third card? >')

# function to determine if a card is an ace
def count_aces(card):
    if card == 'A':
        aces = 1
    else:
        aces = 0
    # return a value of 1 if the card is an ace, 0 if not
    return aces

# function to calculate the value of a card (aces default to 1)
def get_value(card):
    # checks if the card is an ace
    if card == 'A':
        # if yes, assigns a value of 1
        card_value = 1
    # checks if the card is a suit card
    elif card == 'J' or card == 'Q' or card == 'K':
        # assigns a value of 10 to any suit card
        card_value = 10
    else:
        # if it's not a suit card or an ace
        # assumes it is an integer and assigns the value of the card
        card_value = int(card)
    return card_value

# function to determine the advice on the play
def play_hand(hand):
    # assigns the advice by checking the value of the hand
    # by comparing against descending limits
    if hand > 21:
        play = 'Already Busted'
    elif hand == 21:
        play = 'Blackjack!'
    elif hand >= 17:
        play = 'Stay'
    else:
        play = 'Hit'
    return play

# function to check if an ace card should be played at a value of 11
def check_aces(hand, aces):
    if aces > 0:
        if hand < 21:
            # if an 11 should be played,
            # it adds the additional 10 to the hand
            # (the ace was already counted at the value of 1)
            if hand + 10 < 21:
                hand += 10
    return hand

# uses count_aces function to add up the number of aces in the hand
number_of_aces = count_aces(card_1) + count_aces(card_2) + count_aces(card_3)

# uses get_value function to determine the value of the hand
hand_value = get_value(card_1) + get_value(card_2) + get_value(card_3)

# uses check_aces function to determine if an ace should use be used at a value of 11
hand_value = check_aces(hand_value, number_of_aces)

# runs the play_hand function to determine what advice to give the user
advice = play_hand(hand_value)

# outputs the value of the hand and the advice to the user:
print('You have : ' + str(hand_value) + '... ' + advice)

