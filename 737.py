import re
def check_str(string):
    pattern = '^[aeiouAEIOU][A-Za-z0-9_]*'
    if re.match(pattern, string):
        return 'Valid'
    else:
        return 'Invalid'
