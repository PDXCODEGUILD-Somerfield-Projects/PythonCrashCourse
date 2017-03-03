""" function to find pairs that add up to a certain number """

import itertools

def find_sum_pairs(number_list, sum_to_search):
    """

    :param number_list:
    :param sum_to_search:
    :return:
    >>> find_sum_pairs([-1, 0, 1, 2], 3)
    [[1, 2]]

    >>> find_sum_pairs([-1, 0, 1, 2], 1)
    [[-1, 2], [0, 1]]

    >>> find_sum_pairs([2, -1, 2], 1)
    [[2, -1], [-1, 2]]

    >>> find_sum_pairs([-1, 1, 2, 2], 3)
    [[1, 2], [1, 2]]
    """
    answer_list = []
    for i in itertools.combinations(number_list, 2):
        if sum(i) == sum_to_search:
            answer_list.append(list(i))
    return answer_list

def find_sum_pairs_loop(number_list, sum_to_search):
    """

    :param number_list:
    :param sum_to_search:
    :return:

    >>> find_sum_pairs([-1, 0, 1, 2], 3)
    [[1, 2]]

    >>> find_sum_pairs([-1, 0, 1, 2], 1)
    [[-1, 2], [0, 1]]

    >>> find_sum_pairs([2, -1, 2], 1)
    [[2, -1], [-1, 2]]

    >>> find_sum_pairs([-1, 1, 2, 2], 3)
    [[1, 2], [1, 2]]
    """
    answer_list = []
    for index, num in enumerate(number_list):
        for i in number_list[index + 1:len(number_list)]:
            if num + i == sum_to_search:
                answer_list.append([num] + [i])
    return answer_list


def main():
    print(find_sum_pairs([-1, 0, 1, 2], 3))

    print(find_sum_pairs([-1, 0, 1, 2], 1))

    print(find_sum_pairs([2, -1, 2], 1))

    print(find_sum_pairs([-1, 1, 2, 2], 3))

    print(find_sum_pairs_loop([-1, 0, 1, 2], 3))

    print(find_sum_pairs_loop([-1, 0, 1, 2], 1))

    print(find_sum_pairs_loop([2, -1, 2], 1))

    print(find_sum_pairs_loop([-1, 1, 2, 2], 3))

if __name__ == '__main__':
    main()