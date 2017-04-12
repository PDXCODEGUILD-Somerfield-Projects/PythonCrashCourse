""" Translates a word into Pig Latin """


def translate_begins_with_consonant(word):
    """Translates a word starting with a consonant into Pig Latin

    Grabs the number of starting consonants from the function
    count_first_consonants.
        If there is more than one starting consonant, it takes
    those consonants and adds them to the end of the word
    and adds 'ay'.
        If there is one starting consonant, the function removes it
    and adds 'ay' to the end of the word.
        If there are no vowels in the word, it adds 'ay' to the end.
    Function returns the translated word.

    :param word:
    :return:

    >>> translate_begins_with_consonant('test')
    'estay'

    >>> translate_begins_with_consonant('string')
    'ingstray'

    >>> translate_begins_with_consonant('grrr')
    'grrray'
    """
    num_of_consonants = count_first_consonants(word)
    if num_of_consonants > 1:
        add_to_end = word[:num_of_consonants] + 'ay'
        translation = word[num_of_consonants:] + add_to_end
    else:
        translation = word[num_of_consonants:]  + 'ay'
    return translation

def translate_begins_with_vowel(word):
    """Translates a word beginning with a vowel into Pig Latin

    adds 'yay' to the end of the word and returns the translation

    :param word:
    :return:

    >>> translate_begins_with_vowel('aardvark')
    'aardvarkyay'

    >>> translate_begins_with_vowel('ugly')
    'uglyyay'

    """
    translation = word + 'yay'
    return translation

def determines_first_ltr(word):
    """Determines whether the first letter of a word is a consonant or vowel

    Returns 'v' if its a vowel, 'c' if its a consonant

    :param word:
    :return:

    >>> determines_first_ltr('guild')
    'c'

    >>> determines_first_ltr('olive')
    'v'
    """
    if word.startswith(vowel_list):
        first_ltr = 'v'
    else:
        first_ltr = 'c'
    return first_ltr

def determines_last_ltr_punctuation(user_word):
    """Checks to see if the last character of a string is not alpha

    If the last character is not alpha, it returns the character in
    a string. If it is alpha, it returns an empty string

    :param user_word:
    :return:

    >>> determines_last_ltr_punctuation('hello')
    ''

    >>> determines_last_ltr_punctuation('awesome!')
    '!'
    """
    if not user_word[len(user_word) - 1].isalpha():
        punctuation = user_word[len(user_word) - 1]
    else:
        punctuation = ''
    return punctuation

def count_first_consonants(word):
    """Counts the number of consonants at the beginning of a word

    Returns the number of consonants
    ** if there are no vowels in the word, it returns 0

    :param word:
    :return:

    >>> count_first_consonants('string')
    3

    >>> count_first_consonants('celery')
    1

    >>> count_first_consonants('grrr')
    0

    """
    vowel_locations = []
    # creates a list of vowel locations in the word
    for c in vowel_list:
        if c in word:
            vowel_locations.append(word.find(c))
    # determines the location of the first vowel (lowest location)
    if vowel_locations:
        num_consonant_string = min(vowel_locations)
    # if there are no vowels, returns 0
    else:
        num_consonant_string = 0
    return num_consonant_string

def check_first_letter_upper(word):
    """Check to see if the first letter is upper case

    If the first letter is upper case, returns True,
    otherwise, it returns False

    :param word:
    :return:

    >>> check_first_letter_upper('word')
    False

    >>> check_first_letter_upper('Word')
    True

    """
    if (word[0]).isupper() == True:
        is_upper = True
    else:
        is_upper = False
    return is_upper


# creates a string of vowels
vowel_list = 'a', 'e', 'i', 'o', 'u'

def main(user_word):
    """Translates an input word into Pig Latin

    Matches first letter case, last character punctuation,
    accounting for whether the word begins with one or multiple
    consonants or a vowel

    :return:

    >>> main('String')
    String in Pig Latin is Ingstray

    >>> main('Ovaltine!')
    Ovaltine! in Pig Latin is Ovaltineyay!

    >>> main('chair')
    chair in Pig Latin is airchay

    >>> main('streets.')
    streets. in Pig Latin is eetsstray.

    >>> main('aardvark,')
    aardvark, in Pig Latin is aardvarkyay,
    """

    # asks the user for a word to translate into Pig Latin
 ## COMMENTED OUT FOR TESTING   user_word = input('Please give me a word to translate: -->')

    # make a lowercase string we can manipulate from the user's word
    translating_word = (user_word).lower()

    punctuation = determines_last_ltr_punctuation(translating_word)

    if punctuation != '':
        translating_word = translating_word[:len(translating_word) -1]

    if determines_first_ltr(translating_word) == 'v':
        translating_word = translate_begins_with_vowel(translating_word)
    else:
        translating_word = translate_begins_with_consonant(translating_word)

    if check_first_letter_upper(user_word) == True:
        translating_word = translating_word[0].swapcase() + translating_word[1:]

    if punctuation != '':
        translating_word = translating_word + punctuation

    # output to the user
    print(user_word + ' in Pig Latin is ' + translating_word)




if __name__ == '__main__':
    main()


