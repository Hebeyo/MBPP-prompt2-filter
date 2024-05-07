def text_match_wordz(text):
    import re
    patterns = '\w*z.\w*'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return('Not matched!')
