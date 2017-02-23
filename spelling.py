"""
Checks to see if there the input word
has 'ie' or 'ei' and then checks if the word
follows the 'i before e, except after c' rule
"""
is_ie = False
is_ei = False
is_c = False


def check_for_ie(word):
    if 'ie' in word:
        position = word.index('ie')
        is_ie = True
        is_c = word[position - 1] == 'c'
        if (is_ie and is_c):
            rule = False
        else:
            rule = True
    else:
        rule = True
    return rule

def check_for_ei(word):
    if 'ei' in word:
        position = word.index('ei')
        is_ei = True
        is_c = word[position - 1] == 'c'
        if (is_ei and is_c):
            rule = True
        else:
            rule = False
    else:
        rule = True
    return rule

input_word = input('Word? -->')

check_word = input_word.lower()

follows_rule = check_for_ie(check_word) and check_for_ei(check_word)
if follows_rule:
    print_str = ' does follow the rule'
else:
    print_str = ' doesn\'t follow the rule'

print(input_word + print_str)