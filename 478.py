def remove_lowercase(str1):
    str2 = ""
    for i in str1:
        if i.isupper():
            str2 += i
    return str2
