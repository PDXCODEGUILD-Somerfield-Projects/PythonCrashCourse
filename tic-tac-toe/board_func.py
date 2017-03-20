""" 2 functions used by list_board and coords_board

* Create an empty board
* Make a 'pretty' string representation of the board
"""

def build_empty_list_board(spacer):
    """Builds an empty board as a list of lists

    :param spacer: ' ' or None to represent blank space on board
    :return: the 'empty' board as a list of lists
    """
    _rows = []
    _cols = []
    for row in range(0, 3):
        _cols = []
        for col in range(0, 3):
            _cols.append(spacer)
        _rows.append(_cols)
    return _rows

def build_pretty_string(row_list):
    """Creates a string representation from a list of rows

    :param row_list: list of row lists
    :return: string representation of the board
    """
    pretty_string = ''
    for row in row_list:
        for index, col in enumerate(row):
            if col is None:
                pretty_string += ' '
            else:
                pretty_string +=  col
            if index == 0 or index == 1:
                pretty_string += '|'
        pretty_string += '\n'
    return pretty_string

