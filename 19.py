def test_duplicate(arraynums):
    for i in range(len(arraynums)):
        for j in range(i+1,len(arraynums)):
            if arraynums[i] == arraynums[j]:
                return True
    return False
