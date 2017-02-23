""" Adds an oxford comma to a list of words"""

user_words = input("Enter a list of space separated words: >")

words_list = user_words.split()

word_total = len(words_list)

if word_total == 1:
    print_string = words_list[0]
elif word_total == 2:
    print_string = words_list[0] + ' and ' + words_list[1]
elif word_total > 2:
    words_list.insert(len(words_list) - 1, 'and')
    print_string = (', '.join(words_list[:-1]) + ' '
          + ' '.join(words_list[-1:]))
else:
    print_string = 'You didn\'t enter any words!'


print(print_string)