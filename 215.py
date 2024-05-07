def decode_list(alist):
    decoded_list = []
    for i in alist:
        if isinstance(i, list):
            decoded_list.extend([i[1]]*i[0])
        else:
            decoded_list.append(i)
    return decoded_list
