"""Converts user input from one case type string to another

Case types include:
    * CamelCase
    * kebab-case
    * snake_case
    * CONSTANT_CASE
"""
CAMEL_CASE = 'camel'
KEBAB_CASE = 'kebab'
SNAKE_CASE = 'snake'
CONSTANT_CASE = 'constant'
NOT_A_CASE = 'unidentified'

def determine_case(case_string):
    """Finds the case type of a string

    possible cases include: snake_case (SNAKE_CASE), CamelCase (CAMEL_CASE),
    kebab-case (KEBAB_CASE), and CONSTANT_CASE (CONSTANT_CASE).
    If the case type is not one of those types, the function returns NOT_A_CASE

    :param case_string: entered by the user
    :return: the case type: CAMEL_CASE, CONSTANT_CASE, SNAKE_CASE, KEBAB_CASE, or NOT_A_CASE
    >>> determine_case('this_is_a_string')
    'snake'

    >>> determine_case('ThisIsAString')
    'camel'

    >>> determine_case('this-is-a-string')
    'kebab'

    >>> determine_case('THIS_IS_A_STRING')
    'constant'
    """
    if '_' in case_string:
        underscore = True
    else:
        underscore = False
    if '-' in case_string:
        dash = True
    else:
        dash = False
    if case_string.isupper():
        all_caps = True
    else:
        all_caps = False
    if all_caps == False:
        for char in case_string:
            if char.isupper():
                uppercase_ltr = True
                break
            else:
                uppercase_ltr = False
    else:
        uppercase_ltr = True
    return resolve_case_type(underscore, dash, all_caps, uppercase_ltr)


def resolve_case_type(underscore, dash, all_caps, uppercase_ltr):
    """Takes the parameters from the determine_case function and returns the case type

    possible cases include: snake_case (SNAKE_CASE), CamelCase (CAMEL_CASE),
    kebab-case (KEBAB_CASE), and CONSTANT_CASE (CONSTANT_CASE).
    If the case type is not one of those types, the function returns NOT_A_CASE

    :param underscore:
    :param dash:
    :param all_caps:
    :param uppercase_ltr:
    :return: the case type: CAMEL_CASE, CONSTANT_CASE, SNAKE_CASE, KEBAB_CASE, or NOT_A_CASE
    """
    if underscore == True and all_caps == False and dash == False and uppercase_ltr == False:
        case = SNAKE_CASE
    elif underscore == True and all_caps == True and dash == False:
        case = CONSTANT_CASE
    elif dash == True and all_caps == False and underscore == False and uppercase_ltr == False:
        case = KEBAB_CASE
    elif underscore == False and dash == False and all_caps == False and uppercase_ltr == True:
        case = CAMEL_CASE
    else:
        case = NOT_A_CASE
    return case

def create_intermediary_list(case_string, case_type):
    """Separates words into a lowercase list

    :param case_string:
    :param case_type:
    :return: list of lowercase words (from parsed string)
    >>> create_intermediary_list('this_is_a_snake_string', 'snake')
    ['this', 'is', 'a', 'snake', 'string']

    >>> create_intermediary_list('TheseAreSomeCamelWords', 'camel')
    ['these', 'are', 'some', 'camel', 'words']

    >>> create_intermediary_list('here-are-more-kebab-words', 'kebab')
    ['here', 'are', 'more', 'kebab', 'words']

    >>> create_intermediary_list('SOME_CONSTANT_WORDS_FOR_U', 'constant')
    ['some', 'constant', 'words', 'for', 'u']

    """
    if case_type == SNAKE_CASE:
        intermediate_list = snake_to_list(case_string)
    elif case_type == CAMEL_CASE:
        intermediate_list = camel_to_list(case_string)
    elif case_type == KEBAB_CASE:
        intermediate_list = kebab_to_list(case_string)
    elif case_type == CONSTANT_CASE:
        intermediate_list = constant_to_list(case_string)
    return intermediate_list

def snake_to_list(case_string):
    """Transforms snake_case string into a list of lowercase words

    :param case_string:
    :return: list of lowercase words
    >>> snake_to_list('snake_case_list_of_words')
    ['snake', 'case', 'list', 'of', 'words']

    >>> snake_to_list('busy_body')
    ['busy', 'body']
    """
    list_of_words = case_string.split('_')
    return list_of_words

def camel_to_list(case_string):
    """Transforms CamelCase string into a list of lowercase words

    :param case_string:
    :return:
    >>> camel_to_list('TheseAreSomeCamelWords')
    ['these', 'are', 'some', 'camel', 'words']

    """
    list_of_words = []
    y = 0
    for i, char in enumerate(case_string):
        if char.isupper() and not i == 0:
            single_word = ''.join(case_string[y:i])
            list_of_words.append(single_word.lower())
            y = i
        if i == len(case_string) - 1:
            single_word = ''.join(case_string[y:i + 1])
            list_of_words.append(single_word.lower())
    return list_of_words

