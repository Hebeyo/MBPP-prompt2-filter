def reverse_list_lists(lists):
    for i in range(len(lists)):
        lists[i] = lists[i][::-1]
    return lists
