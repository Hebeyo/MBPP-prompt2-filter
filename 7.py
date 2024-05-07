def find_char_long(text):
    import re
    return (re.findall(r"\b\w{4,}\b", text))
