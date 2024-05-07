def find_Max_Num(arr,n) : 
    for i in range(n): 
        for j in range(n-i-1) : 
            if arr[j] < arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    num = 0
    for i in range(n) : 
        num = num * 10 + arr[i] 
    return num
