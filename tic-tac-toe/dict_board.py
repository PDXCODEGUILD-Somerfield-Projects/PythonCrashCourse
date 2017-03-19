"""
_coord_to_token = {
    (0, 0): 'X',
    'a1': 'O',
    '02': None,
    }
"""

class DictTTTBoard(object):
    """Builds a board with dictionary coordinates"""

    def __init__(self, board=None):
        """Builds an empty board dictionary if none exists"""
        self._coord_to_token = {}
        if not board:
            token = None
            # if not -- build empty dict of coordinates:
            for row in range(0, 3):
                for col in range(0, 3):
                    _coord = (row, col)
                    self._coord_to_token.update({_coord : token})
        else:
            # if the board list exists
            self._coord_to_token = board

    def __repr__(self):
        """Shows the board in a dictionary represenation

        coordinate = key,  token = value

        :return:
        >>> DictTTTBoard().__repr__()
        'DictTTTBoard({(0, 0): None, (0, 1): None, (0, 2): None, (1, 0): None, (1, 1): None, (1, 2): None, (2, 0): None, (2, 1): None, (2, 2): None})'
        """
        return 'DictTTTBoard({!r})'.format(
            self._coord_to_token
        )

    def __str__(self):
        """Pretty-print representation of the board

        :return:
        >>> str(DictTTTBoard({(0, 0): 'X', (0, 1): None, (0, 2): None, (1, 0): 'O', (1, 1): None, (1, 2): 'X', (2, 0): None, (2, 1): None, (2, 2): 'O'}))
        '|X| | |\\r\\n|O| |X|\\r\\n| | |O|\\r\\n'
        >>> str(DictTTTBoard())
        '| | | |\\r\\n| | | |\\r\\n| | | |\\r\\n'
        """
        # creates string representation of the board for printing
        pretty_string = '|'
        for row, col in sorted(self._coord_to_token.keys()):
            if col == 0 and row != 0:
                pretty_string += '\r\n|'
            token = self._coord_to_token.get((row, col), ' ')
            if token is not None:
                pretty_string += token + '|'
            else:
                pretty_string += ' |'
        pretty_string += '\r\n'
        return pretty_string

    def place_token(self, x, y, token):
        """Adds the token to the x,y coordinate in the board dictionary

        :param x:
        :param y:
        :param token:
        :return:
        >>> DictTTTBoard().place_token(1, 2, 'X')
        {(0, 0): None, (0, 1): None, (0, 2): None, (1, 0): None, (1, 1): None, (1, 2): None, (2, 0): None, (2, 1): 'X', (2, 2): None}
        >>> DictTTTBoard({(0, 0): 'X', (0, 1): None, (0, 2): None, (1, 0): 'O', (1, 1): None, (1, 2): 'X', (2, 0): None, (2, 1): None, (2, 2): 'O'}).place_token(2, 1, 'O')
        {(0, 0): 'X', (0, 1): None, (0, 2): None, (1, 0): 'O', (1, 1): None, (1, 2): 'O', (2, 0): None, (2, 1): None, (2, 2): 'O'}
        """
        board_col = x
        board_row = y
        # adds token to x,y coordinate key in the dictionary
        self._coord_to_token[(board_row, board_col)] = token
        return self._coord_to_token

    def calc_winner(self):
        """Evaluates the board to return the winner string 'X' or 'O'

        If no winner, returns None

        :return:
        >>> DictTTTBoard({(0, 0): None, (0, 1): 'X', (0, 2): None, (1, 0): 'O', (1, 1): 'O', (1, 2): 'O', (2, 0): 'O', (2, 1): 'X', (2, 2): 'X'}).calc_winner()
        'O'
        >>> DictTTTBoard({(0, 0): None, (0, 1): 'X', (0, 2): 'O', (1, 0): None, (1, 1): 'X', (1, 2): None, (2, 0): None, (2, 1): 'X', (2, 2): 'O'}).calc_winner()
        'X'
        >>> DictTTTBoard({(0, 0): None, (0, 1): 'X', (0, 2): 'O', (1, 0): None, (1, 1): 'O', (1, 2): 'X', (2, 0): 'O', (2, 1): 'X', (2, 2): None}).calc_winner()
        'O'
        >>> DictTTTBoard({(0, 0): 'X', (0, 1): None, (0, 2): 'O', (1, 0): None, (1, 1): 'X', (1, 2): None, (2, 0): 'O', (2, 1): 'O', (2, 2): 'X'}).calc_winner()
        'X'
        >>> DictTTTBoard({(0, 0): 'X', (0, 1): None, (0, 2): 'O', (1, 0): None, (1, 1): None, (1, 2): None, (2, 0): 'O', (2, 1): 'O', (2, 2): 'X'}).calc_winner()

        """
        tokens = ['X', 'O']
        # runs through token coordinates for X and then O
        for token in tokens:
            x = token
            list_token = []
            # create accumulative list of x and y coordinates
            list_token_x = []
            list_token_y = []
            # accumulative lists of diagonal coordinates
            list_token_diag1 = []
            list_token_diag2 = []
            # runs through each coord, token in dictionary
            # and adds coords to the list if they match
            for tuple, tok in self._coord_to_token.items():
                if token == tok:
                    list_token += [tuple]
                    # list of possible horizontal win coordinates
                    list_token_x += [tuple[0]]
                    # list of possible vertical win coordinates
                    list_token_y += [tuple[1]]
                    # list of possible back diagonal win coordinates
                    if tuple[0] == tuple[1]:
                        list_token_diag1 += [tuple]
                    # list of possible front diagonal win coordinates
                    if tuple[1] == abs(tuple[0] - 2):
                        list_token_diag2 += [tuple]
                    # evaluate lists for three coordinates in a line
                    for i in range(len(list_token_x)):
                        if list_token_x.count(i) > 2:
                            return token
                        if list_token_y.count(i) > 2:
                            return token
                    if len(list_token_diag1) > 2:
                        return token
                    if len(list_token_diag2) > 2:
                        return token
        # if there is no winner, returns value of None
        return None


def main():
    pass

if __name__ == '__main__':
    main()