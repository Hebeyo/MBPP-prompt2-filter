def nth_items(list,n):
    new_list=[]
    for i in range(0,len(list),n):
        new_list.append(list[i])
    return new_list
