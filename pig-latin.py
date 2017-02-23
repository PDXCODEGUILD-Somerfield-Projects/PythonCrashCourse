""" Translates a word into Pig Latin """

# creates a string of vowels
vowel_list = 'a', 'e', 'i', 'o', 'u'

# creates a string to store punctuation
punctuation = ''

# asks the user for a word to translate into Pig Latin
user_word = input('Please give me a word to translate: -->')

# make a lowercase string we can manipulate from the user's word
translating_word = (user_word).lower()

# check to see if the last character of the string is alpha
if not translating_word[len(translating_word) - 1].isalpha():
    # if the last character is not alpha, throw it into the variable punctuation
    punctuation = translating_word[len(user_word) - 1]
    # then take it off the end of the word
    translating_word = translating_word[:len(translating_word) -1]

# check to see if the word starts with a vowel from our list
if not (translating_word.startswith(vowel_list)):
    # if not, it creates an output word,
    # takes off the first character,
    # and adds 'ay' to the end
    word = translating_word[1:] + 'ay'
else:
    # if there is a vowel, it adds 'yay' to the
    # end of the output word
    word = translating_word + 'yay'

# check to see if the first character of the user input
# was uppercase
if (user_word[0]).isupper():
    # if yes, change the case of 1st letter of the
    # output string to a capital
    word = (word[0]).swapcase() + word[1:]

# check to see if anything was added to the punctuation string
if punctuation:
    # if yes, add the punctuation to the output word
    word = word + punctuation

# output to the user
print(user_word + ' in Pig Latin is ' + word)