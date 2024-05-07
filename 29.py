def get_Odd_Occurrence(arr,arr_size):   
    result = 0
    for i in range(0,arr_size): 
        result = result ^ arr[i] 
    return result
