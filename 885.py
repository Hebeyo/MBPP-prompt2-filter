def is_Isomorphic(str1,str2):
    if len(str1) != len(str2):
        return False
    dict_str1 = {}
    dict_str2 = {}
    for i, value in enumerate(str1):
        dict_str1[value] = dict_str1.get(value,[]) + [i]
    for j, value in enumerate(str2):
        dict_str2[value] = dict_str2.get(value,[]) + [j]
    if sorted(dict_str1.values()) == sorted(dict_str2.values()):
        return True
    else:
        return False
