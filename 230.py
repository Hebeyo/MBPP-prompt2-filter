def replace_blank(str1,char):
    str2 = ""
    for i in str1:
        if i == " ":
            str2 += char
        else:
            str2 += i
    return str2
