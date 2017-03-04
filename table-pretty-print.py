from sys import argv

#file = open('sample.txt', 'r')
#whole_list = (file.readlines())


def make_a_list_of_rows(text_file):
    list_of_rows = []
    file = open(text_file, 'r')
    for list_line in file.readlines():
        list_of_rows.append(list_line.split())
    return list_of_rows

#print(list_by_rows)
def get_max_length_of_columns(list_by_rows):
    max_length_list = ([max(len(str(x)) for x in line) for line in zip(*list_by_rows)])
    return max_length_list

def print_pipe_line(max_length_list):
    print('|', end='')
    for column_length in max_length_list:
        print('-' * column_length + '|', end='')
    print('\r')

def print_row(list_of_rows, max_length_list):
    for index, list_of_rows in enumerate(list_of_rows):
        if index < 2:
            print_pipe_line(max_length_list)
        for i, item in enumerate(list_of_rows):
            justify_by = max_length_list[i]
            print('|' + str(item.ljust(justify_by)), end='')
        print('|')
    print_pipe_line(max_length_list)

def main():
    # input from user: argv
    for arg1 in argv:
        file_name = arg1


    # create the pretty print
    list_of_rows = make_a_list_of_rows(file_name)
    max_length_list = get_max_length_of_columns(list_of_rows)
    print_row(list_of_rows, max_length_list)

if __name__ == '__main__':
    main()

