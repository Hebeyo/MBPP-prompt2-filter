def check_identical(test_list1, test_list2):
    for i in range(len(test_list1)):
        for j in range(len(test_list1[i])):
            if test_list1[i][j] != test_list2[i][j]:
                return False
    return True
