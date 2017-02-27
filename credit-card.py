"""Problem: credit-card practice - steps 4 - 6"""

def subtract_nine(cc_num_list):
    """

    :param cc_num_list:
    :return:
    >>> [10, 8, 18, 9, 16, 6, 16, 5, 14, 3, 14, 6, 10, 5, 8]
    [1, 8, 9, 9, 7, 6, 7, 5, 5, 3, 5, 6, 1, 5, 8]
    """
    sub_nine_list = [num - 9 if num > 9 else num for num in cc_num_list]
    return sub_nine_list


def sum_subtracted_values(cc_num_list):
    """

    :param cc_num_list:
    :return:
    >>> [1, 8, 9, 9, 7, 6, 7, 5, 5, 3, 5, 6, 1, 5, 8]
    85
    """
    sum_value = 0
    for num in cc_num_list:
        sum_value += num
    return sum_value

def ones_digit_of_sum(sum_value):
    """

    :param sum_value:
    :return:
    >>> 85
    5
    """
    sum_string = str(sum_value)
    ones_digit = int(sum_string[len(sum_string) - 1])
    return ones_digit



print(subtract_nine([10, 8, 18, 9, 16, 6, 16, 5, 14, 3, 14, 6, 10, 5, 8]))
print(sum_subtracted_values([1, 8, 9, 9, 7, 6, 7, 5, 5, 3, 5, 6, 1, 5, 8]))
print(ones_digit_of_sum(85))
