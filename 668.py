def replace(string, char):
    while char*2 in string:
        string = string.replace(char*2, char)
    return string
