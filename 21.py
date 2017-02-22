card_1 = input('What\'s your first card? >')
card_2 = input('What\'s your second card? >')
card_3 = input('What\'s your third card? >')

aces = 0

def count_aces(card):
    if card == 'A':
        aces = 1
    return aces

def get_value(card):
    if card == 'A':
        card_value = 1
        aces += 1
    elif card == 'J' or card == 'Q' or card == 'K':
        card_value = 10
    else:
        card_value = int(card)
    return card_value

def play_hand(hand):
    if hand > 21:
        play = 'Already Busted'
    elif hand == 21:
        play = 'Blackjack!'
    elif hand >= 17:
        play = 'Stay'
    else:
        play = 'Hit'
    return play


hand_value = get_value(card_1) + get_value(card_2) + get_value(card_3)

number_of_aces = count_aces(card_1) + count_aces(card_2) + count_aces(card_3)

advice = play_hand(hand_value)

print('You have : ' + str(hand_value) + '.')
print(advice)

print(str(number_of_aces) + ' aces!')



