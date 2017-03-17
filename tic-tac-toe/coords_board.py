"""Creates a Tic-Tac-Toe game board in a list of coordinates in tuple format:
_token_coords = [
    (1, 1, 'X'),
    (0, 1, 'O'),
]
"""

class CoordsTTTBoard(object):
    """Builds a board row by row from a list of tuples"""

    def __init__(self, board=None):
        """Builds an empty board list if none exists"""


        if not board:
            # if not -- build empty list:
            self._token_coords = []
        else:
            # if the board list exists
            self._token_coords = board

    def __repr__(self):
        """Shows list representation of the tokens on the board

        :return:
        """
        return 'CoordsTTTBoard({!r})'.format(
            self._token_coords
        )

    def __str__(self):
        """Creates a string printable representation of the board

        :return:
        >>> str(CoordsTTTBoard([(1, 1, 'X'), (0, 1, 'O')]))
        '| |O| |\\r\\n| |X| |\\r\\n| | | |\\r\\n'
        """
        pretty_string = ''
        _rows = []
        for row in range(0, 3):
            _col = []
            for col in range(0, 3):
                _col.append(None)
        for move in self._token_coords:
            move_row = move[0]
            move_col = move[1]
            token = move[2]
            _rows[move_row][move_col] = token
        for row in _rows:
            pretty_string += '|'
            for col in row:
                if col is None:
                    pretty_string += ' |'
                else:
                    pretty_string += col + '|'
            pretty_string += '\r\n'
        return pretty_string


        # self._rows = []
        # _col = []
        # if not board:
        #     # if not -- build empty list:
        #     for row in range(0, 3):
        #         _col = []
        #         for col in range(0, 3):
        #             _col.append(' ')
        #         self._rows.append(_col)
        # else:
        #     # if the board list exists
        #     self._rows = board

def main():
    pass


if __name__ == '__main__':
    main()