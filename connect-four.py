"""Reads a move history file and 'plays' the moves in a graphic"""

from collections import OrderedDict

def read_file_to_list_of_moves(file_name):
    """Opens, reads a move history file and creates a list of moves

    :param file_name:
    :return: a list of moves
    >>> read_file_to_list_of_moves('connect-four-moves.txt')
    [4, 3, 5, 6, 4, 4, 5, 3, 6, 2, 7, 7, 3, 7, 4, 5, 6, 5]
    """

def read_move_from_list(list_of_moves):
    """Creates a dictionary of coordinates for each color for all moves

    :param list_of_moves
    :return: list_of_coordinates
    >>> read_move_from_list([4, 3, 5, 6, 4, 4, 5, 3, 6, 2, 7, 7, 3, 7, 4, 5, 6, 5])
    OrderedDict([((5, 3), 'R'), ((5, 2), 'Y'), ((5, 4), 'R'), ((5, 5), 'Y'), ((4, 3), 'R'), ((3, 3), 'Y'), ((4, 4), 'R'), ((4, 2), 'Y'), ((4, 5), 'R'), ((5, 1), 'Y'), ((5, 6), 'R'), ((4, 6), 'Y'), ((3, 2), 'R'), ((3, 6), 'Y'), ((2, 3), 'R'), ((3, 4), 'Y'), ((3, 5), 'R'), ((2, 4), 'Y')])
    """

    coordinate_to_color_dict = OrderedDict({})
    for index, column in enumerate(list_of_moves):
        if index % 2 == 0:
            color = 'R'
        else:
            color = 'Y'
        column_count = list_of_moves[:index].count(column)
        row = column_count
        coordinates = (-(row) + 5, column-1)
        coordinate_to_color_dict.update({coordinates: color})
    return coordinate_to_color_dict

def create_dictionary_of_moves(list_of_coordinates):
    current_matrix = OrderedDict({})
    for row in range(0, 6):
        current_row = row
        for col in range(0, 7):
            current_column = col
            coordinates = (row, col)
            current_matrix.update({coordinates: ''})
    return current_matrix


def make_empty_matrix():
    """Place tokens in order on the game board

    :param token_placement:
    :return: graphic instruction
    >>> translate_to_game_board()
    """
    from collections import OrderedDict
    current_matrix = OrderedDict({})
    for row in range(0, 6):
        current_row = row
        for col in range(0, 7):
            current_column = col
            coordinates = (row, col)
            current_matrix.update({coordinates: ' '})
    return current_matrix


def make_print_string_for_matrix(current_matrix):
    print_string = ''
    for row, col in current_matrix:
        current_row = row
        if col == 0:
            print_string += ('\r\n|')
        print_string += (current_matrix.get((row, col), 0)) + '|'
    print_string += '\n'
    return print_string


def main():
    # file_name = 'connect-four-moves.txt'
    # read_file_to_list_of_moves(file_name)
    current_matrix = make_empty_matrix()
    moves_matrix = create_dictionary_of_moves([4, 3, 5, 6, 4, 4, 5, 3, 6, 2, 7, 7, 3, 7, 4, 5, 6, 5])

    for index, value in enumerate(moves_matrix.items()):
        x = value
        i = index
        current_matrix[value[0]] = moves_matrix[value[0]]

    print_string = make_print_string_for_matrix(current_matrix)
    print(print_string)


if __name__ == '__main__':
    main()

# current_print_str = ''
# for row, col in current_matrix:
#     if col == 0:
#         current_print_str += ('\r\n')
#         current_print_str += '|'
#     current_print_str += (current_matrix.get((row, col), 0)) + '|'
#     #print(current_print_str, end= '|')
# current_print_str += '\n'
# print(current_print_str)




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



