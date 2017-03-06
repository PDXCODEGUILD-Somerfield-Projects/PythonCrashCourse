"""Opens a user-defined txt or csv file and prints the file as a table

Once the user enters file name at the command line, function determines
whether file is a txt (space-delimited) or csv file and creates a list of
each line/row inside a list. The length of the longest word in each 'column'
is determined and then a table is formatted to a string and the string is
printed to the command line."""

import csv
from sys import argv


COLUMN_CHAR = '|'
LINE_CHAR = '-'

def make_a_list_of_rows_from_csv(csv_file):
    """Opens the user-specified csv file and transforms the data into a list

    :param csv_file:
    :return:
    >>> make_a_list_of_rows_from_csv('test.csv')
    [['tree', 'flower', 'color', 'instrument'], ['willow', 'lily', 'grey', 'violin'], ['dogwood', 'rose', 'blue', 'guitar']]
    """
    list_of_rows = []
    file = csv.reader(open(csv_file))
    for line in file:
        list_of_rows.append(line)
    return list_of_rows


def make_a_list_of_rows_from_txt(text_file):
    """Opens the user-specified-file and transforms space-delimited data into a list

    :param text_file:
    :return: list of items by row in a list of the whole
    >>> make_a_list_of_rows_from_txt('test.txt')
    [['tree', 'flower', 'color', 'instrument'], ['willow', 'lily', 'grey', 'violin'], ['dogwood', 'rose', 'blue', 'guitar']]
    """
    list_of_rows = []
    file = open(text_file, 'r')
    for list_line in file.readlines():
        list_of_rows.append(list_line.split())
    return list_of_rows


def get_max_length_of_columns(list_by_rows):
    """Gets the length of the longest item in each 'column' of the list

    :param list_by_rows:
    :return: a list of max lengths of each 'column'
    >>> get_max_length_of_columns([['tree', 'flower', 'color', 'instrument'], ['willow', 'lily', 'grey', 'violin'], ['dogwood', 'rose', 'blue', 'guitar']])
    [7, 6, 5, 10]
    """
    max_length_list = ([max(len(str(x)) for x in line) for line in zip(*list_by_rows)])
    return max_length_list


def create_pipe_line_string(max_length_list):
    """Creates a row/line string with column separators to use in the table

    :param max_length_list:
    :return: a 'line' string made up of COLUMN_CHAR and LINE_CHAR fitting each column length
    >>> create_pipe_line_string([7, 6, 5, 10])
    '|-------|------|-----|----------|\\n'
    """
    pipe_line_string = COLUMN_CHAR
    for column_length in max_length_list:
        pipe_line_string += LINE_CHAR * column_length + COLUMN_CHAR
    pipe_line_string += '\n'
    return pipe_line_string


def create_table_string(list_of_rows, max_length_list):
    """Creates a 'table' to print in the form of a string

    :param list_of_rows:
    :param max_length_list:
    :return:
    >>> create_table_string([['tree', 'flower', 'color', 'instrument'], ['willow', 'lily', 'grey', 'violin'], ['dogwood', 'rose', 'blue', 'guitar']], [7, 6, 5, 10])
    '|-------|------|-----|----------|\\n|tree   |flower|color|instrument|\\n|-------|------|-----|----------|\\n|willow |lily  |grey |violin    |\\n|dogwood|rose  |blue |guitar    |\\n|-------|------|-----|----------|\\n'
    """
    table_string = ''
    pipe_line_string = create_pipe_line_string(max_length_list)
    for index, list_of_rows in enumerate(list_of_rows):
        if index < 2:
            table_string += pipe_line_string
        for i, item in enumerate(list_of_rows):
            justify_by = max_length_list[i]
            table_string += COLUMN_CHAR + str(item.ljust(justify_by))
        table_string += COLUMN_CHAR + '\n'
    table_string += pipe_line_string
    return table_string


def main():
    """Takes a user-specified-file at the command line and prints it in a 'table' format

    First turns a space-delimited text file into a list, then layers the lists into a string
    separated into 'rows' and 'columns' and finally, prints the string

    :return:
    """
    # takes the file name from the user
    for arg1 in argv:
        file_name = arg1

    # creates the 'table' string
    if file_name.endswith('csv'):
        list_of_rows = make_a_list_of_rows_from_csv(file_name)
    else:
        list_of_rows = make_a_list_of_rows_from_txt(file_name)
    max_length_list = get_max_length_of_columns(list_of_rows)
    table_string = create_table_string(list_of_rows, max_length_list)

    # print the string for the user
    print(table_string)

if __name__ == '__main__':
    main()

