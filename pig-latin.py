""" Translates a word into Pig Latin """

vowel_list = 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'
user_word = 'latin'


if not (word.startswith(vowel_list)):
    word = user_word[1:] + 'ay'
else:
    word = user_word + 'yay'


print(word)