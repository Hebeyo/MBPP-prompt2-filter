def all_unique(test_list):
    unique_list = []
    for i in test_list:
        if i in unique_list:
            return False
        else:
            unique_list.append(i)
    return True
