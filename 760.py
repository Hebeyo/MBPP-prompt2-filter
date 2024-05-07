def unique_Element(arr,n):
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            return ('NO')
    return ('YES')
