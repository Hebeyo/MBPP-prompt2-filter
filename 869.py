def remove_list_range(list1, leftrange, rigthrange):
    res = []
    for i in list1:
        if min(i)>=leftrange and max(i)<=rigthrange:
            res.append(i)
    return res
