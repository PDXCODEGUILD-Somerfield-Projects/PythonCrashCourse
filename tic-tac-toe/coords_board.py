"""Creates a Tic-Tac-Toe game board in a list of coordinates in tuple format:
_token_coords = [
    (1, 1, 'X'),
    (0, 1, 'O'),
]
"""
import list_board

class CoordsTTTBoard(object):
    """Builds a board row by row from a list of tuples"""

    def __init__(self, board=None):
        """Builds an empty list of token moves if none exists"""

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
        >>> str(CoordsTTTBoard())
        '| | | |\\r\\n| | | |\\r\\n| | | |\\r\\n'
        """
        # function from list_board to create list of empty rows
        _row_list = list_board.build_empty_list_board(None)
        # fills the empty board with moves
        for move in self._token_coords:
            move_row = move[0]
            move_col = move[1]
            token = move[2]
            _row_list[move_row][move_col] = token
        # creates a string representation of the board from list_board function
        pretty_string = list_board.build_pretty_string(_row_list)
        return pretty_string

    def place_token(self, move):
        """Add the token move to the list of moves

        :param move:
        :return:
        >>> CoordsTTTBoard().place_token((1, 1, 'X'))
        [(1, 1, 'X')]
        >>> CoordsTTTBoard([(1, 2, 'X'), (0, 1, 'O')]).place_token((1, 1, 'X'))
        [(1, 2, 'X'), (0, 1, 'O'), (1, 1, 'X')]
        """
        self._token_coords.append(move)
        return self._token_coords


    def calc_winner(self):
        """Calculates winner from token coordinates

        :return: winner as string 'X', 'O', or None
        >>> CoordsTTTBoard().calc_winner()
        None
        >>> CoordsTTTBoard([(1, 1, 'X'), (0, 2, 'O'), (0, 1, 'X'), (2, 2, 'O'), (2, 1, 'X')])
        X
        """
        SQR = 3
        # for move in board:
        # in each row
        token_list = ['X', 'O']
        for index in range(SQR):
            # checks for horizontal matches through an index of rows
            filtered_x = []
            filtered_x = [tup for tup in self._token_coords if tup[0] == index]
            if len(filtered_x) >= SQR:
                for i in range(len(token_list)):
                    token = token_list[i]
                    filtered_x_token = [tup for tup in filtered_x if tup[2] == token]
                    if len(filtered_x_token) >= SQR:
                        return token
            # checks for vertical matches through an index of columns
            filtered_y = []
            filtered_y = [tup for tup in self._token_coords if tup[1] == index]
            if len(filtered_y) >= SQR:
                for i in range(len(token_list)):
                    token = token_list[i]
                    filtered_y_token = [tup for tup in filtered_y if tup[2] == token]
                    if len(filtered_y_token) >= SQR:
                        return token

        # check for front diagonal by checking row against col
        front_diag = [tup for tup in self._token_coords if tup[1] == (abs(tup[0] - (SQR - 1)))]
        if len(front_diag) >= SQR:
            for i in range(len(token_list)):
                token = token_list[i]
                filtered_front_diag_token = [tup for tup in front_diag if tup[2] == token]
                if len(filtered_front_diag_token) >= SQR:
                    return token

        # checks for back diagonal by comparing row to col
        back_diag = [tup for tup in self._token_coords if tup[0] == tup[1]]
        if len(back_diag) >= SQR:
            for i in range(len(token_list)):
                token = token_list[i]
                filtered_back_diag_token = [tup for tup in back_diag if tup[2] == token]
                if len(filtered_back_diag_token) >= SQR:
                    return token
        return None






def main():
    print(CoordsTTTBoard([(1, 1, 'X'), (0, 2, 'O'), (0, 1, 'X'), (2, 2, 'O'), (2, 1, 'X')]).calc_winner())


if __name__ == '__main__':
    main()