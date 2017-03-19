"""Creates a Tic-Tac-Toe game board in a list of rows format:
_rows = [
['X', ' ', 'O'],
['O', 'X', ' '],
['  ', '  ', 'O'],
]

Includes functions to place a token and calculate a winner
"""
import board_func


class ListTTTBoard(object):
    """Builds a board row by row from a list"""

    def __init__(self, board=None):
        """Builds an empty board list if none exists"""
        if not board:
            # if not -- build empty list:
            self._rows = board_func.build_empty_list_board(' ')
        else:
            # if the board list exists
            self._rows = board


    def __repr__(self):
        """Shows the tic-tac-toe board in list of lists representation

        :return: list format representation of the board
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

        :return: printable string representation of the board as a matrix
        >>> str(ListTTTBoard([['O', ' ', ' '], [' ', 'X', ' '], ['O', ' ', 'X']]))
        '|O| | |\\r\\n| |X| |\\r\\n|O| |X|\\r\\n'
        >>> str(ListTTTBoard())
        '| | | |\\r\\n| | | |\\r\\n| | | |\\r\\n'
        """
        # creates string representation of the board for printing
        pretty_string = board_func.build_pretty_string(self._rows)
        return pretty_string


    def place_token(self, x, y, token):
        """Places an X/O token on the board by x, y coordinates

        :param x: x coordinate (row)
        :param y: y coordinate (col)
        :param token: X, O -- or ' ' if empty
        :return: updates the board
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
        """Evaluates the board to return the winner string 'X' or 'O'

        If no winner, returns None

        :return: 'X' or 'O' -- or None
         >>> ListTTTBoard([['O', 'O', 'O'], ['O', 'X', ' '], ['X', ' ', 'X']]).calc_winner()
         'O'
         >>> ListTTTBoard([['X', ' ', ' '], ['X', 'O', ' '], ['X', 'O', 'O']]).calc_winner()
         'X'
         >>> ListTTTBoard([['A', ' ', 'O'], ['X', 'A', ' '], ['O', 'X', 'A']]).calc_winner()
         'A'
         >>> ListTTTBoard([['O', 'O', 'B'], [' ', 'B', 'X'], ['B', ' ', 'X']]).calc_winner()
         'B'
         >>> ListTTTBoard([['O', ' ', ' '], [' ', 'X', ' '], ['O', ' ', 'X']]).calc_winner()

        """
        # horizontal win
        for row in self._rows:
            if len(set(row)) == 1 and row[0] is not ' ':
                return row[0]
        # vertical win
        col_to_rows = zip(*self._rows)
        for col in col_to_rows:
            if len(set(col)) == 1 and col[0] is not ' ':
                return col[0]
        # diagonal win
        col_index = len(self._rows[0])
        back_diag = []
        for index in range(col_index):
            back_diag.append(self._rows[index][index])
        front_diag = []
        for i in range(col_index - 1, -1, -1):
            front_diag += self._rows[index - i][i]
        if len(set(back_diag)) == 1 and back_diag[0] is not ' ':
            return back_diag[0]
        if len(set(front_diag)) == 1 and front_diag[0] is not ' ':
            return front_diag[0]
        return None


def main():
    print(ListTTTBoard().place_token(1, 2, 'X'))

if __name__ == '__main__':
    main()