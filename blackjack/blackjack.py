import random

SUIT = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
RANK = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', 'Jack', 'Queen', 'King')

class Card(object):
    def __init__(self, rank, suit):
        """Store suit and card number
        """

        self.rank = rank
        self.suit = suit


    def __repr__(self):
        """

        :return:
        >>> x = Card('Jack', 'Hearts')
        >>> x.__repr__()
        "('Jack', 'Hearts')"
        """
        return '({!r}, {!r})'.format(
            self.rank,
            self.suit,
        )

        # @property
        # def suit(self):
        #     return self._suit
        #
        # @suit.setter
        # def suit(self, s):
        #     if s not in SUIT: raise Exception \
        #         ('Suit must be Hearts, Diamonds, Clubs, or Spades.')
        #     self._suit = s
        #
        # @property
        # def rank(self):
        #     return rank._rank
        #
        # @rank.setter
        # def rank(self, r):
        #     if r not in RANK: raise Exception \
        #         ('Rank must be 1 - 9, Jack, Queen, King, or Ace.')
        #     self._rank = r


class Hand(object):
    """ List of playing cards """

    # def __init__(self, card_1, card_2):
    #     """Store a list of cards in hand"""
    #     # card_list = []
    #     # self.card
    #     # for card in card_list:
    #     #     hand.append(Card(card[0], card[1]))
    #     card_1 = Card(card_1[0], card_1[1])
    #     card_2 = Card(card_2[0], card_2[1])
    #     self.card_list = [card_1, card_2]

    def __init__(self, card_list_in=None):
        self.card_list = []
        if card_list_in is not None:
            for card in card_list_in:
                new_card = Card(card[0], card[1])
                self.card_list.append(new_card)


    def __repr__(self):
        """

        :param card_list:
        :return:
        >>> x = Hand([('Jack', 'Hearts'), ('4', 'Clubs')])
        >>> x.__repr__()
        "[('Jack', 'Hearts'), ('4', 'Clubs')]"
        """
        return '{!r}'.format(
            self.card_list
        )

    def add_card_to_hand(self, new_card):
        """

        :param self:
        :return:
        >>> hand = Hand([('4', 'Hearts'), ('2', 'Spades')])
        >>> hand.add_card_to_hand(('7', 'Diamonds'))
        >>> hand.card_list
        [('4', 'Hearts'), ('2', 'Spades'), ('7', 'Diamonds')]
        """
        self.card_list.append(Card(new_card[0], new_card[1]))

    def score_hand(self):
        """

        :return:
        >>> Hand([('7', 'Hearts'), ('2', 'Diamonds')]).score_hand()
        9
        >>> Hand([('Ace', 'Spades'), ('Queen', 'Spades')]).score_hand()
        21
        >>> Hand([('Ace', 'Spades'), ('7', 'Diamonds'), ('Queen', 'Hearts')]).score_hand()
        18
        """
        card_score = 0
        hand_score = 0
        aces = 0
        for card in self.card_list:
            if card.rank.isdigit():
                card_score = int(card.rank)
            elif card.rank in ['Jack', 'Queen', 'King']:
                card_score = 10
            elif card.rank == 'Ace':
                card_score = 1
                aces += 1
            hand_score += card_score
        if aces > 0 and hand_score + 10 <= 21:
            hand_score += 10
            if aces > 1 and hand_score + 10 <= 21:
                hand_score += 10
        return hand_score


    def is_over_twenty_one(self):
        """

        :param self:
        :return:
        >>> Hand([('Ace', 'Spades'), ('Queen', 'Spades')]).is_over_twenty_one()
        False
        >>> Hand([('Queen', 'Spades'), ('9', 'Diamonds'), ('8', 'Hearts')]).is_over_twenty_one()
        True
        >>> Hand([('King', 'Hearts'), ('2', 'Diamonds')]).is_over_twenty_one()
        False
        """
        is_over = False
        score = self.score_hand()
        if int(score) > 21:
            is_over = True
        return is_over

    def add_hand(self, user_card_str):
        """

        :param user_card_str:
        :return:
        >>> Hand().add_hand('10S, QC, AD, 2H')
        [('10', 'Spades'), ('Queen', 'Clubs'), ('Aces', 'Diamonds'), ('2', 'Hearts')]

        # >>> Hand().add_hand('10S, QC, AD, 2H')
        # [('10', 'Spades'), ('Queen', 'Clubs'), ('Aces', 'Diamonds'), ('2', 'Hearts')]
        """
        # hand = '10S, QC, 1D, 2H'
        suit_dict = {'S': 'Spades', 'C': 'Clubs', 'D': 'Diamonds', 'H': 'Hearts'}
        rank_dict = {'A': 'Aces', 'J': 'Jack', 'Q': 'Queen', 'K': 'King'}
        for card in user_card_str.split(','):
            card = card.strip()
            if card[0].isdigit():
                if card[1].isdigit():
                    rank = str(card[:2])
                else:
                    rank = str(card[:1])
            else:
                rank = rank_dict.get(card[0])
            s = card[len(card) -1]
            suit = suit_dict.get(card[len(card)-1])
            c = Card(rank, suit)
            self.card_list.append(c)
        return self.card_list
