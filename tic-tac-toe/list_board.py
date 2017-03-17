"""
_rows = [
[None, None, 'x'],
['', 'X', ''],
['  ', '  ', 'O'],
]
"""

class ListTTTBoard(object):
    """Builds a board row by row from a list"""

    def __init__(self, board=None):
        """Builds an empty board list if none exists"""
        self._rows = []
        _col = []
        if not board:
            # if not -- build empty list:
            for row in range(0, 3):
                _col = []
                for col in range(0, 3):
                    _col.append(' ')
                self._rows.append(_col)
        else:
            # if the board list exists
            self._rows = board



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
        >>> str(ListTTTBoard([['O', ' ', ' '], [' ', 'X', ' '], ['O', ' ', 'X']]))
        '|O| | |\\r\\n| |X| |\\r\\n|O| |X|\\r\\n'
        >>> str(ListTTTBoard())
        '| | | |\\r\\n| | | |\\r\\n| | | |\\r\\n'
        """
        pretty_string = ''
        for row in self._rows:
            pretty_string += '|'
            for col in row:
                pretty_string += col + '|'
            pretty_string += '\r\n'
        return pretty_string




    def place_token(self, x, y, token):
        """Place an X/O token on the board

        :param x:
        :param y:
        :param token:
        :return:
        >>> ListTTTBoard([['O', ' ', ' '], [' ', 'X', ' '], ['O', ' ', 'X']]).place_token(1, 2, 'X')
        [['O', ' ', ' '], [' ', 'X', ' '], ['O', 'X', 'X']]
        >>> ListTTTBoard().place_token(1, 1, 'O')
        [[' ', ' ', ' '], [' ', 'O', ' '], [' ', ' ', ' ']]
        """
        board_col = x
        board_row = y
        # adds token to x,y coordinates in the list
        self._rows[board_row][board_col] = token
        return self._rows


    def calc_winner(self):
        # horizontal win
        for row in self._rows:
            if len(set(row)) == 1:
                return row
        # vertical win
        col_to_rows = zip(*self._row)
        for col in col_to_rows:
            if len(set(col)) == 1:
                return col

        # diagonal win
        # _row = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l'], ['m', 'n', 'o', 'p']]
        col_index = len(self._row[0])
        back_diag = []
        for index in range(col_index):
            back_diag.append(self._row[index][index])
        front_diag = []
        for i in range(col_index - 1, -1, -1):
            front_diag += self._row[index - i][i]
        if len(set(back_diag)) == 1:
            return back_diag
        if len(set(front_diag)) == 1:
            return front_diag
        ### DECIDE ON RETURN VALUE AND CREATE A DOCTEST



def main():
    print(ListTTTBoard().place_token(1, 2, 'X'))

if __name__ == '__main__':
    main()