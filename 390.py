def add_string(list,string):
    add_string=[]
    for i in list:
        add_string.append(string.format(i))
    return add_string
