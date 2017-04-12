# gets list of words from user (in a string)
user_string = input("Enter a list of words separated by a space: >")

# creates a list of words from the user-provide string
word_list = user_string.split()

# counts the number of words in the list
word_count = len(word_list)

# if the number of words is 1:
# prints the word from the list (in 0 position)
if word_count == 1:
    print_string = (word_list[0])
# if the number of words is 2: creates a string
# concatenating the first word (0 position), the word 'and',
# and the second word (1 position)
elif word_count == 2:
    print_string = (''.join(word_list[0]) + ' and '
                          + ''.join (word_list[1]))
# if the number of words is more than 2:
elif word_count > 2:
    # inserts ', and ' before the last word (gets last comma in)
    words_to_print = (word_list[:(word_count - 1)]
                    + [', and '] + word_list[word_count - 1:])
    # creates a string, concatenating everything but the last
    # two words and adds a comma between them,
    print_string = ((', '.join(words_to_print[:word_count -1]))
    # then concatenates that with the last two words (with no comma)
                    + (''.join(words_to_print[word_count -1:])))
    # there are no words entered, adds this message to the print string
else:
    print_string = 'You didn\'t enter any words!'

# prints the message for the user
print(print_string)