def kebab_to_list(case_string):
    """Transforms kebab-case string into a list of lowercase words

    :param case_string:
    :return:
    >>> kebab_to_list('here-are-more-kebab-words')
    ['here', 'are', 'more', 'kebab', 'words']

    >>> kebab_to_list('this-exercise')
    ['this', 'exercise']
    """
    list_of_words = case_string.split('-')
    return list_of_words

def constant_to_list(case_string):
    """Transforms CONSTANT_CASE string into a list of lowercase words

    :param case_string:
    :return:
    >>> constant_to_list('SOME_CONSTANT_WORDS_FOR_U')
    ['some', 'constant', 'words', 'for', 'u']
    """
    list_of_words = []
    split_list_of_words = case_string.split('_')
    for word in split_list_of_words:
        list_of_words.append(word.lower())
    return list_of_words

def list_to_snake(intermediate_list):
    """Transforms list of lowercase words into snake_case

    :param intermediate_list:
    :return:

    >>> list_to_snake(['give', 'me', 'some', 'words', 'to', 'snake'])
    'give_me_some_words_to_snake'

    >>> list_to_snake(['more', 'words'])
    'more_words'
    """
    output_string = '_'.join(intermediate_list)
    return output_string

def list_to_camel(intermediate_list):
    """Transforms list of lowercase words into CamelCase

    :param intermediate_list:
    :return:

    >>> list_to_camel(['here', 'is', 'a', 'camel', 'string'])
    'HereIsACamelString'

    >>> list_to_camel(['best', 'word'])
    'BestWord'
    """
    first_ltr_upper_list = []
    for word in intermediate_list:
        first_ltr_upper_list.append(word.title())
    output_string = ''.join(first_ltr_upper_list)
    return output_string

def list_to_kebab(intermediate_list):
    """Transforms list of lowercase words into kebab-case

    :param intermediate_list:
    :return:

    >>> list_to_kebab(['example', 'of', 'kebab', 'case'])
    'example-of-kebab-case'

    >>> list_to_kebab(['check', 'word'])
    'check-word'
    """
    output_string = '-'.join(intermediate_list)
    return output_string

def list_to_constant(intermediate_list):
    """Transforms list of lowercase words into CONSTANT_CASE

    :param intermediate_list:
    :return:

    >>> list_to_constant(['constant', 'case', 'string'])
    'CONSTANT_CASE_STRING'

    >>> list_to_constant(['drink', 'me'])
    'DRINK_ME'
    """
    all_caps_list = []
    for word in intermediate_list:
        all_caps_list.append((word.upper()))
    output_string = '_'.join(all_caps_list)
    return output_string

def create_output_string(intermediate_list, output_case_type):
    """Transforms a word list into a string by case type

    :param intermediate_list:
    :param output_case_type:
    :return:

    >>> create_output_string(['this', 'is', 'a', 'snake'], 'snake')
    'this_is_a_snake'

    >>> create_output_string(['this', 'is', 'a', 'kebab'], 'kebab')
    'this-is-a-kebab'

    >>> create_output_string(['this', 'is', 'a', 'constant'], 'constant')
    'THIS_IS_A_CONSTANT'

    >>> create_output_string(['this', 'is', 'a', 'camel'], 'camel')
    'ThisIsACamel'
    """
    if output_case_type == SNAKE_CASE:
        output_string = list_to_snake(intermediate_list)
    elif output_case_type == KEBAB_CASE:
        output_string = list_to_kebab(intermediate_list)
    elif output_case_type == CAMEL_CASE:
        output_string = list_to_camel(intermediate_list)
    elif output_case_type == CONSTANT_CASE:
        output_string = list_to_constant(intermediate_list)
    return output_string


def main():
    """Takes a user string in a case type and transforms the string into user defined case type

    :return:
    """
    # get input from user:
    while True:
        original_string = input('Enter an expression in any of these cases: '
                            'snake_case, CamelCase, kebab-case, or CONSTANT_CASE >')
        case_type = determine_case(original_string)
        if case_type == 'unidentified':
            print('The case type in that expression is not recognized.')
            continue
        else:
            break


    while True:
        output_case = input('What case do you want to change to: '
                        'snake, camel, kebab, or constant: >')
        if output_case not in (SNAKE_CASE, KEBAB_CASE, CONSTANT_CASE, CAMEL_CASE):
            print('Sorry, I didn\'t understand that.')
            continue
        else:
            break

    # run through functions:
    intermediate_list = create_intermediary_list(original_string, case_type)
    output_string = create_output_string(intermediate_list, output_case)

    # output new string to user:
    print(original_string + ' to ' + output_case + ' is ' + output_string + '.')


if __name__ == '__main__':
    main()