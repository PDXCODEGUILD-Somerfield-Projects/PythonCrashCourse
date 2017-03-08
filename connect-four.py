"""Reads a move history file and 'plays' each move in a graphic"""

from collections import OrderedDict

FIRST_MOVE = 'Y'
SECOND_MOVE = 'R'

def read_file_to_list_of_moves(file_name):
    """Opens, reads a move history file and creates a list of moves

    :param file_name:
    :return: a list of moves
    >>> read_file_to_list_of_moves('connect-four-moves.txt')
    [4, 3, 5, 6, 4, 4, 5, 3, 6, 2, 7, 7, 3, 7, 4, 5, 6, 5]
    """
    list_of_moves = []
    with open(file_name) as move_file:
        list_of_moves = move_file.read().splitlines()
    list_of_moves = [int(i) for i in list_of_moves]
    return list_of_moves

def create_color_coordinate_dictionary(list_of_moves):
    """Creates a dictionary of coordinates for each color for all moves

    :param list_of_moves
    :return: list_of_coordinates
    >>> create_color_coordinate_dictionary([4, 3, 5, 6, 4, 4, 5, 3, 6, 2, 7, 7, 3, 7, 4, 5, 6, 5])
    OrderedDict([((5, 3), 'Y'), ((5, 2), 'R'), ((5, 4), 'Y'), ((5, 5), 'R'), ((4, 3), 'Y'), ((3, 3), 'R'), ((4, 4), 'Y'), ((4, 2), 'R'), ((4, 5), 'Y'), ((5, 1), 'R'), ((5, 6), 'Y'), ((4, 6), 'R'), ((3, 2), 'Y'), ((3, 6), 'R'), ((2, 3), 'Y'), ((3, 4), 'R'), ((3, 5), 'Y'), ((2, 4), 'R')])
    """
    coordinate_to_color_dict = OrderedDict({})
    for index, column in enumerate(list_of_moves):
        if index % 2 == 0:
            color = FIRST_MOVE
        else:
            color = SECOND_MOVE
        column_count = list_of_moves[:index].count(column)
        row = column_count
        coordinates = (-(row) + 5, column-1)
        coordinate_to_color_dict.update({coordinates: color})
    return coordinate_to_color_dict


def make_empty_matrix():
    """Place tokens in order on the game board

    :param token_placement:
    :return: graphic instruction
    >>> make_empty_matrix()
    OrderedDict([((0, 0), ' '), ((0, 1), ' '), ((0, 2), ' '), ((0, 3), ' '), ((0, 4), ' '), ((0, 5), ' '), ((0, 6), ' '), ((1, 0), ' '), ((1, 1), ' '), ((1, 2), ' '), ((1, 3), ' '), ((1, 4), ' '), ((1, 5), ' '), ((1, 6), ' '), ((2, 0), ' '), ((2, 1), ' '), ((2, 2), ' '), ((2, 3), ' '), ((2, 4), ' '), ((2, 5), ' '), ((2, 6), ' '), ((3, 0), ' '), ((3, 1), ' '), ((3, 2), ' '), ((3, 3), ' '), ((3, 4), ' '), ((3, 5), ' '), ((3, 6), ' '), ((4, 0), ' '), ((4, 1), ' '), ((4, 2), ' '), ((4, 3), ' '), ((4, 4), ' '), ((4, 5), ' '), ((4, 6), ' '), ((5, 0), ' '), ((5, 1), ' '), ((5, 2), ' '), ((5, 3), ' '), ((5, 4), ' '), ((5, 5), ' '), ((5, 6), ' ')])
    """
    current_matrix = OrderedDict({})
    for row in range(0, 6):
        current_row = row
        for col in range(0, 7):
            current_column = col
            coordinates = (row, col)
            current_matrix.update({coordinates: ' '})
    return current_matrix


def make_print_string_for_matrix(current_matrix):
    """Assembles a string 'matrix' from dictionary coordinates

    :param current_matrix:
    :return: string visually representing the matrix when printed
    >>> make_print_string_for_matrix(OrderedDict([((0, 0), ' '), ((0, 1), ' '), ((0, 2), ' '), ((0, 3), ' '), ((0, 4), 'Y'), ((0, 5), 'R'), ((0, 6), ' '), ((1, 0), ' '), ((1, 1), ' '), ((1, 2), ' '), ((1, 3), ' '), ((1, 4), 'Y'), ((1, 5), ' '), ((1, 6), ' '), ((2, 0), ' '), ((2, 1), ' '), ((2, 2), ' '), ((2, 3), ' '), ((2, 4), ' '), ((2, 5), ' '), ((2, 6), ' '), ((3, 0), ' '), ((3, 1), ' '), ((3, 2), ' '), ((3, 3), ' '), ((3, 4), ' '), ((3, 5), ' '), ((3, 6), ' '), ((4, 0), ' '), ((4, 1), ' '), ((4, 2), ' '), ((4, 3), ' '), ((4, 4), ' '), ((4, 5), ' '), ((4, 6), ' '), ((5, 0), ' '), ((5, 1), ' '), ((5, 2), ' '), ((5, 3), ' '), ((5, 4), ' '), ((5, 5), ' '), ((5, 6), ' ')]))
    '\\r\\n| | | | |Y|R| |\\r\\n| | | | |Y| | |\\r\\n| | | | | | | |\\r\\n| | | | | | | |\\r\\n| | | | | | | |\\r\\n| | | | | | | |\\n'
    """
    print_string = ''
    for row, col in current_matrix:
        current_row = row
        if col == 0:
            print_string += ('\r\n|')
        print_string += (current_matrix.get((row, col), 0)) + '|'
    print_string += '\n'
    return print_string


def main():

    # input: opens a text file with the game moves and turns it into a list
    file_name = 'connect-four-moves.txt'
    list_of_moves = read_file_to_list_of_moves(file_name)

    # transforms the list into a dictionary with matrix coordinates for each move
    moves_matrix = create_color_coordinate_dictionary(list_of_moves)

    # creates a dictionary representing the coordinates of an empty matrix
    current_matrix = make_empty_matrix()

    # runs through each move, inserts the 'move' into the empty matrix and creates
    # a string that will visually represent the connect-four board
    for index, value in enumerate(moves_matrix.items()):
        current_matrix[value[0]] = moves_matrix[value[0]]

        # prints the string: shows the board for each move
        print_string = make_print_string_for_matrix(current_matrix)
        print(print_string)


if __name__ == '__main__':
    main()


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



