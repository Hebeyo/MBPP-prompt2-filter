def check_subset(list1, list2):
    for i in list2:
        if i not in list1:
            return False
    return True
