def sequential_search(dlist, item):
    for i in range(len(dlist)):
        if dlist[i] == item:
            return True, i
    return False, -1
