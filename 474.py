def replace_char(str1,ch,newch):
    str2 = ""
    for i in str1:
        if i==ch:
            str2 += newch
        else:
            str2 += i
    return str2
