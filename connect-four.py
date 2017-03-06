"""Reads a move history file and 'plays' the moves in a graphic"""

def read_file_to_list_of_moves(file_name):
    """Opens, reads a move history file and creates a list of moves

    :param file_name:
    :return: a list of moves
    >>> read_file_to_list_of_moves('connect-four-moves.txt')
    [4, 3, 5, 6, 4, 4, 5, 3, 6, 2, 7, 7, 3, 7, 4, 5, 6, 5]
    """

def create_game_board_graphic():
    """Produces string representation of connect four game board

    :return:
    >>>
    '| | | | | | | |\\n| | | | | | | |\\n| | | | | | | |\\n| | | | | | | |\\n| | | | | | | |\\n| | | | | | | |'
    """

def read_move_from_list(list_of_moves):
    """Creates a list of color and coordinates for all moves

    :param list_of_moves
    :return: list_of_coordinates
    >>> read_move_from_list([4, 3, 5, 6, 4, 4, 5, 3, 6, 2, 7, 7, 3, 7, 4, 5, 6, 5])
    [['R', 4, 0], ['Y', 3, 0], ['R', 5, 0], ['Y', 6, 0], ['R', 4, 1], ['Y', 4, 2], ['R', 5, 1], ['Y', 3, 1], ['R', 6, 1], ['Y', 2, 0], ['R', 7, 0], ['Y', 7, 1], ['R', 3, 2], ['Y', 7, 2], ['R', 4, 3], ['Y', 5, 2], ['R', 6, 2], ['Y', 5, 3]]
    """
    list_of_coordinates = []
    for index, column in enumerate(list_of_moves):
        coordinates = []
        if index % 2 == 0:
            color = 'R'
        else:
            color = 'Y'
        column_count = list_of_moves[:index].count(column)
        row = column_count
        coordinates.extend([color, column, row])
        list_of_coordinates.append(coordinates)
    return list_of_coordinates

def translate_to_game_board(list_of_coordinates):
    """Place tokens in order on the game board

    :param token_placement:
    :return: graphic instruction
    >>>
    """
# def check_horizontal_four(tokens_placement):
#
# def check_vertical_four(tokens_placement):
#
# def check_diagonal_four(tokens_placement):
#
# def determine_winner(horizontal_four, vertical_four, diagonal_four):
#     """
#
#     :param horizontal_four:
#     :param vertical_four:
#     :param diagonal_four:
#     :return:
#     """



