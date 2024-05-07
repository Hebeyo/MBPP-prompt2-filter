import re
def check_char(string):
    if re.search(r'^[a-z]$|^([a-z]).*\1$', string):
        return "Valid"
    else:
        return "Invalid"
