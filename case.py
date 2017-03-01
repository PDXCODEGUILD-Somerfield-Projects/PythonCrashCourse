
def determine_case(case_string):
    """Finds the case type of a string

    possible cases include: snake_case ('snake'), CamelCase ('camel'),
    kebab-case ('kebab'), and CONSTANT_CASE ('constant'). If the case type is not one of those types,
    the function returns 'unidentified'

    :param case_string:
    :return:
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

    possible cases include: snake_case ('snake'), CamelCase ('camel'),
    kebab-case ('kebab'), and CONSTANT_CASE ('constant'). If the case type is not one of those types,
    the function returns 'unidentified'

    :param underscore:
    :param dash:
    :param all_caps:
    :param uppercase_ltr:
    :return:
    """
    if underscore == True and all_caps == False:
        case = 'snake'
    elif underscore == True and all_caps == True:
        case = 'constant'
    elif dash == True and all_caps == False:
        case = 'kebab'
    elif underscore == False and dash == False and all_caps == False and uppercase_ltr == True:
        case = 'camel'
    else:
        print('Not able to identify this case type.')
        exit()
    return case

def create_intermediary(case_string, case_type):
    """

    :param case_string:
    :param case_type:
    :return:
    >>> create_intermediary('this_is_a_snake_string', 'snake')
    ['this', 'is', 'a', 'snake', 'string']

    >>> create_intermediary('TheseAreSomeCamelWords', 'camel')
    ['these', 'are', 'some', 'camel', 'words']

    >>> create_intermediary('here-are-more-kebab-words', 'kebab')
    ['here', 'are', 'more', 'kebab', 'words']

    >>> create_intermediary('SOME_CONSTANT_WORDS_FOR_U', 'constant')
    ['some', 'constant', 'words', 'for', 'u']

    """
    if case_type == 'snake':
        intermediate_list = snake_to_list(case_string)
    elif case_type == 'camel':
        intermediate_list = camel_to_list(case_string)
    elif case_type == 'kebab':
        intermediate_list = kebab_to_list(case_string)
    elif case_type == 'constant':
        intermediate_list = constant_to_list(case_string)
    return intermediate_list

def snake_to_list(case_string):
    """

    :param case_string:
    :return:
    >>> snake_to_list('snake_case_list_of_words')
    ['snake', 'case', 'list', 'of', 'words']

    >>> snake_to_list('busy_body')
    ['busy', 'body']
    """
    list_of_words = case_string.split('_')
    return list_of_words

def camel_to_list(case_string):
    """

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
    """

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
    """

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

def intermediate_to_snake(intermediate_list):
    """

    :param intermediate_list:
    :return:

    >>> intermediate_to_snake(['give', 'me', 'some', 'words', 'to', 'snake'])
    'give_me_some_words_to_snake'

    >>> intermediate_to_snake(['more', 'words'])
    'more_words'
    """
    output_string = '_'.join(intermediate_list)
    return output_string

def intermediate_to_camel(intermediate_list):
    """

    :param intermediate_list:
    :return:

    >>> intermediate_to_camel(['here', 'is', 'a', 'camel', 'string'])
    'HereIsACamelString'

    >>> intermediate_to_camel(['best', 'word'])
    'BestWord'
    """
    first_ltr_upper_list = []
    for word in intermediate_list:
        first_ltr_upper_list.append(word.title())
    output_string = ''.join(first_ltr_upper_list)
    return output_string

def intermediate_to_kebab(intermediate_list):
    """

    :param intermediate_list:
    :return:

    >>> intermediate_to_kebab(['example', 'of', 'kebab', 'case'])
    'example-of-kebab-case'

    >>> intermediate_to_kebab(['check', 'word'])
    'check-word'
    """
    output_string = '-'.join(intermediate_list)
    return output_string

def intermediate_to_constant(intermediate_list):
    """

    :param intermediate_list:
    :return:

    >>> intermediate_to_constant(['constant', 'case', 'string'])
    'CONSTANT_CASE_STRING'

    >>> intermediate_to_constant(['drink', 'me'])
    'DRINK_ME'
    """
    all_caps_list = []
    for word in intermediate_list:
        all_caps_list.append((word.upper()))
    output_string = '_'.join(all_caps_list)
    return output_string

def create_output_string(intermediate_list, output_case_type):
    """

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
    if output_case_type == 'snake':
        output_string = intermediate_to_snake(intermediate_list)
    elif output_case_type == 'kebab':
        output_string = intermediate_to_kebab(intermediate_list)
    elif output_case_type == 'camel':
        output_string = intermediate_to_camel(intermediate_list)
    elif output_case_type == 'constant':
        output_string = intermediate_to_constant(intermediate_list)
    return output_string


def main():
    # get input from user:
    original_string = input('Enter an expression in any of these cases: '
                            'snake_case, CamelCase, kebab-case, or CONSTANT_CASE >')
    output_case = input('What case do you want to change to: '
                        'snake, camel, kebab, or constant: >')

    # run through functions:
    case_type = determine_case(original_string)

    intermediate_list = create_intermediary(original_string, case_type)

    output_string = create_output_string(intermediate_list, output_case)


    # output new string to user:
    print(original_string + ' to ' + output_case  + ' is ' + output_string + '.')


if __name__ == '__main__':
    main()