#
class Deck(object):
    """Deck of playing cards in a list"""

    def __init__(self, card_list=None):
        if card_list is not None:
            self.deck_list = card_list
        else:
            self.deck_list = []
            for suit in SUIT:
                for rank in RANK:
                    self.deck_list.append(Card(rank, suit))

    def __repr__(self):
        """

        :return:
        >>> x = Deck()
        >>> x.__repr__()
        "[('Ace', 'Clubs'), ('2', 'Clubs'), ('3', 'Clubs'), ('4', 'Clubs'), ('5', 'Clubs'), ('6', 'Clubs'), ('7', 'Clubs'), ('8', 'Clubs'), ('9', 'Clubs'), ('Jack', 'Clubs'), ('Queen', 'Clubs'), ('King', 'Clubs'), ('Ace', 'Diamonds'), ('2', 'Diamonds'), ('3', 'Diamonds'), ('4', 'Diamonds'), ('5', 'Diamonds'), ('6', 'Diamonds'), ('7', 'Diamonds'), ('8', 'Diamonds'), ('9', 'Diamonds'), ('Jack', 'Diamonds'), ('Queen', 'Diamonds'), ('King', 'Diamonds'), ('Ace', 'Hearts'), ('2', 'Hearts'), ('3', 'Hearts'), ('4', 'Hearts'), ('5', 'Hearts'), ('6', 'Hearts'), ('7', 'Hearts'), ('8', 'Hearts'), ('9', 'Hearts'), ('Jack', 'Hearts'), ('Queen', 'Hearts'), ('King', 'Hearts'), ('Ace', 'Spades'), ('2', 'Spades'), ('3', 'Spades'), ('4', 'Spades'), ('5', 'Spades'), ('6', 'Spades'), ('7', 'Spades'), ('8', 'Spades'), ('9', 'Spades'), ('Jack', 'Spades'), ('Queen', 'Spades'), ('King', 'Spades')]"

        """
        return '{!r}'.format(
            self.deck_list
        )


    def return_shuffled(self):
        """

        :return:

        """
        random.shuffle(self.deck_list)


    def draw_a_card(self):
        """

        :return:
        >>> Deck([('Ace', 'Clubs'), ('4', 'Spades'), ('Queen', 'Clubs'), ('Jack', 'Diamonds')]).draw_a_card()
        ('Ace', 'Clubs')
        """
        top_card = self.deck_list.pop(0)
        return top_card

    def is_deck_empty(self):
        """

        :return:
        >>> Deck([('3', 'Clubs'), ('4', 'Clubs'), ('5', 'Clubs'), ('6', 'Clubs')]).is_deck_empty()
        False
        >>> Deck([]).is_deck_empty()
        True
        """
        is_empty = False
        if not self.deck_list:
            is_empty = True
        return is_empty


def main():
    deck = Deck()
    deck.return_shuffled()
    print(deck.__repr__())
    while not deck.is_deck_empty():
        top_card = deck.draw_a_card()
        print(top_card)
    print(deck.__repr__())

if __name__ == '__main__':
    main()