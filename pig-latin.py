""" Translates a word into Pig Latin """


def translate_begins_with_consonant(word):
    translation = word[1:] + 'ay'
    return translation

def translate_begins_with_vowel(word):
    translation = word + 'yay'
    return translation

def determines_first_ltr(word):
    if word.startswith(vowel_list):
        first_ltr = 'v'
    else:
        first_ltr = 'c'
    return first_ltr

def determines_last_ltr_punctuation(user_word):
    if not user_word[len(user_word) - 1].isalpha():
        punctuation = user_word[len(user_word) - 1]
    else:
        punctuation = ''
    return punctuation

def count_first_consonants(word):
    consonant_num = 0
    while word[consonant_num:] not in vowel_list\
            and consonant_num < len(word):
        consonant_num += 1
    return consonant_num

def check_first_letter_upper(word):
    if (word[0]).isupper() == True:
        is_upper = True
    else:
        is_upper = False
    return is_upper


# creates a string of vowels
vowel_list = 'a', 'e', 'i', 'o', 'u'

def main():

    # asks the user for a word to translate into Pig Latin
    user_word = input('Please give me a word to translate: -->')

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



# # check to see if the last character of the string is alpha
# if not translating_word[len(translating_word) - 1].isalpha():
#     # if the last character is not alpha, throw it into the variable punctuation
#     punctuation = translating_word[len(user_word) - 1]
#     # then take it off the end of the word
#     translating_word = translating_word[:len(translating_word) -1]
#
# # check to see if the word starts with a vowel from our list
# if not (translating_word.startswith(vowel_list)):
#     # if not, it creates an output word,
#     # takes off the first character,
#     # and adds 'ay' to the end
#     word = translating_word[1:] + 'ay'
# else:
#     # if there is a vowel, it adds 'yay' to the
#     # end of the output word
#     word = translating_word + 'yay'
#
# # check to see if the first character of the user input
# # was uppercase
# if (user_word[0]).isupper():
#     # if yes, change the case of 1st letter of the
#     # output string to a capital
#     word = (word[0]).swapcase() + word[1:]
#
# # check to see if anything was added to the punctuation string
# if punctuation:
#     # if yes, add the punctuation to the output word
#     word = word + punctuation

