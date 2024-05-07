def common_prefix(arr, n):
    if n == 0:
        return ""
    if n == 1:
        return arr[0]
    arr.sort()
    end = min(len(arr[0]), len(arr[n - 1]))
    i = 0
    while (i < end and arr[0][i] == arr[n - 1][i]):
        i += 1
    pre = arr[0][:i]
    return pre
