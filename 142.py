def count_samepair(list1,list2,list3):
    result = 0
    for i in range(len(list1)):
        if list1[i] == list2[i] and list2[i] == list3[i]:
            result += 1
    return result
