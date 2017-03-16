"""
_rows = [
[None, None, 'x'],
['', 'X', ''],
['  ', '  ', 'O'],
]
"""

class ListTTTBoard(object):
    """Builds a board row by row from a list"""

    def __init__(self, row_list=None):
        """Builds an empty board list if none exists"""
        self._rows = []
        _col = []
        if not row_list:
            # if not -- build empty list:
            for row in range(0, 3):
                _col = []
                for col in range(0, 3):
                    _col.append(' ')
                self._rows.append(_col)
        else:
            # if the board list exists
            self._rows = row_list



    def __repr__(self):
        """

        :return:
        >>> ListTTTBoard().__repr__()
        "ListTTTBoard([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])"
        >>> ListTTTBoard([['O', ' ', ' '], [' ', 'X', ' '], ['O', ' ', 'X']])
        ListTTTBoard([['O', ' ', ' '], [' ', 'X', ' '], ['O', ' ', 'X']])
        """
        return 'ListTTTBoard({!r})'.format(
            self._rows
        )

    def __str__(self):
        """Pretty-print version of the board

        :return:
        >>> str(ListTTTBoard())
        '| | | |/r| | | |/r| | | |/r'
        """
        pretty_string = ''
        for row in self._rows:
            pretty_string += '|'
            for col in row:
                pretty_string += col + '|'
            pretty_string += '/r'
        return '{!r}'.format(
            pretty_string
        )








    def place_token(self, x, y, token):
        pass

    def calc_winner(self):
        pass

    def __str__(self):
        pass


def main():
    ListTTTBoard()

if __name__ == '__main__':
    main()