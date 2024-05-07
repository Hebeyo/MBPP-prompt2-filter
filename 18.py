def remove_dirty_chars(string, second_string):
    temp = []
    for x in string:
        temp.append(x)
    count = [0] * 256
    for i in second_string:
        count[ord(i)] += 1
    ip_ind = 0
    res_ind = 0
    while ip_ind != len(temp):
        temp_char = temp[ip_ind]
        if count[ord(temp_char)] == 0:
            temp[res_ind] = temp[ip_ind]
            res_ind += 1
        ip_ind += 1
    return ''.join(temp[0:res_ind])
