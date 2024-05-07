import re
def text_match_two_three(text):
    if re.search('ab{2,3}',  text):
        return 'Found a match!'
    else:
        return('Not matched!')
